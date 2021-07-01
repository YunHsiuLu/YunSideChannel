def SlidingWindows(d: int, L: int):
	d_bin = bin(d)[2:]
	h = []
	# sliding windows
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
	return h

def SWdecode(h: list, c: int, n: int):
	M = 1
	for i in range(len(h)):
		M = pow(M, 2**len(h[i]), n)
		if not int(h[i], 2) == 0:
			M = (M * pow(c, int(h[i], 2))) % n
	return M





