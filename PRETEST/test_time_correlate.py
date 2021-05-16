import time
import numpy as np
import matplotlib.pyplot as plt

private = '1010101010011010'

def guess_private(guess):
	if len(guess) != len(private):
		return False
	for i in range(len(guess)-1, -1, -1):
		if guess[i] != private[i]:
			return False
	return True

for pdf in range(4):
	f = plt.figure()
	x = np.array([])
	y = np.array([])
	for i in range(-1, len(private)):
		x = np.append(x, i+1)
		if i == -1:
			guess = private
		else:
			t = ''
			if private[i] == '1':
				t = '0'
			else:
				t = '1'
			guess = private[0:i] + t + private[i+1:]
		
		avg_cost = 0
		runtime = 100
		for _ in range(runtime):
			start = time.time_ns()
			guess_private(guess)
			end = time.time_ns()
			avg_cost += end - start
		avg_cost /= runtime
		y = np.append(y, avg_cost)
		print(f'{i+1}: Average cost: {avg_cost}')

	plt.plot(x, y)
	plt.title('pre timing test; 1-1 password check')
	plt.xlabel('bit # wrong; 0 for all correct')
	plt.ylabel('cost time (ns)')
	plt.xticks(np.arange(0, 17, 1))
	plt.grid()
	plt.savefig('pre_timing_test%d.pdf' % (pdf+1))


