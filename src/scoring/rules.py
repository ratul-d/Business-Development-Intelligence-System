def role_fit(title: str):
    text = f"{title}".lower()
    return any(k in text for k in [
        "toxicology", "safety", "hepatic", "preclinical", "3d"
    ])

def scientific_intent(active_researcher: None):
    return active_researcher is True

def company_intent(funding_stage: str):
    if not funding_stage or not isinstance(funding_stage, str):
        return False
    return funding_stage.lower() in {"series a","series b"}

def technographic_signal(active_researcher: bool, has_grant: bool):
    """
    If they publish OR receive grants in liver / 3D space,
    they are likely using or open to advanced models.
    """
    return bool(active_researcher or has_grant)

def location_hub(company_hq_city: str):
    if not company_hq_city or not isinstance(company_hq_city, str):
        return False
    return company_hq_city.lower() in {
        "boston", "cambridge", "san francisco",
        "basel", "london", "oxford"
    }

def new_hire(new_hire_flag):
    return new_hire_flag is True