import Linder_Peikert_PKEscheme as LP
import numpy as np
import matplotlib.pyplot as plt
from time import time_ns
from pprint import pprint

print("Program Start-------------\n")

run = 100 # bits = run
#m = 1
m = np.array([np.random.randint(2) for _ in range(run)])
PK = []
SK = []
Cipher = []
Plain = []
Enc_time = np.array([])

for i in range(run):
	# Key Generate
	a = LP.LPscheme(100, 100, 1023)
	pk, sk = a.KeyGen()
	PK.append(pk)
	SK.append(sk)

	# Encapsulation
	start = time_ns()
	cipher = a.Enc(pk, m[i])
	end = time_ns()
	Enc_time = np.append(Enc_time, (end-start))
	Cipher.append(cipher)

	# Decapsulation
	plain = a.Dec(sk, cipher)
	Plain.append(plain)

print("Is decapsulation successful?\t", np.all(Plain==m))
if not np.all(Plain==m):
	print("How many Fails?\t", np.count_nonzero((Plain==m)==False))
print("\nProgram End---------------")

