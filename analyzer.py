import pandas as pd

def load_meetings(filepath):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    return df

def analyze_meetings(df):
    results = {}

    # Total stats
    results['total_meetings'] = len(df)
    results['total_hours'] = round(df['duration_minutes'].sum() / 60, 1)
    results['could_be_email'] = int(df['could_be_email'].str.strip().eq('yes').sum())
    results['no_agenda'] = int(df['has_agenda'].str.strip().eq('no').sum())

    # Per day analysis
    daily = df.groupby('date').agg(
        meeting_count=('title', 'count'),
        total_minutes=('duration_minutes', 'sum')
    ).reset_index()

    daily['total_hours'] = round(daily['total_minutes'] / 60, 1)
    daily['overloaded'] = daily['meeting_count'] >= 4

    results['daily'] = daily.to_dict(orient='records')
    results['overloaded_days'] = int(daily['overloaded'].sum())

    # Productivity score (0-100, higher is better)
    email_penalty = (results['could_be_email'] / results['total_meetings']) * 40
    agenda_penalty = (results['no_agenda'] / results['total_meetings']) * 30
    overload_penalty = min(results['overloaded_days'] * 10, 30)

    results['productivity_score'] = max(0, round(100 - email_penalty - agenda_penalty - overload_penalty))

    return results

def get_roast(results):
    score = results['productivity_score']
    overloaded = results['overloaded_days']
    could_be_email = results['could_be_email']
    total = results['total_meetings']

    if score >= 80:
        return "Not bad! Your calendar is actually under control. Are you even trying to look busy?"
    elif score >= 60:
        return f"You have {could_be_email} meetings that could've been emails. Your inbox is lonely."
    elif score >= 40:
        return f"Yikes. {overloaded} overloaded days detected. Have you considered just... not attending?"
    elif score >= 20:
        return f"You spent time in {total} meetings. At this point, just move into the conference room."
    else:
        return "Your calendar is a crime scene. Please seek help immediately. We're serious."