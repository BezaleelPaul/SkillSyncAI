from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
import json
import uuid

# Import custom modules
from modules.resume_parser import extract_text
from modules.skill_extractor import extract_skills
from modules.analyzer import analyze
from modules.score_generator import generate_score
from modules.recommender import recommend

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configuration
UPLOAD_FOLDER = 'resumes'
REPORT_FOLDER = 'reports'
ALLOWED_EXTENSIONS = {'pdf', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['REPORT_FOLDER'] = REPORT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_roles():
    db_path = os.path.join('database', 'skills_db.json')
    with open(db_path, 'r') as f:
        db = json.load(f)
    return sorted(list(db['roles'].keys()))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    roles = get_roles()
    return render_template('upload.html', roles=roles)

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    if 'resume' not in request.files or 'role' not in request.form:
        flash('Missing file or job role selection.')
        return redirect(request.url)
    
    file = request.files['resume']
    role = request.form['role']
    
    if file.filename == '':
        flash('No selected file.')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Add UUID to filename to avoid collisions
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        try:
            # 1. Extract Text
            text = extract_text(filepath)
            
            # 2. Extract Skills
            detected_skills = extract_skills(text)
            
            # 3. Analyze against Role
            analysis = analyze(detected_skills, role)
            
            # 4. Generate Score
            score = generate_score(analysis['matched'], analysis['required'])
            
            # 5. Get Recommendations
            recommendations = recommend(analysis['missing'])
            
            # 6. Generate Report File
            report_filename = f"report_{unique_filename.rsplit('.', 1)[0]}.txt"
            report_path = os.path.join(app.config['REPORT_FOLDER'], report_filename)
            
            with open(report_path, 'w') as f:
                f.write("SKILLSYNC AI - RESUME ANALYSIS REPORT\n")
                f.write("====================================\n\n")
                f.write(f"Target Role: {role}\n")
                f.write(f"Employability Score: {score['score']}% ({score['label']})\n\n")
                f.write("DETECTED SKILLS:\n")
                f.write(", ".join(analysis['matched']) if analysis['matched'] else "None detected")
                f.write("\n\n")
                f.write("MISSING SKILLS:\n")
                f.write(", ".join(analysis['missing']) if analysis['missing'] else "None! You are a perfect match.")
                f.write("\n\n")
                f.write("RECOMMENDATIONS:\n")
                for rec in recommendations:
                    f.write(f"- {rec['skill']}: {rec['tip']}\n")
                    f.write(f"  Resource: {rec['url']}\n")
            
            return render_template('result.html', 
                                 role=role,
                                 analysis=analysis, 
                                 score=score, 
                                 recommendations=recommendations,
                                 report_filename=report_filename)
            
        except Exception as e:
            flash(f"Error processing resume: {str(e)}")
            return redirect(url_for('upload'))
    else:
        flash('Allowed file types are .pdf and .txt')
        return redirect(request.url)

@app.route('/download-report/<filename>')
def download_report(filename):
    return send_from_directory(app.config['REPORT_FOLDER'], filename, as_attachment=True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(debug=True)
