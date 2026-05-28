def generate_score(matched, required):
    """
    Generates an employability score based on matched vs required skills.
    """
    if not required:
        return {"score": 0, "label": "Beginner"}
    
    score = int((len(matched) / len(required)) * 100)
    
    if score >= 80:
        label = "Industry Ready"
    elif score >= 60:
        label = "Intermediate"
    else:
        label = "Beginner"
        
    return {
        "score": score,
        "label": label
    }
