import streamlit as st
import pandas as pd
import subprocess
import sys

st.set_page_config(page_title="Business Development Intelligence Dashboard", layout="wide")
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("3D In-Vitro Models - Lead Generation Dashboard")
st.caption("Ranked scientists & decision-makers by propensity to collaborate")
st.divider()

st.markdown("### Pipeline Controls")

with st.expander("Data Pipeline Controls", expanded=False):
    left, _ = st.columns([1, 1])

    with left:
        pubmed_col, conf_col = st.columns(2)

        with pubmed_col:
            max_pubmed_leads = st.number_input(
                label="Maximum PubMed candidates to fetch",
                min_value=1,
                max_value=50,
                value=10,
                step=5,
                help="Upper limit on PubMed candidates (not guaranteed)."
            )

        with conf_col:
            max_conference_leads = st.number_input(
                label="Maximum Conference candidates to fetch",
                min_value=1,
                max_value=50,
                value=10,
                step=5,
                help="Upper limit on conference leads (not guaranteed)."
            )

    run_col1, run_col2 = st.columns(2)

    with run_col1:
        if st.button("Run Pipeline (Dummy Mode - No Paid APIs)", use_container_width=True):
            with st.spinner("Running pipeline in dummy mode..."):
                result = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "src.pipeline_run_all",
                        "--mode",
                        "dummy",
                        "--max-pubmed-leads",
                        str(max_pubmed_leads),
                        "--max-conference-leads",
                        str(max_conference_leads),
                    ],
                    capture_output=True,
                    text=True
                )

            if result.returncode == 0:
                st.success("Pipeline completed successfully.")
                st.cache_data.clear()
                st.rerun()
            else:
                st.error("Pipeline failed.")
                st.code(result.stderr)

DATA_PATH="src/data/output/stage3_ranked_leads.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

df["Rank"] = df.index+1
df["Probability"] = df["propensity_score"].astype(int)
df["Title"] = df["raw_titles"]
df["Company"] = df["raw_affiliations"]
df["Location"] = df.apply(
    lambda r: f"({r['person_location']})"
    if r.get("is_remote") is True
    else r.get("person_location"),
    axis=1
)
df["HQ"] = df["company_hq_city"]
df["Action"] = df["email"].apply(
    lambda x: "Email" if pd.notna(x) else "Research"
)

# Search + Probability Filter (Side by Side)
st.markdown("### Filters")

with st.container():
    f1, f2 = st.columns([2, 1])

    with f1:
        search_query = st.text_input(
            "Search across name, location, domain, company",
            placeholder="e.g. Boston, Oncology, Toxicology"
        )

    with f2:
        min_prob, max_prob = st.slider(
            "Propensity score",
            0, 100, (0, 100), step=5
        )

# Apply filters
if search_query:
    df = df[df.apply(
        lambda row: search_query.lower() in row.to_string().lower(),
        axis=1
    )]

df = df[(df["Probability"] >= min_prob) & (df["Probability"] <= max_prob)]


# Display
st.subheader("Ranked Leads")

display_cols = [
    "Rank",
    "Probability",
    "name",
    "Title",
    "Company",
    "Location",
    "HQ",
    "email",
    "linkedin_url",
    "Action"
]

st.dataframe(
    df[display_cols],
    use_container_width=True,
    hide_index=True,
    height=550
)

# Export
export_df = df[display_cols].copy()
col1, col2 = st.columns(2)
with col1:
    st.download_button(
        "Download CSV",
        df[display_cols].to_csv(index=False),
        "ranked_leads.csv",
        "text/csv"
    )
st.divider()
# Summary
st.subheader("Summary based on Propensity Score")

hot = df[df["Probability"] >= 80].shape[0]
warm = df[(df["Probability"] >= 50) & (df["Probability"] < 80)].shape[0]
cold = df[df["Probability"] < 50].shape[0]

# Subtle translucent styles
st.markdown("""
<style>
.card {
    padding: 18px;
    border-radius: 10px;
    border-left: 6px solid;
    background-color: rgba(0,0,0,0.02);
}
.high { border-color: #2ecc71; }
.medium { border-color: #f1c40f; }
.low { border-color: #e74c3c; }
</style>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"<div class='card high'>High Priority (80+)<br><h2>{hot}</h2></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='card medium'>Medium Priority (50-79)<br><h2>{warm}</h2></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='card low'>Low Priority (<50)<br><h2>{cold}</h2></div>", unsafe_allow_html=True)

