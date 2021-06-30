print()
e = 7
d = 103
n = 143
L = 3

d_bin = bin(d)[2:]
print('private key is: ', d_bin) # 1100111

m = 21
c = pow(m, e, n)
print('ciphertext is: ', c)
print('    which in binary is: ', bin(c)[2:])
print()
print('does it decrypt successfully?')
print('----', pow(c, d, n) == m)

print('check sliding window for L = %d#####' % L)

h = []

# sliding windows
# 110, 0, 111

i = 0
zi = 0
while i < len(d_bin):
	if d_bin[i] == '1':
		if not zi == 0:
			h.append('0' * zi)
			zi = 0
		h.append(d_bin[i:i+L])
		i += L
	else:
		zi += 1
		i += 1

print('sliding windows are: ', h)
print()

# doing decryption

M = 1
for i in range(len(h)):
	M = pow(M, 2**len(h[i]))
	if not int(h[i], 2) == 0:
		M = M * c**int(h[i], 2)
		M = M % n

print('the decrypt result is: ', M)
print()




