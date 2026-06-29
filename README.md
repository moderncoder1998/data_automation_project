# RemoteOK Job Scraper

A Python-based job scraping project that fetches remote job listings from the RemoteOK API, cleans and filters the data, and exports the results as a CSV file.

## Features

- Fetches live job data from the RemoteOK API
- Filters jobs based on a keyword
- Cleans and validates the data
- Removes duplicate records
- Converts salary fields to numeric values
- Generates execution logs
- Creates a validation report
- Exports cleaned data to CSV

## Project Structure

```
jobscraper/
│
├── main.py
├── scraper.py
├── data_cleaner.py
├── logger.py
├── requirements.txt
├── README.md
│
└── output/
    ├── jobs_clean.csv
    ├── validation_report.csv
    └── execution_log.txt
```

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Move into the project folder:

```bash
cd jobscraper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application with a keyword.

Example:

```bash
python main.py python
```

or

```bash
python main.py data
```

## Output

The project generates:

- Cleaned job data (CSV)
- Validation report (CSV)
- Execution log

All files are stored inside the `output/` folder.

## Technologies Used

- Python
- Requests
- Pandas
- Logging
- REST API
- CSV

## Future Improvements

- Export reports to Excel
- Interactive dashboard
- SQL validation
- API retry mechanism
- Unit testing