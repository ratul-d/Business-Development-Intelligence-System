from src_demo.integrations.apollo import enrich_email, dummy_enrich_email
from src_demo.integrations.pubmed import has_recent_relevant_publication
import yaml

keywords = yaml.safe_load(open("src_demo/config/keywords.yaml"))

def enrich(row):
    email = dummy_enrich_email(row["name"], row["company"])

    scientific_intent = has_recent_relevant_publication(
        row["name"],
        keywords["scientific_keywords"])

    return {
        **row,
        "email":email,
        "scientific_intent":scientific_intent
    }