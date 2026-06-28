from src.resume_parser import extract_resume_text
from src.jd_parser import extract_jd_text

from src.skill_extractor import extract_skills

resume_text = extract_resume_text("data/resumes/Tejashwita_Priya_final_Resume.pdf")
jd_text = extract_jd_text("data/jobs/job.text")

resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(jd_text)

print("Resume skills")
print(resume_skills)

print("\nJob skills")
print(jd_skills)
