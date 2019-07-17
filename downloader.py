from selenium import webdriver

# Topic-Googlekey map
QUERY_MAP = {
    'deepLearning':'%2Fm%2F0h1fn8h',
    'python':'%2Fm%2F05z1_',
    'kmeans':'%2Fm%2F061s_s'
}
# Google Trends base URL
# Example full URL
# https://trends.google.com/trends/explore?q=%2Fm%2F0h1fn8h,%2Fm%2F05z1_
BASE_URL = "https://trends.google.com/trends/explore?hl=en-US&date=2018-01-01%202018-12-31&q="

# this is the HTML class name of the download buttons
CLASS_NAME = 'export'

def run():
    browser = webdriver.Chrome()
    allTerms = list(QUERY_MAP.keys())
    N = len(allTerms)
    # only one comparison per pair
    for i in range(N):
        for j in range(i + 1, N):
            term1 = allTerms[i]
            term2 = allTerms[j]
            print(term1 + ',' + term2)
            download(browser, term1, term2)
    input('hit enter when done: ')


def download(browser, termA, termB):
    url = makeUrl(termA, termB)
    browser.get(url)
    browser.refresh()
    elements = browser.find_elements_by_class_name(CLASS_NAME)
    # There are six download buttons on the page.
    # 0: interest over time
    # 1: comparison by region
    # 2: term1 interest by region
    # 3: term1 related terms
    # 4: term2 interest by region
    # 5: term2 related terms
    # To start, we want [1] comparison by region
    perhapsElem = elements[1]
    perhapsElem.click();

def makeUrl(termA, termB):
    query = QUERY_MAP[termA] + "," + QUERY_MAP[termB]
    return BASE_URL + query

if __name__ == '__main__':
   run()