DROP TABLE IF EXISTS case_logs;

CREATE TABLE case_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    case_type TEXT NOT NULL,
    case_number TEXT NOT NULL,
    filing_year TEXT NOT NULL,
    raw_html TEXT NOT NULL
);