import pandas as pd
from src.ingestion.linkedin_identify import identify_from_linkedin
from src.ingestion.pubmed_identify import identify_from_pubmed
from src.ingestion.merge_candidates import merge_candidates
from src.ingestion.conference_identify import identify_from_conference

def run_stage1(max_linkedin_leads,max_pubmed_leads,max_conference_leads):
    linkedin = identify_from_linkedin(max_people=max_linkedin_leads)
    pubmed = identify_from_pubmed(max_people=max_pubmed_leads)
    conference = identify_from_conference(max_people=max_conference_leads)

    allcandidates = linkedin + pubmed + conference
    merged = merge_candidates(allcandidates)


    rows=[]
    for c in merged.values():
        rows.append({
            "name": c["name"],
            "sources": ",".join(c["sources"]),
            "raw_titles": "; ".join(c["raw_titles"]),
            "raw_affiliations": "; ".join(c["raw_affiliations"]),
            "domains": "; ".join(c["domains"]),
            "person_location": "; ".join(c["person_location"]),
            "linkedin_url": c["linkedin_url"],
            "latest_experience_start_date": c["latest_experience_start_date"],
            "pubmed_ids": "; ".join(c["pubmed_ids"]),
            "conference_roles": "; ".join(c["conference_roles"]),
            "evidence_count": len(c["sources"])
        })

    df = pd.DataFrame(rows)
    df.to_csv("src/data/output/stage1_candidates.csv",index=False)
    print("Stage 1 Complete.")

if __name__ == "__main__":
    run_stage1(10,5,5)