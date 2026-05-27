def analyze_skill_gap(user_skills, jobs):
    user_skills_lower = [s.lower() for s in user_skills]
    result = []

    for job in jobs:
        required = [s.lower() for s in job['required_skills']]
        matched = [s for s in required if s in user_skills_lower]
        missing = [s for s in required if s not in user_skills_lower]

        match_percent = round((len(matched) / len(required)) * 100) if required else 0

        result.append({
            "job_title":      job['title'],
            "company":        job['company'],
            "match_score":    job.get('match_score', 0),
            "matched_skills": matched,
            "missing_skills": missing,
            "skill_match_%":  match_percent
        })

    return result