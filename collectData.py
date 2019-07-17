#!/usr/bin/python

import urllib.request
import json

python_URL = "https://trends.google.com/trends/api/widgetdata/comparedgeo?hl=en-US&tz=420&req=%7B%22geo%22:%7B%7D,%22comparisonItem%22:%5B%7B%22time%22:%222018-01-01+2018-12-31%22,%22complexKeywordsRestriction%22:%7B%22keyword%22:%5B%7B%22type%22:%22ENTITY%22,%22value%22:%22%2Fm%2F05z1_%22%7D%5D%7D%7D%5D,%22resolution%22:%22COUNTRY%22,%22locale%22:%22en-US%22,%22requestOptions%22:%7B%22property%22:%22%22,%22backend%22:%22IZG%22,%22category%22:0%7D%7D&token=APP6_UEAAAAAXS5DywF6nUnJs0zsVufesN6ljLVHdnYf"
olympic_games_URL = "https://trends.google.com/trends/api/widgetdata/comparedgeo?hl=en-US&tz=420&req=%7B%22geo%22:%7B%7D,%22comparisonItem%22:%5B%7B%22time%22:%222018-01-01+2018-12-31%22,%22complexKeywordsRestriction%22:%7B%22keyword%22:%5B%7B%22type%22:%22ENTITY%22,%22value%22:%22%2Fm%2F05nd_%22%7D%5D%7D%7D%5D,%22resolution%22:%22COUNTRY%22,%22locale%22:%22en-US%22,%22requestOptions%22:%7B%22property%22:%22%22,%22backend%22:%22IZG%22,%22category%22:0%7D%7D&token=APP6_UEAAAAAXS5g5hC69tNk3bewIJatvULX11U_cLjH"

page = urllib.request.urlopen(olympic_games_URL)
page.readline() #Read the useless first-line in the response
response = page.readline().decode('utf-8')
response_dict = json.loads(response)
print(response_dict['default']['geoMapData'][0])
