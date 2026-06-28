from src.resume_parser import extract_resume_text
from src.jd_parser import extract_jd_text
from src.skill_extractor import extract_skills
from src.matcher import caculate_match

# Read files
resume_text = extract_resume_text("data/resumes/Tejashwita_Priya_final_Resume.pdf")
jd_text = extract_jd_text("data/jobs/job.text")

# Extract skills
resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(jd_text)

# Compare
score, matched, missing = caculate_match(resume_skills, jd_skills)

print("="*70)
print(f"Match score: {score}%")
print("="*70)

print("\n✅ Matched Skills:")

for skill in sorted(matched):
    print(f"  ✓ {skill}")

print("\n❌ Missing Skills:")

for skill in sorted(missing):
    print(f"  ✗ {skill}")
