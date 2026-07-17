def build_resume_feedback_prompt(
        resume_text: str,
        jd_text: str,
        score: float,
        matched: list[str],
        missing: list[str],
        ats_score: int,
        ats_issues: list[str]
) -> str:
    """
    Build a prompt for Gemini to generate
    personalized resume feedback.
    """

    prompt = f"""
You are an experienced technical recruiter and career coach.

Below is a candidate's resume and the job description.

{resume_text}

{jd_text}

Analyze the following resume analysis results.

Match Score:
{score:.1f}%

ATS Score:
{ats_score}%

Matched Skills:
{", ".join(matched) if matched else "None"}

Missing Skills:
{", ".join(missing) if missing else "None"}

ATS Issues:
{chr(10).join(ats_issues) if ats_issues else "None"}

Generate your response in this format:

1. Overall Assessment

2. Strengths

3. Weaknesses

4. Resume Improvements

5. Learning Roadmap

6. Final Career Advice

Keep the advice concise, practical and encouraging.
"""
    return prompt
