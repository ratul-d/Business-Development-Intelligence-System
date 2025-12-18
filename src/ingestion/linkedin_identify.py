import pandas as pd

def identify_from_linkedin(csv_path="src/data/input/clay_leads.csv", max_people=10):
    """
    Clay-exported LinkedIn search results
    """
    df = pd.read_csv(csv_path)
    df = df.head(max_people)

    candidates = []
    for _, row in df.iterrows():
        candidates.append({
            "name": row.get("name"),
            "source": "linkedin",
            "title": row.get("latest_experience_title"),
            "affiliation": row.get("latest_experience_company"),
            "domain": row.get("domain"),
            "linkedin_url": row.get("url"),
            "location": row.get("location_name"),
            "latest_experience_start_date": row.get("latest_experience_start_date"),
            "pubmed_id": None,
            "conference_role": None
        })

    return candidates
