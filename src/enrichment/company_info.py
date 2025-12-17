import os
import requests

CRUNCHBASE_API_KEY = os.getenv("CRUNCHBASE_API_KEY")

def enrich_company_crunchbase(company_name):
    if not CRUNCHBASE_API_KEY:
        return {
            "company_hq_city": None,
            "company_hq_country": None,
            "funding_stage": "unknown",
            "funding_source": "crunchbase_unavailable"
        }

    url = "https://api.crunchbase.com/api/v4/entities/organizations"
    params = {
        "user_key":CRUNCHBASE_API_KEY,
        "query":company_name
    }
    response = requests.get(url,json=params)

    if response.status_code != 200:
        return {
            "company_hq_city": None,
            "company_hq_country": None,
            "funding_stage": "unknown",
            "funding_source": "crunchbase_error"
        }

    data = response.json().get("entities",[])
    if not data:
        return {
            "company_hq_city": None,
            "company_hq_country": None,
            "funding_stage": "unknown",
            "funding_source": "crunchbase_not_found"
        }

    org = data[0]["properties"]

    return {
        "company_hq_city": org.get("city_name"),
        "company_hq_country": org.get("country_code"),
        "funding_stage": org.get("last_funding_type"),
        "funding_source": "crunchbase"
    }

"""
> since accessing url = "https://api.crunchbase.com/api/v4/entities/organizations" is only available in paid plan
> hence we use mock function for now
"""

def enrich_company_mock(company_name):
    mock_db = {
        # ===== BIOTECH / PHARMA =====
        "Acme Biotech": {
            "company_hq_city": "Boston",
            "company_hq_country": "USA",
            "funding_stage": "Series B"
        },
        "OncoThera": {
            "company_hq_city": "Cambridge",
            "company_hq_country": "USA",
            "funding_stage": "Series A"
        },
        "NeoLiver Therapeutics": {
            "company_hq_city": "San Francisco",
            "company_hq_country": "USA",
            "funding_stage": "Series B"
        },
        "Helix Pharma": {
            "company_hq_city": "Cambridge",
            "company_hq_country": "Switzerland",
            "funding_stage": "Public"
        },
        "TinyBio": {
            "company_hq_city": "Austin",
            "company_hq_country": "USA",
            "funding_stage": "Seed"
        },
        "Livera Biosciences": {
            "company_hq_city": "Oxford",
            "company_hq_country": "United Kingdom",
            "funding_stage": "Series A"
        },

        # ===== ACADEMIC / HOSPITAL =====
        "Guangdong Provincial Key Laboratory of Gastroenterology": {
            "company_hq_city": "Guangzhou",
            "company_hq_country": "China",
            "funding_stage": "Grant-funded"
        },
        "Tongji Hospital": {
            "company_hq_city": "Wuhan",
            "company_hq_country": "China",
            "funding_stage": "Grant-funded"
        },
        "Balikesir University": {
            "company_hq_city": "Balikesir",
            "company_hq_country": "Turkey",
            "funding_stage": "Grant-funded"
        },
        "Cleveland Clinic": {
            "company_hq_city": "Cleveland",
            "company_hq_country": "USA",
            "funding_stage": "Grant-funded"
        }
    }


    data = mock_db.get(company_name, {})

    if not data:
        return {
            "company_hq_city": None,
            "company_hq_country": None,
            "funding_stage": "unknown",
            "hq_funding_source": "mock_crunchbase_not_found"
        }

    return {
        "company_hq_city": data.get("company_hq_city"),
        "company_hq_country": data.get("company_hq_country"),
        "funding_stage": data.get("funding_stage", "unknown"),
        "hq_funding_source": "mock_crunchbase"
    }