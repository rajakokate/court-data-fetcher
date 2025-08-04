from flask import Flask, render_template, request
import sqlite3
from flask import g


from scraper.delhi_high_court import get_case_status

app = Flask(__name__)

DATABASE = 'cases.db'

def get_db ():
    db = getattr(g,'_database', None)

    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exc):
    db = getattr(g,'_database',None)
    if db:
        db.close()


#Home route: show the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/search', methods=['POST'])
def search ():
    case_type = request.form.get('case_type')
    case_number  = request.form.get('case_number')
    filing_year = request.form.get("filing_year")

    # call scrapping function 
    try:
        result = get_case_status(case_type,case_number,filing_year)
        case_data, raw_html = result
    except Exception as e:
        print("Scrapper Error:", e)
        return '<h3>Error: Error could not fetch case details. Please check your input or try again later</h3>'

    # Insert into database
    if raw_html:
        db = get_db()
        db.execute('''
            INSERT INTO case_logs (case_type, case_number, filing_year, raw_html)
            VALUES  (?, ?, ?, ?)
            ''', (case_type, case_number, filing_year, raw_html))
        db.commit()

    if case_data:
        return render_template('results.html', data = case_data)
    else:
        return '<h3>No Case data found. Please verify case_details and try again</h3>'

if __name__ == '__main__':
    app.run(debug=True)