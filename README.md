# DataSense - AI Information Extractor

DataSense is a powerful web-based tool designed to extract specific information for entities listed in datasets, such as companies or organizations, using advanced web searches and an LLM (Large Language Model). The application enables users to upload data via CSV files or connect directly to Google Sheets. This extracted information can be viewed, analyzed, and downloaded, all through a clean and user-friendly Flask web interface.

---

## Key Features

- **Seamless Data Upload**: Upload CSV files or connect directly to Google Sheets to input your data.
- **Custom Prompts**: Define unique prompts for the type of information you'd like to extract for each entity.
- **Automated Web Search**: Uses SerpAPI to gather web search results for each entity based on the custom prompts.
- **Intelligent Data Extraction**: Leverages OpenAI’s LLM to parse search results and extract requested information (e.g., emails, addresses).
- **Interactive Dashboard**: View extracted information in a table format, with options to download or update the connected Google Sheet.

---

## Screenshots

### Main Dashboard
![DataSense Main Dashboard](https://github.com/user-attachments/assets/124b90cf-f4c8-49c7-a67c-3da3868f11bc)

### Data Extraction in Action
![Data Extraction in Action](https://github.com/user-attachments/assets/67504d24-8490-434e-98a4-4f91651d9a5d)

---

## Project Structure

```plaintext
DataSense/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # HTML template for the dashboard
├── static/
│   └── css/
│       └── style.css      # CSS styling
├── services/
│   ├── gsheet_service.py  # Google Sheets integration
│   ├── llm_service.py     # LLM integration (OpenAI)
│   └── search_service.py  # Web search integration (SerpAPI)
├── .env                   # Environment variables (API keys, etc.)
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
