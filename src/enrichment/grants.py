import requests

def check_nih_grants(name):
    url = "https://api.reporter.nih.gov/v2/projects/search"
    payload = {
        "criteria":{
            "pi_names":[name],
            "text_search":["liver toxicity","3d models"]
        },
        "limit":1
    }

    try:
        r = requests.post(url,json=payload)
        if r.status_code != 200:
            return False

        results = r.json().get("results",[])
        return len(results) > 0
    except requests.exceptions.RequestException:
        return False