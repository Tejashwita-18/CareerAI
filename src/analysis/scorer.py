from typing import Set

class ResumeScorer:
    """
    Calculates different scores used during resume analysis.
    """

    def calculate_skill_score(self, resume_skills: Set[str], jd_skills: Set[str]) -> tuple[float, list[str], list[str]]:
        """
        Compare resume skills against job description skills.

        Parameters:
            resume_skills (Set[str]): Skills extracted from the resume.
            jd_skills (Set[str]): Skills extracted from the job description.

        Returns:
            tuple:
                - Overall skill matched percentage
                - Matched skills
                - Missing skills
        """

        matched_skills = sorted(resume_skills.intersection(jd_skills))
        missing_skills = sorted(jd_skills.difference(resume_skills))

        if not jd_skills:
            score = 0.0
        else:
            score = (len(matched_skills) / len(jd_skills)) * 100
        
        return score, matched_skills, missing_skills
    
    def calculate_keyword_score(self) -> float:
        """
        Placeholder for keyword relevance scoring.
        """

        return 100.0
    
    def calculate_education_score(self) -> float:
        """
        Placeholder for education matching.
        """

        return 100.0
    
    def calculate_experience_score(self) -> float:
        """
        Placeholder for experience matching.
        """

        return 100.0
