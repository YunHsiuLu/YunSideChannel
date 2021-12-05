from math import prod, sqrt

def vec_dis(v):
	t = 0
	for i in v:
		t += i*i
	return sqrt(t)

def mat_dis(m):
	t = []
	for i in m:
		t.append(vec_dis(i))
	return vec_dis(t)

def data_improved(data, upper_lim):
	tmp = data
	while (max(tmp) > upper_lim):
		tmp.remove(max(tmp))
	return tmp

def align_list(l1, l2):
	t1 = l1
	t2 = l2
	if len(t1) < len(t2):
		t2 = t2[:len(t1)]
	else:
		t1 = t1[:len(t2)]
	return t1, t2
