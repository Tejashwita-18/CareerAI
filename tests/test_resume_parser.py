from src.parsers.resume_parser import extract_resume_text

# resume_text = extract_resume_text("data/resumes/Tejashwita_Priya_final_Resume.pdf")

# print(resume_text)

def test_extract_resume_text():

    resume_text = extract_resume_text(
        "data/resumes/Tejashwita_Priya_final_Resume.pdf"
    )

    assert isinstance(resume_text, str)
    assert len(resume_text) > 0
