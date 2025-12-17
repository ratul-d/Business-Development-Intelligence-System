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

def enrich_contact_mock(name, company):
    email = f"{name.lower().replace(' ','.')}@{company.lower().replace(' ','')}.com"
    return {
        "email": email,
        "phone": None,
        "contact_source": "mock_apollo"
    }
