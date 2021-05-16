import time
import random
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
	ticks = ''
	# guess for 10 times
	for i in range(-1, 10):
		guess = ''
		x = np.append(x, i+1)
		if i == -1:
			guess = private
		else:
			for _ in range(len(private)):
				guess += str(random.randint(0,1))
		ticks += str(i+1) + ': ' + guess + '\n'
		avg_cost = 0
		runtime = 100
		for _ in range(runtime):
			start = time.time_ns()
			guess_private(guess)
			end = time.time_ns()
			avg_cost += end - start
		avg_cost /= runtime
		y = np.append(y, avg_cost)
		print(f'{i+1}:\tAverage cost: {avg_cost}')
	
	
	plt.plot(x, y)
	plt.title('pre timing random guess; 1-1 password check')
	plt.xlabel('random guess; 1st for original exec time')
	plt.ylabel('cost time (ns)')
	plt.xticks(np.arange(0, 11, 1))
	plt.text(6, 5000, ticks)
	plt.grid()
	plt.savefig('pi_results/pre_timing_randomguess%d.pdf' % (pdf+1))
