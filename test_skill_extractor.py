from src.resume_parser import extract_resume_text
from src.skill_extractor import extract_skills

resume_text = extract_resume_text("data/resumes/Tejashwita_Priya_final_Resume.pdf")

skills = extract_skills(resume_text)

for category, skill_list in skills.items():

    print(f"\n{category}")

    for skill in skill_list:
        print(f"  ✓ {skill}")
