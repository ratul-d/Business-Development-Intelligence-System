from Bio import Entrez
from datetime import datetime
import os

Entrez.email = os.getenv("NCBI_EMAIL", "your_email@example.com")

def has_recent_relevant_publication(author_name, keywords, years=2):

    #search by name
    query = f"{author_name}[Author]"
    handle = Entrez.esearch(db="pubmed", term=query, retmax=5)
    ids = Entrez.read(handle)["IdList"]

    if not ids:
        return False

    #get actual records of each id
    handle  = Entrez.efetch(db="pubmed", id=",".join(ids), rettype="medline")
    records = handle.read().lower()

    recent_year = str(datetime.now().year-years)

    # check if its in recent years and
    # has any of our scientific_keywords
    for k in keywords:
        if k in records and recent_year in records:
            return True

    return False