from difflib import SequenceMatcher
import re

def normalize_location(text):
    if not text or not isinstance(text, str):
        return None

    # remove quotes, punctuation, extra spaces
    text = text.strip().lower()
    text = re.sub(r'[",]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text


def is_remote(person_location, company_hq_city, threshold=0.70):
    if not person_location or not company_hq_city:
        return None

    p_loc = normalize_location(person_location)
    c_loc = normalize_location(company_hq_city)

    if not p_loc or not c_loc:
        return None

    similarity = SequenceMatcher(None, p_loc, c_loc).ratio()

    # If locations are NOT similar enough → remote
    return similarity < threshold
