import matplotlib.pyplot as plt
import pylab as pl

def plotData(x, xlabel, y, ylabel, title): 
    plt.plot(x, y, 'r-', label='Distance')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend(loc='best')
    plt.title(title)
    plt.show()

# Varying distance 
distance = [10, 50, 100, 200, 300, 500]
decisionTime = [0.984, 0.921, 0.852, 0.706, 0.489, 0.368]
xlabel = 'Distance'
ylabel = 'Percent Time Elapsed Till 50% Certainty'
title = 'Percent Time Elapsed Till 50% Certainty with Varying Distance'
plotData(distance, xlabel, decisionTime, ylabel, title)

# Varying 