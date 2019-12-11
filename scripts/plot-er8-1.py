import matplotlib.pyplot as plt
import numpy as np

x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
y1 = np.loadtxt('results/nn/er/allsdc.csv', delimiter='\n', unpack=True)
y2 = np.loadtxt('results/cnn/er/allsdc.csv', delimiter='\n', unpack=True)
y3 = np.loadtxt('results/lenet/er/allsdc.csv', delimiter='\n', unpack=True)
y4 = np.loadtxt('results/alexnet/er/allsdc.csv', delimiter='\n', unpack=True)
y5 = np.loadtxt('results/fcn/er/allsdc.csv', delimiter='\n', unpack=True)
y6 = np.loadtxt('results/hcnn/er/allsdc.csv', delimiter='\n', unpack=True)
y7 = np.loadtxt('results/rnn/er/allsdc.csv', delimiter='\n', unpack=True)
y8 = np.loadtxt('results/vgg11/er/allsdc.csv', delimiter='\n', unpack=True)


fig, ax = plt.subplots()

ax.plot(x,y1, label='NN')
ax.plot(x,y2, label='CNN')
ax.plot(x,y3, label='LeNet')
ax.plot(x,y4, label='AlexNet')
ax.plot(x,y5, label='FCN')
ax.plot(x,y6, label='HCNN')
ax.plot(x,y7, label='RNN')
ax.plot(x,y8, label='VGG11')

ax.legend()
ax.plot()
ax.set(xlabel="Error rate (Random element)", ylabel="SDC rate",
	title="SDC rate vs FI error rate")
ax.grid()

fig.savefig("ER-8-1.png")
plt.show()