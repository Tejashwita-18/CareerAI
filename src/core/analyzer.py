from src.parsers.resume_parser import extract_resume_text
from src.parsers.jd_parser import extract_jd_text
from src.extractors.skill_extractor import extract_skills
from src.analysis.scorer import ResumeScorer
from src.analysis.ats_checker import ATSChecker

def analyze_resume(resume_path: str, jd_path: str):
    """
    Complete pipeline for analyzing a resume against
    a job description.
    """

    resume_text = extract_resume_text(resume_path)
    jd_text = extract_jd_text(jd_path)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    scorer = ResumeScorer()

    ats_checker = ATSChecker()

    score, matched, missing = scorer.calculate_skill_score(resume_skills, jd_skills)

    ats_result = ats_checker.check_resume(resume_text)

    return {
        "score": score,
        "matched": matched,
        "missing": missing,
        "ats_score": ats_result["ats_score"],
        "ats_issues": ats_result["issues"],
        "resume_skills": resume_skills,
        "jd_skills": jd_skills
    }
