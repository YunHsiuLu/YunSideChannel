import sys
sys.path.append('/Users/yulu/Desktop/PRETEST')

from default_keys import KEY512
from sliding_windows.SlidingWindows import SlidingWindows
from time import time_ns
import random
import numpy as np
import matplotlib.pyplot as plt

# RSA512 for L = 5
#h = SlidingWindows(KEY512.pri, 5)
h = ['10111', '0', '11011', '10001', '11000', '11100', '10111', '10111', '000', '11010', '00000', '10000', '0', '10111', '000', '10110', '11010', '000', '11101', '10000', '0', '10000', '11010', '0', '11010', '0', '11111', '00', '11000', '0', '10101', '11010', '0', '10011', '10110', '10011', '0', '10111', '11110', '10101', '000', '11010', '00', '11111', '10101', '0', '11001', '10000', '11111', '10101', '00', '11011', '0000', '11000', '10100', '0', '10011', '11011', '000000', '10011', '0', '10110', '10100', '000', '11110', '0', '10011', '11110', '11111', '10000', '0', '11101', '11011', '11010', '11000', '00', '11100', '11100', '0', '10100', '0', '11010', '000', '11011', '0', '10001', '10101', '00', '10101', '000', '11000', '10010', '11011', '10010', '000', '11111', '0', '11101', '11000', '11000', '10010', '000000', '10001', '0', '11000', '10111', '00', '11000', '000', '10110', '10001', '0', '10100', '10011', '10101', '0', '11011', '11010', '0', '10100', '000', '10001', '11100', '0', '10010', '00', '11001']
n = KEY512.N
x = np.arange(0, len(h))

'''
# sliding window c1

window_time = []
m = 8888888888
c = pow(m, KEY512.pub, n)
M = 1

for i in range(len(h)):
	start = time_ns()

	M = pow(M, 2**len(h[i]), n)
	if not int(h[i], 2) == 0:
		M = (M * pow(c, int(h[i], 2))) % n

	end = time_ns()
	window_time.append(end-start)
	#print('window%d execute time: %d ns' % (i,end-start))

y1 = np.array(window_time)

# sliding window c2

window_time = []
m = 3333
c = pow(m, KEY512.pub, n)
M = 1

for i in range(len(h)):
	start = time_ns()

	M = pow(M, 2**len(h[i]), n)
	if not int(h[i], 2) == 0:
		M = (M * pow(c, int(h[i], 2))) % n

	end = time_ns()
	window_time.append(end-start)
	#print('window%d execute time: %d ns' % (i,end-start))

y2 = np.array(window_time)

# sliding window c3

window_time = []
m = 111111
c = pow(m, KEY512.pub, n)
M = 1

for i in range(len(h)):
	start = time_ns()

	M = pow(M, 2**len(h[i]), n)
	if not int(h[i], 2) == 0:
		M = (M * pow(c, int(h[i], 2))) % n

	end = time_ns()
	window_time.append(end-start)
	#print('window%d execute time: %d ns' % (i,end-start))

y3 = np.array(window_time)
'''

# sliding window for a set
y = []
for _ in range(5):
	window_time = []
	m = random.randint(0, 1e8)
	c = pow(m, KEY512.pub, n)
	M = 1
	for i in range(len(h)):
		start = time_ns()
		M = pow(M, 2**len(h[i]), n)
		if not int(h[i], 2) == 0:
			M = (M * pow(c, int(h[i], 2))) % n
		end = time_ns()
		window_time.append(end-start)
	y.append(window_time)

y = np.array(y)
label = ['c1', 'c2', 'c3', 'c4', 'c5']
color = ['r', 'g', 'b', 'k', 'c']

fig, axs = plt.subplots(5, 1, sharex=True, sharey=True, figsize = (12, 7))
fig.suptitle('Decrypt a set of ciphertext each window execution time')
axs[-1].set_xlabel('.', color=(0,0,0,0))
axs[-1].set_ylabel('.', color=(0,0,0,0))
fig.text(0.5, 0.02, 'Window No.', ha='center')
fig.text(0.01, 0.5, 'Execution Time (ns)', va='center', rotation='vertical')
from matplotlib import ticker
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1))

for i in range(5):
	axs[i].set_title('Decrypt c%d' % (i+1))
	axs[i].bar(x, y[i], color = color[i])
	axs[i].yaxis.set_major_formatter(formatter)
for a in axs.flat:
	a.label_outer()
plt.tight_layout()


plt.savefig('Multi_WindowExTime.pdf')
plt.savefig('Multi_WindowExTime.png')


#plt.show()
