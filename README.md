# DataSense - AI Information Extractor

DataSense is a powerful web-based tool designed to extract specific information for entities listed in datasets, such as companies or organizations, using advanced web searches and a Large Language Model (LLM). The application enables users to upload data via CSV files or connect directly to Google Sheets. This extracted information can be viewed, analyzed, and downloaded, all through a clean and user-friendly Flask web interface.

---

## Key Features

- **Seamless Data Upload**: Upload CSV files or connect directly to Google Sheets to input your data.
- **Custom Prompts**: Define unique prompts for the type of information you'd like to extract for each entity.
- **Automated Web Search**: Uses SerpAPI to gather web search results for each entity based on the custom prompts.
- **Intelligent Data Extraction**: Leverages OpenAI’s LLM to parse search results and extract requested information (e.g., emails, addresses).
- **Interactive Dashboard**: View extracted information in a table format, with options to download or update the connected Google Sheet.

---

## Prerequisites

- **Python 3.7+**
- **Flask**: For the web application
- **Google Sheets API**: For connecting to Google Sheets
- **SerpAPI**: For web searches
- **OpenAI API**: For information extraction

---

## Screenshots

### Main Dashboard
![DataSense Main Dashboard](https://github.com/user-attachments/assets/124b90cf-f4c8-49c7-a67c-3da3868f11bc)

### Data Extraction in Action
![Data Extraction in Action](https://github.com/user-attachments/assets/67504d24-8490-434e-98a4-4f91651d9a5d)

---

## Setup and Installation

### Steps

2. **Set Up a Virtual Environment**

   Create a virtual environment for the project and activate it. On Windows, use the command `venv\Scripts\activate`.

3. **Install Requirements**

   Install all necessary packages listed in `requirements.txt` to set up the project dependencies.

4. **Configure Environment Variables**

   Create a `.env` file in the project root and add your API keys:
   - `GOOGLE_SHEETS_API_KEY`: Your Google Sheets API Key
   - `SERPAPI_KEY`: Your SerpAPI Key
   - `OPENAI_API_KEY`: Your OpenAI API Key

5. **Run the Flask Application**

   Run the application using Flask. The app will be accessible at `http://127.0.0.1:5000`.

---

## Usage Guide

1. **Upload Data**:
   - **CSV**: Upload a CSV file containing a column with entity names (e.g., company names).
   - **Google Sheets**: Connect to a Google Sheet by entering the Sheet ID.

2. **Set Custom Prompt**:
   - Define a prompt template, such as: `Find the contact email and address for {entity}`.

3. **Extract Information**:
   - For each entity, DataSense performs a web search and uses the LLM to extract the specified information.

4. **View and Download Results**:
   - View the extracted data in a table and download it as a CSV or update the original Google Sheet.

---

## Third-Party APIs and Tools Used

1. **OpenAI API**
   - **Purpose**: Uses GPT models to parse search results and extract specific information based on the user-defined prompt.
   - **Usage**: Requires an API key, which can be set in the `.env` file under `OPENAI_API_KEY`.

2. **SerpAPI**
   - **Purpose**: Conducts automated web searches based on the specified prompt and entity name.
   - **Usage**: Requires an API key, which can be set in the `.env` file under `SERPAPI_KEY`.

3. **Google Sheets API**
   - **Purpose**: Connects directly to Google Sheets to pull data for extraction and update results back into the sheet.
   - **Usage**: Requires a Google Sheets API key, which can be set in the `.env` file under `GOOGLE_SHEETS_API_KEY`.

4. **Flask**
   - **Purpose**: Provides the web framework for the application, serving the dashboard and handling user interactions.

---

## Dependencies

- **Flask**: Web framework to create the dashboard interface.
- **pandas**: For handling CSV data.
- **gspread and oauth2client**: For Google Sheets integration.
- **requests**: For making HTTP requests to APIs.
- **python-dotenv**: For managing environment variables securely.
- **OpenAI API**: To interact with the LLM for data extraction.
- **SerpAPI**: For fetching web search results.

---

## Future Improvements

- **Enhanced Error Handling**: Notify users of specific issues (e.g., invalid API keys, missing columns).
- **Advanced Querying**: Support complex multi-field extraction queries (e.g., emails, addresses, phone numbers in a single prompt).
- **Export to Additional Formats**: Provide options to export to Google Sheets, Excel, and JSON.
