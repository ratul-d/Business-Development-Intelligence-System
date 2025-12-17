import os
import requests

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")

def enrich_contact_apollo(name, company):
    if not APOLLO_API_KEY:
        return {
            "email": None,
            "phone": None,
            "contact_source": "apollo_api_key_missing"
        }

    url = "https://api.apollo.io/v1/people/match"
    payload = {
        "api_key": APOLLO_API_KEY,
        "name":name,
        "organization_name": company
    }

    r = requests.post(url,json=payload)
    if r.status_code != 200:
        return {"email": None, "phone": None, "contact_source":"apollo_error"}

    person = r.json().get("person",{})
    return {
        "email":person.get("email"),
        "phone":person.get("phone_numbers",[None][0]),
        "contact_source" : "apollo"
    }

"""
> since accessing url = "https://api.apollo.io/v1/people/match" is only available in paid plan of apollo
> hence we use mock function for now
"""
import random
def enrich_contact_mock(name, company):
    domain = "gmail.com" if len(company) > 15 else f"{company.lower().replace(' ', '')}.com"
    return {
        "email": f"{name.lower().replace(' ', '.')}@{domain}",
        "phone": f"{random.randint(200,999)}-{random.randint(200,999)}-{random.randint(1000,9999)}",
        "contact_source": "mock_apollo"
    }
