# app.py

from flask import Flask, request, render_template, redirect, url_for, session
import pandas as pd
import os
from services.search_service import search_entity
from services.llm_service import extract_info
from services.gsheet_service import load_google_sheet

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Route to the main page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if Google Sheets link is provided
        sheet_id = request.form.get("sheet_id")
        if sheet_id:
            # Load data from Google Sheets
            df = load_google_sheet(sheet_id)
            session['source'] = 'google_sheets'
            session['sheet_id'] = sheet_id
            return render_template("index.html", columns=list(df.columns), data_preview=df.head().to_html())

        # Otherwise, handle file upload
        file = request.files.get("file")
        if file and file.filename.endswith('.csv'):
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            session['source'] = 'csv'
            session['file_path'] = file_path
            df = pd.read_csv(file_path)
            return render_template("index.html", columns=list(df.columns), data_preview=df.head().to_html())

    return render_template("index.html")

# Route to process the data
@app.route("/process", methods=["POST"])
def process():
    column = request.form.get("column")
    prompt_template = request.form.get("prompt_template")
    
    source = session.get('source')
    if source == 'google_sheets':
        sheet_id = session.get('sheet_id')
        df = load_google_sheet(sheet_id)
    elif source == 'csv':
        file_path = session.get('file_path')
        df = pd.read_csv(file_path)
    else:
        return redirect(url_for("index"))

    # Process data if loaded
    if df is not None and column in df.columns:
        try:
            results = []
            for entity in df[column]:
                prompt = prompt_template.format(entity=entity)
                search_results = search_entity(prompt)
                extracted_info = extract_info(search_results, entity)
                results.append(extracted_info)
            
            # Add extracted info to the DataFrame and display it
            df["Extracted Info"] = results
            return render_template("index.html", columns=list(df.columns), data_preview=df.to_html())

        except Exception as e:
            return f"Error processing data: {e}"
    else:
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)