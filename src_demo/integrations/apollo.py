import os
import requests

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")

def enrich_email(name, company):
    if not APOLLO_API_KEY:
        return None

    url = "https://api.apollo.io/v1/people/match"
    payload = {
        "api_key":APOLLO_API_KEY,
        "name": name,
        "orgnization_name": company
    }
    r = requests.post(url, json=payload)
    if r.status_code ==  200:
        return r.json().get("person", {}).get("email")
    return None

def dummy_enrich_email(name: str, company: str) -> str:
    """
    Dummy Apollo email enrichment.
    Generates a realistic business email based on name + company.

    This is used when APOLLO_API_KEY is not provided.
    Safe for demos, assignments, and offline testing.
    """

    if not name or not company:
        return None

    # Normalize inputs
    name_parts = name.lower().replace("dr ", "").split()
    company_domain = company.lower().replace(" ", "").replace(",", "") + ".com"

    # Common email patterns
    if len(name_parts) >= 2:
        first = name_parts[0]
        last = name_parts[-1]
        email = f"{first}.{last}@{company_domain}"
    else:
        email = f"{name_parts[0]}@{company_domain}"

    return email
