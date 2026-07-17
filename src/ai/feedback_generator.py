from src.ai.prompt_builder import build_resume_feedback_prompt
from src.ai.gemini_client import GeminiClient

def generate_ai_feedback(
        resume_text,
        jd_text,
        score,
        matched,
        missing,
        ats_score,
        ats_issues
):
    """
    Generate AI-powered resume feedback.
    """

    prompt = build_resume_feedback_prompt(
        resume_text = resume_text,
        jd_text = jd_text,
        score = score,
        matched = matched,
        missing = missing,
        ats_score = ats_score,
        ats_issues = ats_issues
    )

    try:
        client = GeminiClient()
        return client.generate_feedback(prompt)
    
    except Exception as e:
        return(
            "⚠️ AI feedback is currently unavailable.\n\n"
            f"Error: {str(e)}"
        )
