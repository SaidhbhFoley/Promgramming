# Messing with pie charts

import numpy as np
import matplotlib.pyplot as plt

possibleCounties = ('Dublin', 'Claire', 'Galway', 'Donegal', 'Kerry')
counties=np.random.choice(
    possibleCounties,
    p=[0.1, 0.3, 0.2, 0.12, 0.28 ],
    size=(100)
)

unique, counts = np.unique(counties, return_counts=True)
#plt.pie(counts, labels= unique)
#plt.show()

plt.bar(unique, counts)
plt.show()