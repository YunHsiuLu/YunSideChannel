print()
e = 7
d = 103
n = 143

d_bin = bin(d)[2:]
print('private key is: ', d_bin)

m = 21
c = pow(m, e, n)
print('ciphertext is: ', c)
print('    which in binary is: ', bin(c)[2:])
print()
print('does it decrypt successfully?')
print('----', pow(c, d, n) == m)

print('check sliding window for L = 1#####')

temp = c
for i in range(len(d_bin)):
	if i == 0:
		pass
	else:
		temp = pow(temp, 2)
		if d_bin[i] == '1':
			temp = temp * c
		temp = temp % n

print('---- the result is: ', temp)
print()

					