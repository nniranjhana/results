import matplotlib.pyplot as plt
import numpy as np
import math

# x = [ "ARGMAX", "CONV2D", "EQUAL", "FLOOR", "MATMUL", "MAXPOOL", "MEAN", "MUL", "REALDIV", "RELU", "SOFTMAX", "SUB"]
# y = [ 1, 0.2125, 1, 0.1649, 0.0551, 0.3642, 0.0325, 0.1496, 0.1484, 0.2881, 0.6024, 0.0253]


x2 = ["Conv", "Relu", "Maxpool", "Softmax"]
y2 = [0.2125, 0.2881, 0.3642, 0.6024]

y2err = []

for item in y2:
	err = 1.96*(math.sqrt(item*(1-item)/10000))
	y2err.append(err)

print max(y2err)
print min(y2err)


x1=["Add", "Sub", "Mul", "Div", "Matmul"]
y1 = [0.1113, 0.0253, 0.1496, 0.1484, 0.0551]

y1err = []

for item in y1:
	err = 1.96*(math.sqrt(item*(1-item)/10000))
	y1err.append(err)

print max(y1err)
print min(y1err)

x3=["Argmax", "Equal"]
y3=[1, 1]



fig, ax = plt.subplots()
ax.bar(x1, y1,label="General computation operators")
ax.bar(x1, y1err, bottom=y1, color='cyan')

ax.bar(x2, y2,label="Convolutional computation operators")
ax.bar(x2, y2err, bottom=y2, color='yellow')

ax.bar(x3, y3,label="Final classification operators")
ax.set_ylabel('SDC rate')
ax.set_title('SDC rate (single bit flip) over operators in CNN model')


# plt.rcParams.update({'font.size':14})
ax.tick_params(axis='both', which='major', labelsize=7)
ax.tick_params(axis='both', which='minor', labelsize=7)
ax.plot()
ax.grid()
ax.legend()
plt.show()