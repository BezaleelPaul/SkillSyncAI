import json
import os

def recommend(missing_skills):
    """
    Provides learning recommendations for missing skills.
    """
    db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'skills_db.json')
    
    with open(db_path, 'r') as f:
        db = json.load(f)
    
    courses = db.get('courses', {})
    recommendations = []
    
    for skill in missing_skills:
        url = courses.get(skill, "https://www.google.com/search?q=learn+" + skill.replace(" ", "+"))
        tip = f"Complete a project or certification in {skill} to strengthen your profile."
        
        # Specific tips for some common skills
        if "Flask" in skill or "Django" in skill:
            tip = f"Build 2 web projects using {skill} to solidify this skill."
        elif "Python" in skill:
            tip = "Solve 50+ LeetCode problems in Python to master syntax and logic."
        elif "Docker" in skill or "Kubernetes" in skill:
            tip = f"Deploy a multi-container app using {skill} on a cloud platform."
            
        recommendations.append({
            "skill": skill,
            "url": url,
            "tip": tip
        })
        
    return sorted(recommendations, key=lambda x: x['skill'])
