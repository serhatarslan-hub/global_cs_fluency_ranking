"""
This script is used to automatically download data from Google Trends, using
webdriver.
"""

from selenium import webdriver
import time
from constants import *

def download(browser, url):
    """
    Use Chrome, piloted by webdriver, to download data from Google Trends.

    When on a Google Trends page, there are six download buttons on the page:
    0: interest over time
    1: comparison by region
    2: term1 interest by region
    3: term1 related terms
    4: term2 interest by region
    5: term2 related terms

    To start, we want [1] comparison by region
    """

    browser.get(url)
    browser.refresh()
    time.sleep(SLEEP_TIME)
    elements = browser.find_elements_by_class_name(CLASS_NAME)
    regionComparison = elements[1]
    regionComparison.click();

def makeUrl(query1, query2=None):
    """
    Create a full Google Trends URL programatically, from the search terms' keys.

    Supports passing both one term's key (standalone measurement) and two terms'
    keys (for comparison)
    """

    if query2 is not None:
        return BASE_URL + query1 + "," + query2
    else:
        return BASE_URL + query1

def run(verbose = False):
    """
    Iterate through the queries in constants.QUERY_MAP and gather relative
    term interest automatically from Google Trends.

    """
    browser = webdriver.Chrome()
    all_terms = list(QUERY_MAP.keys())

    # Get relative interest for each keyword
    for i in range(0, len(all_terms)):
        if i == 0:
            # Get only the first keyword's data for country-wise comparison
            url = makeUrl(QUERY_MAP[all_terms[0]])
            download(browser, url)
            continue

        reference_term = all_terms[i-1]
        reference_query = QUERY_MAP[reference_term]
        term = all_terms[i]
        query = QUERY_MAP[term]

        if verbose:
            print(reference_term + ' vs. ' + term)

        url = makeUrl(reference_query, query)
        download(browser, url)

    input('Hit enter when done: ')

if __name__ == '__main__':
   run()
