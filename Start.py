# NEA.real.start
import csv
import urllib.request
DataRepository = "https://football-data.co.uk/mmz4281/2526/E0.csv"
rawData = urllib.request.urlopen(DataRepository)
textLines = [line.decode('utf-8') for line in rawData.readlines()]
Rows = csv.DictReader(textLines)




#https://dashee87.github.io/football/python/predicting-football-results-with-statistical-modelling-dixon-coles-and-time-weighting/
