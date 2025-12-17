import pandas as pd
from src.enrichment.person_contact import enrich_contact_mock, enrich_contact_apollo
from src.enrichment.company_info import enrich_company_mock, enrich_company_crunchbase
from src.enrichment.is_remote import is_remote
from src.enrichment.grants import check_nih_grants
from src.enrichment.scientific_profile import summarize_scientific_activity
from src.enrichment.tenure import estimate_tenure

def run_stage2():
    df = pd.read_csv("src/data/stage1_candidates.csv")
    enirched_rows=[]

    for _,row in df.iterrows():
        name = row["name"]
        company = row["raw_affiliations"]

        if row["sources"] == "pubmed":
            contact = {
                "email": None,
                "phone": None,
                "contact_source": "academic_no_email"
            }
        else:
            contact = enrich_contact_mock(row["name"], row["raw_affiliations"])

        company_data = enrich_company_mock(company)
        remote_flag = is_remote(
            str(row["person_location"]),
            str(company_data.get("company_hq_city"))
        )
        tenure = estimate_tenure(str(row["latest_experience_start_date"]))

        has_grant = check_nih_grants(name)

        pubmed_ids = (
            str(row["pubmed_ids"]).split("; ")
            if pd.notna(row.get("pubmed_ids"))
            else []
        )
        science = summarize_scientific_activity(pubmed_ids)

        enirched_rows.append({
            **row,
            **contact,
            **company_data,
            **tenure,
            **science,
            "is_remote":remote_flag,
            "has_nih_grant": has_grant

        })

    out = pd.DataFrame(enirched_rows)
    out.to_csv("src/data/stage2_enriched.csv",index=False)
    print("Stage 2 Complete.")

if __name__ == "__main__":
    run_stage2()