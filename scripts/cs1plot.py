import numpy as np
import matplotlib.pyplot as plt
import math

N = 6

y2 = [0.3832, 0.3498, 0.3472, 0.3386, 0.3164, 0.2952]
y3 = [0.2813, 0.2554, 0.263, 0.2362, 0.2179, 0.2061]
y4 = [0.4348, 0.3954, 0.3465, 0.3154, 0.2869, 0.2396]

ind = np.arange(N)
width = 0.2

fig, ax = plt.subplots()

ax.bar(ind, y2, width, label="2 layers", align='center', color='purple')
ax.bar(ind+width, y3, width, label="3 layers", align='center', color='violet')
ax.bar(ind+2*width, y4, width, label="4 layers", align='center', color='indigo')

ax.set_ylabel('SDC Rate')
ax.set_xlabel('Number of neurons')
ax.set_title('SDC Rate vs. Hyperparameter Variation')
ax.set_xticks(ind+width)
ax.set_xticklabels(('16', '32', '64', '128', '256', '512'))

ax.grid()
ax.legend()
plt.show()
