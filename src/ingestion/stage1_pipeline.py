import pandas as pd
from src.ingestion.linkedin_identify import identify_from_linkedin
from src.ingestion.pubmed_identify import identify_from_pubmed
from src.ingestion.merge_candidates import merge_candidates

def run_stage1():
    linkedin = identify_from_linkedin()
    pubmed = identify_from_pubmed()

    allcandidates = linkedin + pubmed
    merged = merge_candidates(allcandidates)


    rows=[]
    for c in merged.values():
        rows.append({
            "name": c["name"],
            "sources": ",".join(c["sources"]),
            "raw_titles": "; ".join(c["raw_titles"]),
            "raw_affiliations": "; ".join(c["raw_affiliations"]),
            "domains": "; ".join(c["domains"]),
            "locations": "; ".join(c["locations"]),
            "linkedin_url": c["linkedin_url"],
            "pubmed_ids": "; ".join(c["pubmed_ids"]),
            "conference_roles": "; ".join(c["conference_roles"]),
            "evidence_count": len(c["sources"])
        })

    df = pd.DataFrame(rows)
    df.to_csv("src/data/stage1_candidates.csv",index=False)
    print("Stage 1 Complete.")

if __name__ == "__main__":
    run_stage1()