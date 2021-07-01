import time
import sys
sys.path.append('/Users/yulu/Desktop/PRETEST')
print()

from key_generate import key_generate
from sliding_windows.SlidingWindows import *
from ET_vs_proc import draw

proc0 = []
proc1 = []
et = []

KEY = key_generate(512)
#print('test private key is:', KEY.pri)

# slide private key

# 512 bit window length is 5
h = SlidingWindows(KEY.pri, 5)
#print('windows:', h)
Process = [len(h), 0] # 0: S; 1: M
for i in h:
	if int(i, 2) == 0:
		Process[1] += 1
proc0.append(Process[0])
proc1.append(Process[1])
#print('test RSA encode & decode with normal way####')
m = 88888888
c = KEY.encode(m)
'''
print('    ciphertext is:', c)
print('    does it decode successfully?')
print('----', KEY.decode(c) == m)
print()
print('test RSA decode with sliding windows####')
print('here we use ciphertext above############')
'''
start = time.time_ns()
M = SWdecode(h, c, KEY.N)
end = time.time_ns()
et.append(end-start)

print('\tsliding windows method result:')
print('\t%d' % M)
print('\texecute time: %dns' % (end-start))
print('\tSquare: %d times' % Process[0])
print('\tMultiply: %d times' % Process[1])
print()


