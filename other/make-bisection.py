import numpy as np
from matplotlib import pyplot as plt

#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True

xrange = (-10, 10)
yrange = (-10, 10)

def f(x):
   return 0.02 * x**3 + 2

x = np.linspace(*xrange, 100)

plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.axis([*xrange, *yrange])
plt.xticks(range(*xrange, 2))
plt.yticks(range(*yrange, 2))

plt.plot(x, f(x), color='grey')
plt.savefig('bisection.svg')
plt.show()