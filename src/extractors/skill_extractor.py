SKILLS = {

    "Programming": [
        "python",
        "sql",
        "java",
        "c++",
        "javascript",
        "bash"
    ],

    "Data Analytics": [
        "data analysis",
        "data cleaning",
        "data visualization",
        "statistical analysis",
        "reporting",
        "dashboarding",
        "power bi",
        "tableau",
        "excel",
        "pandas",
        "numpy"
    ],

    "Machine Learning": [
        "machine learning",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "xgboost"
    ],

    "Cloud": [
        "aws",
        "azure",
        "gcp"
    ],

    "Data Engineering": [
        "airflow",
        "spark",
        "hadoop",
        "kafka"
    ],

    "Tools": [
        "jenkins",
        "grafana",
        "git",
        "linux"
    ],

    "Databases": [
        "postgresql",
        "mysql",
        "mongodb",
        "oracle"
    ]
}

def extract_skills(text: str) -> dict:
    """
    Extract skills from resume texts.

    Args:
        text (str): Resume text
    
    Returns:
        dict: Skills grouped by category
    """

    text = text.lower()

    extracted_skills = {}

    for category, skills in SKILLS.items():
        found_skills = []

        for skill in skills:
            if skill in text:
                found_skills.append(skill)
        
        extracted_skills[category] = found_skills
    
    return extracted_skills
