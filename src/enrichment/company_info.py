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
        # ===== BIOTECH / PHARMA (LINKEDIN SOURCED) =====

        "NovaCura Biosciences": {
            "company_hq_city": "San Diego",
            "company_hq_country": "USA",
            "funding_stage": "Series B"
        },

        "Aurora Therapeutics": {
            "company_hq_city": "San Jose",
            "company_hq_country": "USA",
            "funding_stage": "Series A"
        },

        "Valence Pharma": {
            "company_hq_city": "Basel",
            "company_hq_country": "Switzerland",
            "funding_stage": "Private"
        },

        "HepatoGenix": {
            "company_hq_city": "South San Francisco",
            "company_hq_country": "USA",
            "funding_stage": "Series B"
        },

        "Alpine BioLabs": {
            "company_hq_city": "Munich",
            "company_hq_country": "Germany",
            "funding_stage": "Series A"
        },

        "NeuroAxis Therapeutics": {
            "company_hq_city": "Bangalore",
            "company_hq_country": "India",
            "funding_stage": "Seed"
        },

        "Orionis Pharma": {
            "company_hq_city": "Princeton",
            "company_hq_country": "USA",
            "funding_stage": "Public"
        },

        "Redwood Biotech": {
            "company_hq_city": "Redwood City",
            "company_hq_country": "USA",
            "funding_stage": "Series C"
        },

        "Sakura Therapeutics": {
            "company_hq_city": "Tokyo",
            "company_hq_country": "Japan",
            "funding_stage": "Private"
        },

        "BrightPath Pharma": {
            "company_hq_city": "Dublin",
            "company_hq_country": "Ireland",
            "funding_stage": "Series B"
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