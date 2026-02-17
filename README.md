# Meeting Diarrhea Detector

Ever feel like your calendar has completely taken over your life? This tool analyzes your meeting data and tells you exactly how bad it is — then roasts you about it.

## What it does

Upload a CSV of your meetings and get back:
- A **productivity score** out of 100
- Detection of **overloaded days** (4+ meetings)
- Count of meetings that **could've been emails**
- A **daily breakdown** of your calendar chaos
- A personalized **roast** based on your results

## Tech stack

- Python + Flask (web framework)
- Pandas (data analysis)
- HTML/CSS (frontend dashboard)

## How to run it

1. Clone the repo
```
   git clone https://github.com/preiyalthakkar3007/meeting-diarrhea-detector.git
   cd meeting-diarrhea-detector
```

2. Create a virtual environment and install dependencies
```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
```

3. Run the app
```
   python app.py
```

4. Open your browser and go to `http://127.0.0.1:5000`

## CSV format

Your CSV file should have these columns:

| Column | Description | Values |
|---|---|---|
| date | Meeting date | YYYY-MM-DD |
| title | Meeting name | Any text |
| duration_minutes | Length in minutes | Number |
| attendees | Number of attendees | Number |
| has_agenda | Whether it had an agenda | yes / no |
| could_be_email | Could it have been an email? | yes / no |

A sample file is included in `sample_data/meetings.csv` to get you started.

## Sample output

- 16 meetings analyzed across 5 days
- 15 hours of meeting time detected
- 5 meetings flagged as unnecessary
- Productivity score: 52/100
- Verdict: *"Yikes. 2 overloaded days detected. Have you considered just... not attending?"*