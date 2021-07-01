import numpy as np
import matplotlib.pyplot as plt

def draw(p0: list, p1: list, et: list):
	x0 = np.array(p0)
	x1 = np.array(p1)
	y = np.array(et)
	plt.figure(figsize=(10, 6))
	plt.subplot(121)
	plt.xlabel('# of squares')
	plt.ylabel('execution time(ns)')
	plt.plot(x0, y, 'o')
	plt.subplot(122)
	plt.plot(x1, y, 'o')
	plt.xlabel('# of multiplies')
	plt.ylabel('execution time(ns)')

	plt.show()