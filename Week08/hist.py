# messing with hists

import matplotlib.pyplot as plt
import numpy as np

minSalary= 20000
maxSalary= 80000
numberOfEntries= 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

plt.hist(salaries)
plt.show()