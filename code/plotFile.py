from matplotlib import pyplot as plt
from numpy import loadtxt
from sys import argv

data = loadtxt(argv[1]).T

plt.plot(data[0], data[1])
plt.grid(True)
plt.show()
