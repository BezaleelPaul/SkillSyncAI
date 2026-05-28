import json
import os

def analyze(detected_skills, role):
    """
    Analyzes detected skills against the required skills for a specific role.
    """
    db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'skills_db.json')
    
    with open(db_path, 'r') as f:
        db = json.load(f)
    
    required_skills = db['roles'].get(role, [])
    
    matched = [skill for skill in detected_skills if skill in required_skills]
    missing = [skill for skill in required_skills if skill not in detected_skills]
    
    return {
        "required": required_skills,
        "matched": matched,
        "missing": missing
    }
