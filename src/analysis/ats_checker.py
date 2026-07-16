class ATSChecker:
    """
    Performs basic ATS compatibility checks.
    """

    def check_resume(self, resume_text: str) -> dict:
        """
        Analyze resume for ATS compatibility.
        """

        score = 100
        issues = []

        # Check resume length
        word_count = len(resume_text.split())

        if word_count < 200:
            score -= 15
            issues.append("Resume is too short.")
        elif word_count > 1000:
            score -= 10
            issues.append("Resume is too long.")

        # Check for email
        if '@' not in resume_text:
            score -= 20
            issues.append("Email address was not found.")

        # Check for phone number
        has_phone = any(char.isdigit() for char in resume_text)

        if not has_phone:
            score -= 20
            issues.append("Phone number was not found.")

        score = max(score, 0)

        return {
            "ats_score": score,
            "issues" : issues
        }
