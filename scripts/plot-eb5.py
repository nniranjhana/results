import matplotlib.pyplot as plt
import numpy as np

x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
y1 = np.loadtxt('results/nn/eb/allsdc.csv', delimiter='\n', unpack=True)
y2 = np.loadtxt('results/cnn/eb/allsdc.csv', delimiter='\n', unpack=True)
y3 = np.loadtxt('results/lenet/eb/allsdc.csv', delimiter='\n', unpack=True)
y4 = np.loadtxt('results/alexnet/eb/allsdc.csv', delimiter='\n', unpack=True)
y5 = np.loadtxt('results/fcn/eb/allsdc.csv', delimiter='\n', unpack=True)


fig, ax = plt.subplots()

ax.plot(x,y1, label='NN')
ax.plot(x,y2, label='CNN')
ax.plot(x,y3, label='LeNet')
ax.plot(x,y4, label='AlexNet')
ax.plot(x,y5, label='FCN')

ax.legend()
ax.plot()
ax.set(xlabel="Error rate (Bit flip element)", ylabel="SDC rate over 1000 injections on 10 inputs",
	title="SDC rate vs FI error rate")
ax.grid()

fig.savefig("EB-5.png")
plt.show()