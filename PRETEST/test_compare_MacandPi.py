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
	
f = plt.figure()
x = np.array([])
y = np.array([])
G =  ['1010101010011010', '1111010010110111', '1111101011001111', 
	'0010111101101100', '1000001000000011', '1010110000111000', 
	'0100110111000000', '1000100000011001', '0100001101000110', 
	'1100011000011100', '0010101001000011']
ticks = ''
# guess for 10 times
for i in range(len(G)):
	guess = G[i]
	x = np.append(x, i)
	ticks += str(i) + ': ' + guess + '\n'
	
	avg_cost = 0
	runtime = 100
	for _ in range(runtime):
		start = time.time_ns()
		guess_private(guess)
		end = time.time_ns()
		avg_cost += end - start
	avg_cost /= runtime
	y = np.append(y, avg_cost)
	print(f'{i}:\tAverage cost: {avg_cost}')


plt.plot(x, y)
plt.title('pre timing random guess; 1-1 password check')
plt.xlabel('random guess; 1st for original exec time')
plt.ylabel('cost time (ns)')
plt.xticks(np.arange(0, 11, 1))
plt.text(6, 5000, ticks) # for pi
#plt.text(6, 1100, ticks) # for mac
plt.grid()
plt.savefig('pi_results/test_compare.pdf')
#plt.savefig('mac_results/test_compare.pdf')

