def caculate_match(resume_skills: dict, jd_skills: dict):
    """
    Compare resume skills with job description skills

    Parameters:
        resume_skills: Skills extracted from the resume
        jd_skills: Skills extracted from job description

    Returns:
        tuple:
            match_score (float)
            matched_skills (set)
            missing_skills (set)
    """

    resume_set = set()
    jd_set = set()

    # Convert resume dictionary into a set
    for skills in resume_skills.values():
        resume_set.update(skills)

    # Convert JD dictionary into a set
    for skills in jd_skills.values():
        jd_set.update(skills)

    matched_skills = resume_set.intersection(jd_set)
    missing_skills = jd_set - resume_set

    if len(jd_set) == 0:
        match_score = 0.0
    else:
        match_score = round(
            (len(matched_skills) / len(jd_set)) * 100,
            2
        )
    
    return match_score, matched_skills, missing_skills
