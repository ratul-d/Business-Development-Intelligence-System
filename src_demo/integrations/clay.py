import pandas as pd

def load_clay_csv(path="src_demo/data/input/clay_leads.csv"):
    """
    Clay export should include:
    name, title, company, linkedin_url, person_location, company_hq, funding_stage
    """
    return pd.read_csv(path)