from difflib import SequenceMatcher

def similar(a,b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def clean_str(x):
    if isinstance(x, str) and x.strip():
        return x.strip()
    return None


def merge_candidates(all_candidates):
    merged={}

    for c in all_candidates:
        name = c["name"]

        matched_key = None
        for existing in merged:
            if similar(existing,name) > 0.85:
                matched_key = existing
                break

        key = matched_key if matched_key else name

        if key not in merged:
            merged[key] = {
                "name": name,
                "sources": set(),
                "raw_titles": set(),
                "raw_affiliations": set(),
                "domains": set(),
                "locations": set(),
                "linkedin_url": None,
                "latest_experience_start_date": None,
                "pubmed_ids": set(),
                "conference_roles": set()
            }

        entry = merged[key]

        if c.get("source"):
            entry["sources"].add(c["source"])

        if c.get("title"):
            entry["raw_titles"].add(c["title"])

        affiliation = clean_str(c.get("affiliation"))
        if affiliation:
            entry["raw_affiliations"].add(affiliation)

        domain = clean_str(c.get("domain"))
        if domain:
            entry["domains"].add(domain)

        loc = clean_str(c.get("location"))
        if loc:
            entry["locations"].add(loc)

        if c.get("linkedin_url") and not entry["linkedin_url"]:
            entry["linkedin_url"] = c["linkedin_url"]

        start_date = clean_str(c.get("latest_experience_start_date"))
        if start_date:
            if not entry["latest_experience_start_date"]:
                entry["latest_experience_start_date"] = start_date
            else:
                entry["latest_experience_start_date"] = min(
                    entry["latest_experience_start_date"], start_date
                )

        if c.get("pubmed_id"):
            if isinstance(c["pubmed_id"], (list, set)):
                entry["pubmed_ids"].update(c["pubmed_id"])
            else:
                entry["pubmed_ids"].add(c["pubmed_id"])

        if c.get("conference_role"):
            entry["conference_roles"].add(c["conference_role"])

    return merged