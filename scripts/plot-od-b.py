import numpy as np
import matplotlib.pyplot as plt

x = ["NN","CNN","LeNet","AlexNet","FCN"];
y1 = [0.1532, 0.1861, 0.2618, 0.0584, 0.1839]
plt.scatter(x, y1, label="One fault per run")

plt.plot()
plt.xlabel("Bit flip element fault type")
plt.ylabel("SDC rate over 1000 injections on 10 inputs")
y2 = [0.2729, 0.2893, 0.5174, 0.1133, 0.6875]
plt.scatter(x, y2, label="Dynamic instance")
plt.plot()
plt.grid()
plt.legend()

# fig.savefig("DR-5.png")
plt.show()