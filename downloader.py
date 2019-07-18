from selenium import webdriver
import time

# Reference keyword for comparison
REFERENCE = {
    'keyword':'hashTable',
    'query':'%2Fm%2F03llm'
}
# Topic-Googlekey map
QUERY_MAP = {
    'python':'%2Fm%2F05z1_',
    'react':'%2Fm%2F012l1vxv',
    'javaScript':'%2Fm%2F02p97',
    'pVsNpProblem':'%2Fm%2F01txp',
    'churchTuringThesis':'%2Fm%2F01_3k',
    'polynomialTimeReduction':'%2Fm%2F01529y',
    'finiteStateMachine':'%2Fm%2F02ykc',
    'haltingProblem':'%2Fm%2F03k9j',
    'java':'%2Fm%2F07sbkfb',
    'forLoop':'%2Fm%2F02d6dm',
    'string':'%2Fm%2F06x16',
    'segmentationFault':'%2Fm%2F0746c',
    'integerOverflow':'%2Fm%2F06qksn',
    'memoryLeak':'%2Fm%2F04yqh',
    'stack':'%2Fm%2F01p2sd',
    'heap':'%2Fm%2F03mwv',
    'NaN':'%2Fm%2F0d3y6',
    'mutualExclusion':'%2Fm%2F09637',
    'c++':'%2Fm%2F0jgqg',
    'semaphore':'%2Fm%2F015xjd',
    'hyperTextTransferProtocol':'%2Fm%2F03hgt',
    'nullPointer':'%2Fm%2F012wkzmt',
    'regularExpression':'%2Fm%2F06f01',
    'edgeDetection':'%2Fm%2F01w_8f',
    'computerVision':'%2Fm%2F01xzx',
    'imageSegmentation':'%2Fm%2F02jj2w',
    'garbageCollection':'%2Fm%2F01z4f',
    'transmissionControlProtocol':'%2Fm%2F07hzk',
    'TCPcongestionControl':'%2Fm%2F05r707',
    'database':'%2Fm%2F02bc6',
    'designThinking':'%2Fm%2F0c5z0t',
    'heuristicEvaluation':'%2Fm%2F01_11z',
    'interactionDesign':'%2Fm%2F02lvnm',
    'polynomialHierarchy':'%2Fm%2F030dw0',
    'cookLevinTheorem':'%2Fm%2F030tgp',
    'postCorrespondenceProblem':'%2Fm%2F0h7t4',
    'markovChainMonteCarlo':'%2Fm%2F01jcrc',
    'dijkstrasAlgorithm':'%2Fm%2F0cf7t',
    'countMinSketch':'%2Fm%2F0h94cvy',
    'spectralGraphTheory':'%2Fm%2F02mlcn',
    'spectralClustering':'%2Fm%2F0h7nlb1',
    'cache':'%2Fm%2F01zyw',
    'interruptHandler':'%2Fm%2F02zgwt',
    'registerFile':'%2Fm%2F05mw3z',
    'instructionPipelining':'%2Fm%2F01g5qh',
    'kmeansClustering':'%2Fm%2F061s_s',
    'artificialNeuralNetworks':'%2Fm%2F05dhw',
    'logisticRegression':'%2Fm%2F01h161',
    'gradientDescent':'%2Fm%2F01cmhh',
    'deepLearning':'%2Fm%2F0h1fn8h',
    'imageNet':'%2Fg%2F11_ryl961',
    'concurrencyControl':'%2Fm%2F01ftm6',
    'queryOptimization':'%2Fm%2F09fs7f',
    'sql':'%2Fm%2F075st',
    'twoPhaseLocking':'%2Fm%2F02vk5ky',
    'bTree':'%2Fm%2F01h9m',
    'extendibleHashing':'%2Fm%2F026nrq0',
    'linearHashing':'%2Fm%2F08hkpd',
    'mapReduce':'%2Fm%2F05pp4x',
    'chernoffBound':'%2Fm%2F037gp9',
    'lovaszLocalLemma':'%2Fm%2F06w7zz',
    'matrixCompletion':'%2Fm%2F0jkzd0s',
    'LambdaCalculus':'%2Fm%2F04mg4',
    'systemF':'%2Fm%2F039vd_',
    'logicalRelations':'%2Fm%2F01cc54'
}

# Google Trends base URL
# Example full URL (comparing two terms for the year of 2018)
# https://trends.google.com/trends/explore?hl=en-US&date=2018-01-01%202018-12-31&q=%2Fm%2F0h1fn8h,%2Fm%2F05z1_
BASE_URL = "https://trends.google.com/trends/explore?hl=en-US&date=2018-01-01%202018-12-31&q="

# this is the HTML class name of the download buttons
CLASS_NAME = 'export'

def run():
    browser = webdriver.Chrome()

    # Get the reference keyword only data first
    url = makeUrl(REFERENCE['query'])
    download(browser, url)
    time.sleep(1)

    # Get comparison data for each keyword 
    reference_term = REFERENCE['keyword']
    reference_query = REFERENCE['query']
    for term, query in QUERY_MAP.items():
        print( reference_term + ' vs. ' + term )
        url = makeUrl(reference_query, query)
        download( browser, url )

    input('hit enter when done: ')


def download(browser, url):
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
    regionComparison = elements[1]
    regionComparison.click();

def makeUrl(queryA, queryB=None):
    if queryB is not None:
        return BASE_URL + queryA + "," + queryB
    else:
        return BASE_URL + queryA

if __name__ == '__main__':
   run()