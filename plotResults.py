import matplotlib.pyplot as plt
import pylab as pl
import pandas as pd 
import math

csv_dir = 'rawData/'
levels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def plotData(x, xlabel, y, ylabel, title): 
    plt.plot(x, y, 'r-', label='Distance')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend(loc='best')
    plt.title(title)
    plt.show()

def plotHumanData(x, xlabel, red, green, unsure, ylabel, title): 
    plt.plot(x, red, 'r-', label='Red Block')
    plt.plot(x, green, 'g-', label='Green Block')
    plt.plot(x, unsure, 'b-', label='Uncertain')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend(loc='best')
    plt.title(title)
    plt.show()

def getProcessedCSV(level): 
	df = pd.read_csv(csv_dir + 'processed_' + str(level) + '.csv')
	time_list = df['time'].tolist()
	last_t = len(time_list)-1
	for t in range(len(time_list)):
		if math.isnan(time_list[t]): 
			last_t = t-1 
			break 
	df['time'] = df['time'] / time_list[last_t]
	return df['time'][0:last_t], df['unsure percent'][0:last_t], df['green percent'][0:last_t], df['red percent'][0:last_t]

# # Varying distance 
# distance = [10, 50, 100, 200, 300, 500]
# decisionTime = [0.984, 0.921, 0.852, 0.706, 0.489, 0.368]
# xlabel = 'Distance'
# ylabel = 'Percent Time Elapsed Till 50% Certainty'
# title = 'Percent Time Elapsed Till 50% Certainty with Varying Distance'
# plotData(distance, xlabel, decisionTime, ylabel, title)

# Human Data 
for l in levels: 
	x, unsure, green, red = getProcessedCSV(l)
	xlabel = 'Time'
	ylabel = 'Average Estimation'
	title = 'Estimation of Status vs. Time'
	plotHumanData(x, xlabel, red, green, unsure, ylabel, title)

