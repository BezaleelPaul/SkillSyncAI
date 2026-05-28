import json
import os
import re

def extract_skills(text):
    """
    Extracts skills from text by matching against a master list from skills_db.json.
    """
    db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'skills_db.json')
    
    with open(db_path, 'r') as f:
        db = json.load(f)
    
    # Create a unique list of all skills across all roles
    all_skills = set()
    for role_skills in db['roles'].values():
        for skill in role_skills:
            all_skills.add(skill)
    
    detected_skills = []
    
    # Case-insensitive keyword matching
    for skill in all_skills:
        # Use regex to match whole words/phrases to avoid partial matches (e.g., 'R' in 'React')
        # However, some skills are short (C, R), so we need to be careful.
        # Simple word boundary might not work for 'C++', so we use a more robust pattern if needed.
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text, re.IGNORECASE):
            detected_skills.append(skill)
            
    return sorted(list(set(detected_skills)))
