import pandas as pd
from src.scoring.scorer import score_lead

def run_stage3():
    df = pd.read_csv("src/data/stage2_enriched.csv")

    scored_rows = []

    for _,row in df.iterrows():
        score, breakdown = score_lead(row)

        scored_rows.append({
            **row,
            "propensity_score":score,
            "breakdown":breakdown
        })

    out = pd.DataFrame(scored_rows)
    out = out.sort_values("propensity_score", ascending=False)
    out.to_csv("src/data/stage3_ranked_leads.csv", index=False)

    print("Stage 3 Complete.")

if __name__ == "__main__":
    run_stage3()