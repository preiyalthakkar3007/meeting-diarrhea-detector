from flask import Flask, render_template, request
import os
from analyzer import load_meetings, analyze_meetings, get_roast

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return render_template('index.html', error='No file uploaded')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No file selected')

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    df = load_meetings(filepath)
    results = analyze_meetings(df)
    roast = get_roast(results)

    return render_template('results.html', results=results, roast=roast)

if __name__ == '__main__':
    app.run(debug=True)