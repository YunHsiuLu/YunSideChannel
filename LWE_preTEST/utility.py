from math import prod, sqrt

def vec_dis(v):
	t = 0
	for i in v:
		t += i*i
	return t

def mat_dis(m):
	t = []
	for i in m:
		t.append(vec_dis(i))
	return prod(t)**(1/len(t))

