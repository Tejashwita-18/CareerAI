from src.resume_parser import extract_resume_text
from src.jd_parser import extract_jd_text
from src.skill_extractor import extract_skills
from src.matcher import caculate_match

def analyze_resume(resume_path: str, jd_path: str):
    """
    Complete pipeline for analyzing a resume against
    a job description.
    """

    resume_text = extract_resume_text(resume_path)
    jd_text = extract_jd_text(jd_path)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    score, matched, missing = caculate_match(resume_skills, jd_skills)

    return {
        "score": score,
        "matched": matched,
        "missing": missing,
        "resume_skills": resume_skills,
        "jd_skills": jd_skills
    }
