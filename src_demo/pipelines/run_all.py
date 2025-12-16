import pandas as pd
from src_demo.ingestion.identify import identify
from src_demo.enrichment.enrich import enrich
from src_demo.scoring.scorer import score

def run():
    df = identify()

    enriched_rows=[]
    for _,row in df.iterrows():
        enriched = enrich(row)
        s, breakdown = score(enriched)
        enriched["score"] = s
        enriched["score_breakdown"] = breakdown
        enriched_rows.append(enriched)

    out = pd.DataFrame(enriched_rows)
    out = out.sort_values("score", ascending=False)
    out.to_csv("src_demo/data/output/leads_scored.csv", index=False)
    print("Leads scored and exported.")

if __name__ == "__main__":
    run()