import streamlit as st
import pandas as pd

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

left_col, right_col = st.columns(2)

with left_col:
    search_query = st.text_input(
        "Search (e.g. Boston, Oncology, Toxicology, Company name)",
        ""
    )

with right_col:
    min_prob, max_prob = st.slider(
        "Propensity score range",
        min_value=0,
        max_value=100,
        value=(0, 100),
        step=5
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
st.subheader("Export")
export_df = df[display_cols].copy()
col1, col2 = st.columns(2)
with col1:
    st.download_button(
        "Download CSV",
        df[display_cols].to_csv(index=False),
        "ranked_leads.csv",
        "text/csv"
    )

# Summary
st.subheader("Summary")
hot = df[df["Probability"] >= 80].shape[0]
warm = df[(df["Probability"] >= 50) & (df["Probability"] < 80)].shape[0]
cold = df[df["Probability"] < 50].shape[0]

m1, m2, m3 = st.columns(3)
m1.metric("High Priority (80+)", hot)
m2.metric("Medium Priority (50-79)", warm)
m3.metric("Low Priority (<50)", cold)