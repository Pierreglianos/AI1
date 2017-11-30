import numpy as np
from matplotlib import pyplot as plt

X = np.array([400,900,390,1000,550])
minX = min(X)
T = np.linspace(0.01, 5, 100)
# xSum = np.sum(np.power(X, -1 * np.power(T, -1)))
# TODO : Write the code as explained in the instructions
plt.axis([0, 5, 0, 1])
plt.title("Probability as a function of the temperature")
plt.ylabel("P")
plt.xlabel("T")
plt.grid()

for x in X:
    Y = [((np.power(x/minX, -1/t))/(np.sum(np.power(X/minX, -1/t)))) for t in T]
    plt.plot(Y)
    plt.show(block=False)
    plt.waitforbuttonpress()

plt.legend(X)
plt.waitforbuttonpress()