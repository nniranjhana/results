import matplotlib.pyplot as plt
import numpy as np

x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
y1 = np.loadtxt('results/comma-120/er/allsdc.csv', delimiter='\n', unpack=True)
y2 = np.loadtxt('results/comma-60/er/allsdc.csv', delimiter='\n', unpack=True)
y3 = np.loadtxt('results/comma-30/er/allsdc.csv', delimiter='\n', unpack=True)
y4 = np.loadtxt('results/comma-15/er/allsdc.csv', delimiter='\n', unpack=True)
y5 = np.loadtxt('results/resnet-1/er/allsdc.csv', delimiter='\n', unpack=True)
y6 = np.loadtxt('results/resnet-5/er/allsdc.csv', delimiter='\n', unpack=True)
y7 = np.loadtxt('results/sqn-1/er/allsdc.csv', delimiter='\n', unpack=True)
y8 = np.loadtxt('results/sqn-5/er/allsdc.csv', delimiter='\n', unpack=True)


fig, ax = plt.subplots()

ax.plot(x,y1, label='Comma-120')
ax.plot(x,y2, label='Comma-60')
ax.plot(x,y3, label='Comma-30')
ax.plot(x,y4, label='Comma-15')
ax.plot(x,y5, label='Resnet-18-top1')
ax.plot(x,y6, label='Resnet-18-top5')
ax.plot(x,y7, label='SqueezeNet-top1')
ax.plot(x,y8, label='SqueezeNet-top5')


ax.legend()
ax.plot()
ax.set(xlabel="Error rate (Random element)", ylabel="SDC rate",
	title="SDC rate vs FI error rate")
ax.grid()

fig.savefig("ER-8-2.png")
plt.show()