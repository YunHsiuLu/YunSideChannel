import Linder_Peikert_PKEscheme as LP
import numpy as np
import matplotlib.pyplot as plt
from time import time_ns
from pprint import pprint

print("Program Start---------------\n")
print("Run LWE with different key\n")

run = 100 # bits = run
#m = 1
m = np.array([np.random.randint(2) for _ in range(run)])
x = np.array(range(run))

PK = []
SK = []
Cipher = []
Plain = []
Enc_time = np.array([])
Dec_time = np.array([])

for i in range(run):
	# Key Generate
	a = LP.LPscheme(100, 100, 4097)
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
	start = time_ns()
	plain = a.Dec(sk, cipher)
	end = time_ns()
	Dec_time = np.append(Dec_time, (end-start))
	Plain.append(plain)

print("Is decapsulation successful?\t", np.all(Plain==m))
if not np.all(Plain==m):
	print("How many Fails?\t", np.count_nonzero((Plain==m)==False))

fig_enc, ax_enc = plt.subplots(1,1,figsize=(10, 6))
ax_enc.set_title("Encapsulation time (label with message)")
ax_enc.plot(x, Enc_time)
for i, txt in enumerate(m):
	ax_enc.annotate(txt, (x[i], Enc_time[i]))

fig_dec, ax_dec = plt.subplots(1,1,figsize=(10, 6))
ax_dec.set_title("Decapsulation time (label with message)")
ax_dec.plot(x, Dec_time)
for i, txt in enumerate(m):
	ax_dec.annotate(txt, (x[i], Dec_time[i]))
plt.show()

