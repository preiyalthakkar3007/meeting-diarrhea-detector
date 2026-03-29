# 🚽 Meeting Diarrhea Detector

> *"You don't have a productivity problem. You have a calendar problem."*

[![Live Demo](https://img.shields.io/badge/🔴_LIVE_DEMO-meeting--diarrhea--detector.onrender.com-red?style=for-the-badge)](https://meeting-diarrhea-detector.onrender.com)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?style=flat-square&logo=flask)
![Pandas](https://img.shields.io/badge/Pandas-2.x-purple?style=flat-square&logo=pandas)

---

## The Problem

You wake up. Check your calendar. 6 meetings before lunch.  
Three of them have no agenda. Two of them could've been a Slack message.  
One of them is a meeting *to plan another meeting*.

**This tool diagnoses your calendar disease — and roasts you for it.**

---

## What You Get

| Feature | What It Does |
|--------|--------------|
| 📊 **Productivity Score** | Rates your calendar health 0–100 (spoiler: it's bad) |
| 🔥 **Overload Detector** | Flags days where meetings ate your soul (4+) |
| 📧 **Could've Been an Email** | Counts the meetings that had no business existing |
| 📅 **Daily Breakdown** | A table of your suffering, day by day |
| 🎤 **Personalized Roast** | Brutally honest feedback based on your results |

---

## How It Works
```
Upload CSV → Analyze → Get Roasted
```

1. Export or create a CSV of your meetings
2. Upload it to the app
3. Receive your productivity score + a roast you probably deserve

---

## CSV Format
```csv
date,title,duration_minutes,attendees,has_agenda,could_be_email
2024-01-15,Sprint Planning,60,8,yes,no
2024-01-15,Sync Sync Sync,30,4,no,yes
```

| Column | Type | Description |
|--------|------|-------------|
| `date` | YYYY-MM-DD | When the meeting happened |
| `title` | text | What they called it |
| `duration_minutes` | number | How long it stole from you |
| `attendees` | number | How many people suffered |
| `has_agenda` | yes/no | Did anyone prepare? |
| `could_be_email` | yes/no | The real question |

> 📁 A sample file is included at `sample_data/meetings.csv`

---

## Sample Output
```
📊 Productivity Score: 52/100
📅 Meetings analyzed: 16 across 5 days  
⏱️  Total meeting time: 15 hours
🚨 Overloaded days: 2
📧 Unnecessary meetings: 5

🎤 Roast: "Yikes. 2 overloaded days detected.
           Have you considered just... not attending?"
```

---

## Run Locally
```bash
git clone https://github.com/preiyalthakkar3007/meeting-diarrhea-detector.git
cd meeting-diarrhea-detector
pip install -r requirements.txt
python app.py
# Open http://127.0.0.1:5000
```

---

## Tech Stack

- **Backend:** Python + Flask
- **Data Analysis:** Pandas
- **Frontend:** HTML/CSS (Jinja2 templates)
- **Deployment:** Render

---

*Built because someone had 8 meetings in one day and needed to cope.*
