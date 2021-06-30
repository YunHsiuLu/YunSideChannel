import sys
sys.path.append('/Users/yulu/Desktop/PRETEST')
print()

from key_generate import key_generate
from sliding_windows.SlidingWindows import *

KEY = key_generate(512)
print('test private key is:', KEY.pri)

# slide private key

# 512 bit window length is 4
h = SlidingWindows(KEY.pri, 4)
print('windows:', h)
print()
print('test RSA encode & decode with normal way####')
m = 88888888
c = KEY.encode(m)
print('    ciphertext is:', c)
print('    does it decode successfully?')
print('----', KEY.decode(c) == m)
print()
print('test RSA decode with sliding windows####')
print('here we use ciphertext above############')
M = SWdecode(h, c, KEY.N)
print('    sliding windows method result:')
print('----', M)




