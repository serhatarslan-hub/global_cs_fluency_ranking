from selenium import webdriver
import time

# Topic-Googlekey map
# Keywords are ordered from most popular to least popular worldwide in 2018
#  Popularity ordering allows to compare relatively similar trends, 
# so that the precision issue, i.e. <1%, is minimized.
QUERY_MAP = {
    'java':'%2Fm%2F07sbkfb',
    'python':'%2Fm%2F05z1_',
    'javaScript':'%2Fm%2F02p97',
    'sql':'%2Fm%2F075st',
    'database':'%2Fm%2F02bc6',
    'string':'%2Fm%2F06x16',
    'c++':'%2Fm%2F0jgqg',
    'react':'%2Fm%2F012l1vxv',
    'cache':'%2Fm%2F01zyw',
    'hyperTextTransferProtocol':'%2Fm%2F03hgt',
    'forLoop':'%2Fm%2F02d6dm',
    'stack':'%2Fm%2F01p2sd',
    'regularExpression':'%2Fm%2F06f01',
    'transmissionControlProtocol':'%2Fm%2F07hzk',
    'NaN':'%2Fm%2F0d3y6',
    'artificialNeuralNetwork':'%2Fm%2F05dhw',
    'deepLearning':'%2Fm%2F0h1fn8h',
    'heap':'%2Fm%2F03mwv',
    'hashTable':'%2Fm%2F03llm',
    'logisticRegression':'%2Fm%2F01h161',
    'designThinking':'%2Fm%2F0c5z0t',
    'garbageCollection':'%2Fm%2F01z4f',
    'nullPointer':'%2Fm%2F012wkzmt',
    'finiteStateMachine':'%2Fm%2F02ykc',
    'kmeansClustering':'%2Fm%2F061s_s',
    'semaphore':'%2Fm%2F015xjd',
    'segmentationFault':'%2Fm%2F0746c',
    'computerVision':'%2Fm%2F01xzx',
    'memoryLeak':'%2Fm%2F04yqh',
    'dijkstrasAlgorithm':'%2Fm%2F0cf7t',
    'mapReduce':'%2Fm%2F05pp4x',
    'integerOverflow':'%2Fm%2F06qksn',
    'typeSystem':'%2Fm%2F01cc54',
    'gradientDescent':'%2Fm%2F01cmhh',
    'imageSegmentation':'%2Fm%2F02jj2w',
    'interactionDesign':'%2Fm%2F02lvnm',
    'instructionPipelining':'%2Fm%2F01g5qh',
    'bTree':'%2Fm%2F01h9m',
    'mutualExclusion':'%2Fm%2F09637',
    'edgeDetection':'%2Fm%2F01w_8f',
    'imageNet':'%2Fg%2F11bwhb03wl',
    'interruptHandler':'%2Fm%2F02zgwt',
    'markovChainMonteCarlo':'%2Fm%2F01jcrc',
    'pVsNpProblem':'%2Fm%2F01txp',
    'queryOptimization':'%2Fm%2F09fs7f',
    'LambdaCalculus':'%2Fm%2F04mg4',
    'TCPcongestionControl':'%2Fm%2F05r707',
    'twoPhaseLocking':'%2Fm%2F02vk5ky',
    'concurrencyControl':'%2Fm%2F01ftm6',
    'haltingProblem':'%2Fm%2F03k9j',
    'heuristicEvaluation':'%2Fm%2F01_11z',
    'spectralClustering':'%2Fm%2F0h7nlb1',
    'registerFile':'%2Fm%2F05mw3z', 
    'chernoffBound':'%2Fm%2F037gp9',
    'churchTuringThesis':'%2Fm%2F01_3k',
    'systemF':'%2Fm%2F039vd_',
    'matrixCompletion':'%2Fm%2F0jkzd0s',
    'spectralGraphTheory':'%2Fm%2F02mlcn',
    'cookLevinTheorem':'%2Fm%2F030tgp',
    'extendibleHashing':'%2Fm%2F026nrq0',
    'postCorrespondenceProblem':'%2Fm%2F0h7t4',
    'polynomialTimeReduction':'%2Fm%2F01529y',
    'linearHashing':'%2Fm%2F08hkpd',
    'countMinSketch':'%2Fm%2F0h94cvy',
    'polynomialHierarchy':'%2Fm%2F030dw0',
    'lovaszLocalLemma':'%2Fm%2F06w7zz',
    'logicalRelations':'%2Fg%2F11clwpd'
}

# Google Trends base URL
# Example full URL (comparing two terms for the year of 2018)
# https://trends.google.com/trends/explore?hl=en-US&date=2018-01-01%202018-12-31&q=%2Fm%2F0h1fn8h,%2Fm%2F05z1_
BASE_URL = "https://trends.google.com/trends/explore?hl=en-US&date=2018-01-01%202018-12-31&q="

# this is the HTML class name of the download buttons
CLASS_NAME = 'export'

def run():
    browser = webdriver.Chrome()

    allTerms = list(QUERY_MAP.keys())
    
    # Get the first keyword only data as country-wise comparison
    url = makeUrl(QUERY_MAP[allTerms[0]])
    download(browser, url)

    # Get comparison data for each keyword 
    for i in range(1,len(allTerms)):
        reference_term = allTerms[i-1]
        reference_query = QUERY_MAP[reference_term]
        term = allTerms[i]
        query = QUERY_MAP[term]
        print( reference_term + ' vs. ' + term )
        url = makeUrl(reference_query, query)
        download( browser, url )

    input('hit enter when done: ')


def download(browser, url):
    browser.get(url)
    browser.refresh()
    time.sleep(3)
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