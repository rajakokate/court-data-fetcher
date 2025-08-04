from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def parse_case_details (html):
    soup = BeautifulSoup(html, 'html.parser')
    

    #Find table rows
    rows = soup.select('table.table.table-bordered tbody tr')

    if not rows:
        print("No case details found in the response.")
        return None
    
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 4:
            case_info = cols[1].get_text(strip=True).replace('\n', ' ')
            parties = cols[2].get_text(strip= True).replace('\n', ' ')
            dates = cols[3].get_text(strip= True).replace ('\n', ' ')

        return {   
            'case info': case_info,
            'parties': parties,
            "dates": dates
        }

def get_case_status(case_type, case_number,case_year):
    # set up Chrome using web driver manager
    service = Service(ChromeDriverManager().install()) 
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # runs it in background
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')


    # Launch chrome browser
    driver = webdriver.Chrome(service=service, options=options)

    try:
            # Open delhi high court  case status page
        url = 'https://delhihighcourt.nic.in/app/get-case-type-status'
        driver.get(url)

    

        # step1 Select case type -> W.P.(CRL)
        case_type_dropdown = Select(driver.find_element(By.ID,'case_type'))
        case_type_dropdown.select_by_visible_text(case_type)

        # Step 2 Fill the case number and year
        driver.find_element(By.ID,"case_number").send_keys(case_number)
        driver.find_element(By.ID,'case_year').send_keys(case_year)

        # Step 3: Extract captcha and fill it
    

        captcha_value = driver.find_element(By.ID, 'randomid').get_attribute('value')
        driver.find_element(By.ID, 'captchaInput').send_keys(captcha_value)

        print("Captcha code(randomId)", captcha_value)

        # Step 4 click submit
        driver.find_element(By.ID,'search').click()

        #waiting timer for page load
        time.sleep(3)

        # extract result
        result = driver.page_source
        print("\n--- Expected HTML length:", len(result))
        parsed_data = parse_case_details(result)

    finally:
        driver.quit()
    return parsed_data, result




# Test run

if __name__ == '__main__':
    get_case_status()