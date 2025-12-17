from datetime import datetime

def estimate_tenure(latest_experience_start_date):
    if not latest_experience_start_date:
        return {
            "tenure_years": None,
            "tenure_bucket": "unknown"
        }

    try:
        start_date = datetime.strptime(latest_experience_start_date, "%Y-%m-%d")
        today = datetime.today()
        tenure_years = round((today - start_date).days / 365, 1)
        new_hire = False
        if tenure_years < 2.5:
            new_hire = True

        return {
            "tenure_years": tenure_years,
            "new_hire": new_hire
        }

    except ValueError:
        return {
            "tenure_years": None,
            "new_hire": "unknown"
        }