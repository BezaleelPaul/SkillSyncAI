# SkillSync AI – Resume & Skill Gap Analyzer

SkillSync AI is a modern web application designed to help job seekers identify the gap between their current skills and the requirements of their target job roles. Using AI-powered text extraction and keyword matching, it provides an employability score and a personalized learning roadmap.

## 🚀 Features

- **Multi-Format Parsing**: Supports PDF and TXT resumes using `pdfplumber` and `PyPDF2`.
- **Intelligent Skill Extraction**: Matches resume content against a comprehensive database of job roles and required skills.
- **Gap Analysis**: Identifies exactly which skills are missing for a selected job role.
- **Employability Scoring**: Calculates a percentage score based on industry-standard requirements.
- **Personalized Recommendations**: Provides curated learning resources and strategic tips for every missing skill.
- **Automated Reports**: Generates a downloadable plaintext report for offline review.
- **Modern UI**: Dark-themed, responsive interface with Bootstrap 5 and interactive animations.

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3, Flask |
| **Parsing** | pdfplumber, PyPDF2 |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5 |
| **Database** | JSON (Flat-file) |

## 📂 Folder Structure

```
SkillSyncAI/
├── app.py                # Main Flask application
├── requirements.txt      # Dependencies
├── README.md             # Documentation
├── resumes/              # Uploaded resumes (auto-generated)
├── reports/              # Generated analysis reports (auto-generated)
├── static/               # CSS and JS assets
├── templates/            # HTML templates (Jinja2)
├── modules/              # Core logic (Parser, Extractor, Analyzer, etc.)
└── database/             # Skills and courses database (JSON)
```

## ⚙️ Installation

1. **Clone the repository** (or copy the files):
   ```bash
   # Create the directory
   mkdir SkillSyncAI
   cd SkillSyncAI
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the App**:
   Open your browser and navigate to `http://127.0.0.1:5000`

## 📖 Usage

1. **Upload**: Select your resume file (.pdf or .txt) and your target job role (e.g., Python Developer).
2. **Analyze**: Click "Analyze My Resume" to start the process.
3. **Review**: View your employability score, matched skills, and missing skills.
4. **Learn**: Click on the "Learn Now" links to bridge your skill gaps using the provided resources.
5. **Download**: Get your full report by clicking "Download Full Report".

## 🔮 Future Enhancements

- **NLP Integration**: Use SpaCy or Transformers for more nuanced skill extraction (handling synonyms).
- **Authentication**: Allow users to save their analysis history.
- **Direct Integration**: Pull job requirements directly from LinkedIn or Indeed APIs.
- **Rich Reports**: Export reports as PDF with charts and visualizations.

---

**Author:** [Your Name/Placeholder]
**Version:** 1.0.0
