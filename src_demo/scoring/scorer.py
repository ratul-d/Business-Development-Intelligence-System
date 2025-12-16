import yaml

weights = yaml.safe_load(open("src_demo/config/scoring_weights.yaml"))
hubs = yaml.safe_load(open("src_demo/config/hubs.yaml"))
keywords = yaml.safe_load(open("src_demo/config/keywords.yaml"))

def score(row):
    score = 0
    breakdown = {}

    title = row["title"].lower()

    if any(k in title for k in keywords["role_keywords"]):
        score += weights["role_fit"]
        breakdown["role_fit"] = weights["role_fit"]

    if row["scientific_intent"]:
        score += weights["scientific_intent"]
        breakdown["scientific_intent"] = weights["scientific_intent"]

    funding = str(row.get("funding_stage", "")).lower()
    if funding in weights["funding"]:
        score += weights["funding"][funding]
        breakdown["funding"] = weights["funding"][funding]

    if row["company_hq"] in hubs:
        score += weights["location_hub"]
        breakdown["location"] = weights["location_hub"]

    if "in vitro" in str(row.get("company_description", "")).lower():
        score += weights["technographic"]
        breakdown["technographic"] = weights["technographic"]

    return score, breakdown