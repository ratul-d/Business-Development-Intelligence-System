def summarize_scientific_activity(pubmed_ids):
    return {
        "recent_publications": len(pubmed_ids),
        "active_researcher": len(pubmed_ids) > 0
    }
