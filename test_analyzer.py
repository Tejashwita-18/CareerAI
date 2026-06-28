from src.services.analyzer import analyze_resume

result = analyze_resume(
    "data/resumes/Tejashwita_Priya_final_Resume.pdf",
    "data/jobs/job.text"
)

print(result)
