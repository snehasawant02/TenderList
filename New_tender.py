import time
from urllib.parse import urljoin
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://bidplus.gem.gov.in/all-bids"
chrome_options = Options()
chrome_options.add_argument('--headless')

# Use a context manager to ensure the driver is closed properly
with webdriver.Chrome(options=chrome_options) as driver:
    # Set timeout time
    wait = WebDriverWait(driver, 10)

    # Use a web driver to open the page
    driver.get(url)

    # Wait for the page to load and dynamic content to appear
    time.sleep(10)

    keywords1 = 'Data Entry'

    # Find and interact with the search input box
    Keywords = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='searchBid']"))
    )
    Keywords.send_keys(keywords1)

    # Find and interact with the search button
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='searchBidRA']"))
    )
    search_button.click()

    # Wait for the page with search results to load
    time.sleep(5)

    # Loop through the pages

        # Parse the HTML content using BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all anchor tags with 'href' attribute
    href_tags = soup.find_all('a', href=True)
    base_url="https://bidplus.gem.gov.in"
    # Extract and print the href attributes
    for tag in href_tags:
        href = tag['href']
        print(href)
        if href.startswith('showbidDocument/') or href.startswith('/showradocumentPdf/') or href.startswith('/showbidDocument/'):
            full_url = urljoin(base_url, href)
            print(full_url)

        # Check if there is a next page button

