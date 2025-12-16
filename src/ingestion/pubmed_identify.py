from Bio import Entrez
from datetime import datetime
import os

Entrez.email = os.getenv("NCBI_EMAIL", "your_email@example.com")

KEYWORDS = [
    "drug-induced liver injury",
    "liver toxicity",
    "hepatic",
    "3d cell",
    "organ-on-chip"
]

def identify_from_pubmed(max_results=50):
    year_cutoff = datetime.now().year - 2
    query = " OR ".join(KEYWORDS)

    handle = Entrez.esearch(db="pubmed",term=query, retmax=max_results)
    ids = Entrez.read(handle)["IdList"]

    candidates = []

    if not ids:
        return False

    fetch = Entrez.efetch(db="pubmed", id=",".join(ids), rettype="medline", retmode="text")
    records = fetch.read().split("\n\n")

    for record in records:
        record_lower = record.lower()
        if str(year_cutoff) not in record_lower:
            continue

        lines = record.split("\n")
        authors = [l.replace("AU  - ", "") for l in lines if l.startswith("AU  - ")]
        affiliations = [l.replace("AD  - ", "") for l in lines if l.startswith("AD  - ")]

        for author in authors:
            candidates.append({
                "name": author,
                "source": "pubmed",
                "title": None,
                "affiliation": affiliations[0] if affiliations else None,
                "domain": None,
                "linkedin_url": None,
                "location": None,
                "pubmed_id": ids,
                "conference_role": None
            })

    return candidates