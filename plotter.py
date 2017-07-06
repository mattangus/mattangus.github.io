import matplotlib.pyplot as plt
import numpy as np

def bell_fn(x, a, b, c):
	inner = (x - c) / a;
	outer = 1 + (pow(abs(inner), 2.0 * b));
	return 1 / outer;

def bell(x, a, b, c, greater, less):
	y = np.zeros(x.shape)
	for i in range(len(x)):
		if greater and x[i] > c:
			y[i] = 1
		elif less and x[i] < c:
			y[i] = 1
		else:
			y[i] = bell_fn(x[i], a, b, c)
	return y

def inv_bell(x, a, b, c, right):
	y = np.zeros(x.shape)
	for i in range(len(x)):
		if right and x[i] < c:
			y[i] = 0
		elif not right and x[i] > c:
			y[i] = 0
		else:
			y[i] = 1 - bell_fn(x[i], a, b, c)
	return y

def gauss_fn(x, c, s):
	inner = (x - c) / s;
	temp = np.exp((-0.5) * (inner * inner));
	return temp;

def gauss(x, c, s, greater, less):
	y = np.zeros(x.shape)
	for i in range(len(x)):
		if greater and x[i] > c:
			y[i] = 1
		elif less and x[i] < c:
			y[i] = 1
		else:
			y[i] = gauss_fn(x[i], c, s)
	return y

def inv_gauss(x, c, s, right):
	y = np.zeros(x.shape)
	for i in range(len(x)):
		if right and x[i] < c:
			y[i] = 0
		elif not right and x[i] > c:
			y[i] = 0
		else:
			y[i] = 1 - gauss_fn(x[i], c, s)
	return y


def near_far():
	x = np.arange(-1.0, 4.0, 0.005)
	near = bell(x, 1, 3, 0.5, False, True)
	far = bell(x, 1, 3, 2.5, True, False)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	near_line, = ax.plot(x, near)
	far_line, = ax.plot(x, far)
	ax.legend([near_line, far_line], ['Near', 'Far'])
	ax.grid(True)
	ax.set_xlabel('distance')
	ax.set_ylabel('membership')
	plt.show()

def target():
	x = np.arange(-40, 40, 0.01)
	right = inv_bell(x, 15.0, 3.0, 0.0, False)
	ahead = bell(x, 15.0, 3.0, 0.0, False, False)
	left = inv_bell(x, 15.0, 3.0, 0.0, True)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	right_line, = ax.plot(x, right)
	ahead_line, = ax.plot(x, ahead)
	left_line, = ax.plot(x, left)
	ax.legend([right_line, ahead_line, left_line], ['Right', 'Ahead', 'Left'])
	ax.grid(True)
	ax.set_xlabel('angle')
	ax.set_ylabel('membership')
	plt.show()

def free():
	x = np.arange(-20, 20, 0.01)
	right = inv_gauss(x, 0.0, 5.0, False)
	ahead = gauss(x, 0.0, 5.0, False, False)
	left = inv_gauss(x, 0.0, 5.0, True)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	right_line, = ax.plot(x, right)
	ahead_line, = ax.plot(x, ahead)
	left_line, = ax.plot(x, left)
	ax.legend([right_line, ahead_line, left_line], ['Right', 'Ahead', 'Left'])
	ax.grid(True)
	ax.set_xlabel('angle')
	ax.set_ylabel('membership')
	plt.show()

free()