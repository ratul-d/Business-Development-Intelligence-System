from src.scoring.weights import SCORING_WEIGHTS
from src.scoring import rules

def score_lead(row):
    score = 0
    breakdown = {}

    # Role Fit
    if rules.role_fit(row.get("title", "")):
        score += SCORING_WEIGHTS["role_fit"]
        breakdown["role_fit"] = SCORING_WEIGHTS["role_fit"]

    # Scientific Intent
    if rules.scientific_intent(row.get("active_researcher")):
        score += SCORING_WEIGHTS["scientific_intent"]
        breakdown["scientific_intent"] = SCORING_WEIGHTS["scientific_intent"]

    # Company Intent
    if rules.company_intent(row.get("funding_stage")):
        score += SCORING_WEIGHTS["company_intent"]
        breakdown["company_intent"] = SCORING_WEIGHTS["company_intent"]

    # Technographic
    if rules.technographic_signal(row.get("active_researcher"),row.get("has_nih_grant")):
        score += SCORING_WEIGHTS["technographic"]
        breakdown["technographic"] = SCORING_WEIGHTS["technographic"]

    # Location Hub
    if rules.location_hub(row.get("company_hq_city")):
        score += SCORING_WEIGHTS["location_hub"]
        breakdown["location_hub"] = SCORING_WEIGHTS["location_hub"]

    # New Hire Bonus
    if rules.new_hire(row.get("new_hire")):
        score += SCORING_WEIGHTS["new_hire_bonus"]
        breakdown["new_hire_bonus"] = SCORING_WEIGHTS["new_hire_bonus"]

    return min(score,100), breakdown