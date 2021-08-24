def ecc_add(ecc, P, Q=None):
	if Q == None:
		x = P[0]
		y = P[1]
		temp = 3*pow(x,2) + ecc.a
		if temp > 0:
			temp = temp % ecc.p
			s = 1
			while (2*y*s) % ecc.p != temp:
				s += 1
			xr = (pow(s,2) - 2*x) % ecc.p
			yr = (s*(x-xr) - y) % ecc.p
			return [xr, yr]
		elif temp < 0:
			temp = abs(temp) % ecc.p
			s = 1
			while (2*y*s) % ecc.p != temp:
				s += 1
			s = -s % ecc.p
			xr = (pow(s,2) - 2*x) % ecc.p
			yr = (s*(x-xr) - y) % ecc.p
			return [xr, yr]
		else:
			s = 0
			xr = (pow(s,2) - 2*x) % ecc.p
			yr = (s*(x-xr) - y) % ecc.p
			return [xr, yr]
	elif (P[0] == Q[0]) and ((P[1] + Q[1]) % ecc.p == 0):
		return [None, None]
	else:
		xp = P[0]
		yp = P[1]
		xq = Q[0]
		yq = Q[1]
		temp = yp - yq
		if temp > 0:
			temp = temp % ecc.p
			s = 1
			while ((xp - xq)*s) % ecc.p != temp:
				s += 1
			xr = (pow(s,2) - xp - xq) % ecc.p
			yr = (s*(xp-xr) - yp) % ecc.p
			return [xr, yr]
		elif temp < 0:
			temp = abs(temp) % ecc.p
			s = 1
			while ((xp - xq)*s) % ecc.p != temp:
				s += 1
			s = -s % ecc.p
			xr = (pow(s,2) - xp - xq) % ecc.p
			yr = (s*(xp-xr) - yp) % ecc.p
			return [xr, yr]
		else:
			s = 0
			xr = (pow(s,2) - xp - xq) % ecc.p
			yr = (s*(xp-xr) - yp) % ecc.p
			return [xr, yr]

def Subgroup(ecc, no):
	no = no % len(ecc.G)
	if no == 0:
		print("You choose infinite point!")
		return 0
	else:
		g = []
		g.append([None, None])
		g.append(ecc.G[no])
		g.append(ecc_add(ecc, g[1]))
		while 1:
			g_next = ecc_add(ecc, g[1], g[-1])
			if g_next == [None, None]:
				break
			g.append(g_next)
		return g

class ECC():
	def __init__(self, p, a, b):
		flag = False if (4 * a**3 - 27 * b**2 == 0) else True
		self.p = p
		self.a = a
		self.b = b
		x = list(range(self.p))
		y = list(range(self.p))
		self.G = []
		self.G.append([None, None])
		for i in x:
			for j in y:
				if (pow(i,3) + self.a*i + self.b - pow(j,2)) % self.p == 0:
					(self.G).append([i,j])
	
	def print_curve(self):
		string = "y^2 = x^3 + " + self.a * "x + " + str(self.b)
		print(string)

	def group_size(self):
		return len(self.G) # include inf


ECC_a = ECC(17, 0, 7)
ECC_a.print_curve()
print("Whole group size (include inf point): %d" % (ECC_a.group_size()))
print("Whole group:")
print(ECC_a.G)
g = Subgroup(ECC_a, 17)
print("Whole sub-group size (include inf point): %d" % (len(g)))
print("Subgroup:")
for p in range(len(g)):
	print("%d * g\t= " % (p), g[p])


			

