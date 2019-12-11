import numpy as np
import matplotlib.pyplot as plt

N = 8

# x = ["NN","CNN","LeNet","AlexNet","FCN", "HCNN", "RNN", "VGG11"];
y1 = [0.1532, 0.1861, 0.2618, 0.0584, 0.1839, 0.2049, 0.009, 0.2077]

ind = np.arange(N)
width = 0.35

fig, ax = plt.subplots()

ax.bar(ind, y1, width, label="One fault per run", align='center', color='b')

y2 = [0.2729, 0.2893, 0.5174, 0.1133, 0.6875, 0.8282, 0.3891, 0.8132]
ax.bar(ind+width, y2, width, label="Dynamic instance", align='center', color='r')

ax.set_ylabel('SDC rate')
ax.set_title('SDC rate (bit flip element) for 2 fault configurations')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels( ('NN', 'CNN', 'LeNet', 'AlexNet', 'FCN', 'HCNN', 'RNN', 'VGG11') )

ax.grid()
ax.legend()

# fig.savefig("DR-5.png")
plt.show()