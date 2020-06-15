# Time, in seconds, for chromedriver to wait for the page to load
SLEEP_TIME = 3

# The Base URL for Google Trends.
# Example full URL, (comparing two terms for the year of 2018):
# https://trends.google.com/trends/explore?hl=en-US&date=2018-01-01%202018-12-31&q=%2Fm%2F0h1fn8h,%2Fm%2F05z1_
BASE_URL = "https://trends.google.com/trends/explore?hl=en-US&date=2018-01-01%202018-12-31&q="

# HTML class name of the download buttons
CLASS_NAME = 'export'

# Topic -> Googlekey map, for programmatically searching Google Trends.
# The keywords are ordered from most popular to least popular worldwide in 2018.
# Ordering by pouplarity allows to compare relatively similar trends,
# so that precision issues are minimized (e.g. for numbers < 1%).
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
