import re

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
        checks = {}

        text = resume_text.lower()

        # ----------------------------------
        #          Resume Length
        # ----------------------------------

        word_count = len(resume_text.split())

        if word_count < 200:
            score -= 15
            issues.append("Resume is too short.")
            checks["Resume Length"] = False
        elif word_count > 1000:
            score -= 10
            issues.append("Resume is too long.")
            checks["Resume Length"] = False
        else:
            checks["Resume Length"] = True

        # ----------------------------------
        #              Email
        # ----------------------------------

        email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        if re.search(email_pattern, resume_text):
            checks["Email"] = True
        else:
            score -= 20
            issues.append("Email address not found.")
            checks["Email"] = False

        # ----------------------------------
        #          Phone Number
        # ----------------------------------

        phone_pattern = r"(\+?\d[\d\s\-]{8,}\d)"

        if re.search(phone_pattern, resume_text):
            checks["Phone Number"] = True
        else:
            score -= 20
            issues.append("Phone number not found.")
            checks["Phone Number"] = False

        # ----------------------------------
        #            LinkedIn
        # ----------------------------------

        if "linkedin.com" in text:
            checks["LinkedIn"] = True
        else:
            score -= 5
            issues.append("LinkedIn profile not found.")
            checks["LinkedIn"] = False

        # ----------------------------------
        #             Github
        # ----------------------------------

        if "github.com" in text:
            checks["Github"] = True
        else:
            score -= 5
            issues.append("Github profile not found.")
            checks["Github"] = False

        score = max(score, 0)

        return {
            "ats_score": score,
            "issues" : issues,
            "checks" : checks
        }
