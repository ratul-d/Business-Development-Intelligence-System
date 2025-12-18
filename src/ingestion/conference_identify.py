"""
STUB / PLACEHOLDER MODULE

This module simulates lead identification from scientific conferences
(e.g., SOT, AACR, ASGCT, SLAS).

IMPORTANT:
- This is a hardcoded mock implementation.
- MUST be replaced later with:
    - Conference website scraper
    - PDF abstract parser
    - Attendee list ingestion
    - OR paid APIs (Ex Orbis, Clarivate, Elsevier)

Purpose:
- Allow Stage 1 pipeline to run end-to-end
- Validate merge + ranking logic
"""

def identify_from_conference(max_people=5):
    """
    Identify potential leads from conference participation.

    Future implementation ideas:
    - Scrape conference abstract books (PDF / HTML)
    - Extract authors + affiliations
    - Detect roles: Speaker, Poster Presenter, Session Chair
    - Link institution → company domain
    - Match against scientific keywords

    For now:
    - Return hardcoded mock candidates
    """

    # HARD-CODED DUMMY DATA (REPLACE WITH REAL SCRAPER)
    candidates = [
        {
            "name": "Dr. Laura McKenzie",
            "source": "conference",
            "title": "Director of Developmental Toxicology",
            "affiliation": "GSK",
            "domain": "gsk.com",
            "linkedin_url": None,
            "location": "Research Triangle Park, NC",
            "latest_experience_start_date": None,
            "pubmed_id": "PMID:37291844",
            "conference_role": "SOT 2024 Invited Speaker"
        },
        {
            "name": "Dr. Anton Petrov",
            "source": "conference",
            "title": "Head of Regulatory Toxicology",
            "affiliation": "Novartis",
            "domain": "novartis.com",
            "linkedin_url": None,
            "location": "Basel, Switzerland",
            "latest_experience_start_date": None,
            "pubmed_id": None,
            "conference_role": "EUROTOX 2023 Panelist"
        },
        {
            "name": "Dr. Melissa Grant",
            "source": "conference",
            "title": "Senior Principal Scientist, DILI",
            "affiliation": "Bristol Myers Squibb",
            "domain": "bms.com",
            "linkedin_url": None,
            "location": "New Brunswick, NJ",
            "latest_experience_start_date": None,
            "pubmed_id": "PMID:36922411",
            "conference_role": "SOT 2023 Platform Presenter"
        },
        {
            "name": "Dr. Wei Zhang",
            "source": "conference",
            "title": "Director, Translational Safety Sciences",
            "affiliation": "AstraZeneca",
            "domain": "astrazeneca.com",
            "linkedin_url": None,
            "location": "Cambridge, United Kingdom",
            "latest_experience_start_date": None,
            "pubmed_id": None,
            "conference_role": "AACR 2024 Workshop Leader"
        },
        {
            "name": "Dr. Carlos Mendes",
            "source": "conference",
            "title": "Head of Nonclinical Risk Assessment",
            "affiliation": "Sanofi",
            "domain": "sanofi.com",
            "linkedin_url": None,
            "location": "Paris, France",
            "latest_experience_start_date": None,
            "pubmed_id": "PMID:36155409",
            "conference_role": "SOT 2024 Poster Judge"
        },
        {
            "name": "Dr. Nina Rasmussen",
            "source": "conference",
            "title": "Principal Scientist, Systems Toxicology",
            "affiliation": "Novo Nordisk",
            "domain": "novonordisk.com",
            "linkedin_url": None,
            "location": "Copenhagen, Denmark",
            "latest_experience_start_date": None,
            "pubmed_id": None,
            "conference_role": "EUROTOX 2024 Speaker"
        },
        {
            "name": "Dr. Paul Richardson",
            "source": "conference",
            "title": "Director of Reproductive Toxicology",
            "affiliation": "Eli Lilly",
            "domain": "lilly.com",
            "linkedin_url": None,
            "location": "Indianapolis, IN",
            "latest_experience_start_date": None,
            "pubmed_id": "PMID:35890217",
            "conference_role": "SOT 2023 Symposium Organizer"
        },
        {
            "name": "Dr. Yuki Matsumoto",
            "source": "conference",
            "title": "Group Leader, Preclinical Safety",
            "affiliation": "Takeda",
            "domain": "takeda.com",
            "linkedin_url": None,
            "location": "Osaka, Japan",
            "latest_experience_start_date": None,
            "pubmed_id": None,
            "conference_role": "JST 2024 Oral Presenter"
        },
        {
            "name": "Dr. Hannah Cooper",
            "source": "conference",
            "title": "Scientific Director, Safety Biomarkers",
            "affiliation": "Regeneron",
            "domain": "regeneron.com",
            "linkedin_url": None,
            "location": "Tarrytown, NY",
            "latest_experience_start_date": None,
            "pubmed_id": "PMID:36577102",
            "conference_role": "AACR 2023 Moderator"
        },
        {
            "name": "Dr. Omar El-Sayed",
            "source": "conference",
            "title": "Director of Predictive Toxicology",
            "affiliation": "Merck KGaA",
            "domain": "merckgroup.com",
            "linkedin_url": None,
            "location": "Darmstadt, Germany",
            "latest_experience_start_date": None,
            "pubmed_id": None,
            "conference_role": "EUROTOX 2023 Keynote Speaker"
        }
    ]

    return candidates[:max_people]
