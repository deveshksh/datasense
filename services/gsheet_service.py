# services/gsheet_service.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os

# Load credentials and connect to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

def load_google_sheet(sheet_id):
    """
    Load data from Google Sheets by sheet ID.
    """
    try:
        sheet = client.open_by_key(sheet_id).sheet1  # Open the first sheet
        data = sheet.get_all_records()  # Get all records as a list of dictionaries
        df = pd.DataFrame(data)  # Convert to DataFrame
        return df
    except Exception as e:
        print(f"Error loading Google Sheet: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error