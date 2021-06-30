from time import time_ns
from pprint import pprint

def comp(a, b):
	for i in range(len(a)):
		if a[-1+i] != b[-1+i]:
			return False
	return True

def login(passwd):
	secret = 111 
	bs = bin(secret)[2:]
	bp = bin(passwd)[2:]
	if len(bs) < 8:
		p = 8 - len(bs)
		bs = '0' * p + bs
	if len(bp) < 8:
		p = 8 - len(bp)
		bp = '0' * p + bp
	if comp(bs, bp):
		return 'User has access'
	return 'User does not have access'

count = {}
for c in range(20):
	results = {key: 0 for key in range(256)}
	for _ in range(1000):
		for i in range(256):
			start = time_ns()
			login(i)
			end = time_ns()
			results[i] += end-start
	s = sorted(results, key=results.get, reverse=True)[:5]
	#pprint(f'The probable secret is: {s}')
	for v in s:
		if v in count:
			count[v] += 1
		else:
			count[v] = 1
pprint(count)
pprint(sorted(count, key=count.get, reverse=True))




