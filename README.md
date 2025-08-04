# Court-Data Fetcher & Mini-Dashboard

## Overview

This project is a simple web application that allows users to search for case details from the **Delhi High Court** website. The user can input a case type, case number, and filing year. The app programmatically scrapes the court’s official site to fetch and display the case metadata and the most recent judgment/order PDF link.

This submission is part of the Internship Assignment – Task 1: *“Court-Data Fetcher & Mini-Dashboard”*.

## Features

- Simple form-based UI to input:
  - Case Type
  - Case Number
  - Filing Year
  - Captcha
- Backend using Python, Flask, and Selenium to:
  - Bypass view-state and captcha handling
  - Scrape Delhi High Court case status data
- Parses and displays:
  - Case information
  - Party names
  - Latest judgment/order PDF link (if available)
- Stores:
  - Each search query
  - Raw HTML response
  - In SQLite database
- Error handling for:
  - Invalid input
  - Court website issues

## Court Targeted

**Delhi High Court**  
Official URL: https://delhihighcourt.nic.in/app/get-case-type-status

## Tech Stack

- **Language:** Python 3.x  
- **Web Framework:** Flask  
- **Scraping Tools:** Selenium, BeautifulSoup  
- **Database:** SQLite  
- **Browser Driver:** ChromeDriver (managed via `webdriver-manager`)

## CAPTCHA Strategy

The Delhi High Court site includes a CAPTCHA code pre-filled in a hidden input field named `randomid`.  
We extract its value using:

```python
captcha_value = driver.find_element(By.ID, 'randomid').get_attribute('value')
driver.find_element(By.ID, 'captchaInput').send_keys(captcha_value)
````

This method works without using any external CAPTCHA solvers or image recognition.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/court-data-fetcher.git
cd court-data-fetcher
```

### 2. Create and activate virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> Sample `requirements.txt`:

```
Flask
selenium
bs4
webdriver-manager
```

### 4. Initialize the database

```bash
python init_db.py
```

### 5. Run the Flask app

```bash
python app.py
```

Access the app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Folder Structure

```
court-data-fetcher/
│
├── app.py                 # Main Flask application
├── init_db.py             # Script to initialize SQLite DB
├── schema.sql             # SQL schema for query logging
├── scraper/
│   └── delhi_high_court.py   # Scraping logic for Delhi High Court
├── templates/
│   ├── index.html         # Search form UI
│   └── results.html       # Parsed case result display
├── cases.db               # SQLite DB file (auto-created)
├── README.md
├── LICENSE
└── requirements.txt
```

## Known Issues / Limitations

* CAPTCHA handling works only because the current site uses a hidden field. If the format changes or CAPTCHA becomes image-based, this may break.
* Only supports Delhi High Court for now.
* Only fetches the **latest** order/judgment PDF (no pagination).

## License

This project is licensed under the MIT License. See `LICENSE` file for details.

## References / Credits

* Selenium WebDriver
* BeautifulSoup
* webdriver-manager
* Delhi High Court Official Website: [https://delhihighcourt.nic.in/](https://delhihighcourt.nic.in/)

## Demo Video

**\[To be added after recording]**
(Include YouTube or Loom link here)

```

```
