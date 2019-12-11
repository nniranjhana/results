import numpy as np
import matplotlib.pyplot as plt

N = 8

# x = ["Comma-15","Comma-30","Comma-60","Comma-120","ResN-t1", "ResN-t5", "SqN-t1", "SqN-t5"];
y1 = [0.3776, 0.3538, 0.3304, 0.307, 0.1929, 0.1812, 0.1264, 0.1099]

ind = np.arange(N)
width = 0.35

fig, ax = plt.subplots()

ax.bar(ind, y1, width, label="One fault per run", align='center', color='b')

y2 = [0.8475, 0.8199, 0.7876, 0.757, 0.9465, 0.9425, 0.4888, 0.4411]
ax.bar(ind+width, y2, width, label="Dynamic instance", align='center', color='r')

ax.set_ylabel('SDC rate')
ax.set_title('SDC rate (bit flip element) for 2 fault configurations')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels( ('Comma-15', 'Comma-30', 'Comma-60', 'Comma-120', 'ResNet-t1', 'ResNet-t5', 'SqzeNet-t1', 'SqzeNet-t5') )

ax.tick_params(axis='x', which='major', labelsize=6.8)
# ax.tick_params(axis='both', which='minor', labelsize=6)
plt.rcParams.update({'font.size':9})

ax.grid()
ax.legend(loc="upper left")

# fig.savefig("DR-5.png")
plt.show()