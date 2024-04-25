# Web Scraping COVID-19 Data Using APIs

## Overview
This project demonstrates how to retrieve COVID-19 data for the state of Washington using web scraping techniques and APIs. The script extracts data from the [COVID Tracking Project API](https://covidtracking.com/data/api) and stores it in a CSV file for further analysis.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Data Description](#data-description)
- [License](#license)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/web-scraping-covid-data.git
    ```

2. Install the required dependencies:
    ```bash
    pip install requests pandas
    ```

## Usage
1. Run the script `scrape_covid_data.py`:
    ```bash
    python scrape_covid_data.py
    ```
    This script will retrieve COVID-19 data for the state of Washington and store it in a CSV file named `washington_covid.csv`.

2. Analyze the data using tools like pandas or visualize it using libraries like matplotlib or seaborn.

## Data Description
The data stored in the CSV file includes the following columns:
- `name_of_state`: Name of the state (in this case, "Washington").
- `date`: Date of the data in YYYYMMDD format.
- `total_cases`: Total number of COVID-19 cases reported.
- `confirmed_cases`: Number of confirmed COVID-19 cases.

## License
This project is licensed under the [MIT License](LICENSE).
