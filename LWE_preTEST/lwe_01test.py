import Linder_Peikert_PKEscheme as LP
import numpy as np
import matplotlib.pyplot as plt
from time import time_ns
from utility import *

print("Program Start---------------\n")
print("Run LWE with same key\n")

Cipher = []
Plain = []
Enc_0_time = []
Dec_0_time = []
Enc_1_time = []
Dec_1_time = []

a = LP.LPscheme(100, 100, 4097)
pk, sk = a.KeyGen()
print("Secret key:\n", sk)
print("Secret key distance square: ", vec_dis(sk))
print("Public key A:\n", pk[0])
print("Public key distance: ", mat_dis(pk[0]))
print("Public key b:\n", pk[1])
print("Public key distance square: ", vec_dis(pk[1]))
run = 500
x = np.arange(0, run)

# 0's enc and dec time
for _ in range(run+10):
	start = time_ns()
	cipher = a.Enc(pk, 0)
	end = time_ns()
	Enc_0_time.append(end - start)

	start = time_ns()
	plain = a.Dec(sk, cipher)
	end = time_ns()
	Dec_0_time.append(end - start)
Enc_0_time = Enc_0_time[10:]
Dec_0_time = Dec_0_time[10:]
Enc_0_time_ave = sum(Enc_0_time)/len(Enc_0_time)
Dec_0_time_ave = sum(Dec_0_time)/len(Dec_0_time)

print("\t0's enc and dec time: %.2f and %.2f\n" % (Enc_0_time_ave, Dec_0_time_ave))

# 1's enc and dec time
for _ in range(run+10):
	start = time_ns()
	cipher = a.Enc(pk, 1)
	end = time_ns()
	Enc_1_time.append(end - start)

	start = time_ns()
	plain = a.Dec(sk, cipher)
	end = time_ns()
	Dec_1_time.append(end - start)
Enc_1_time = Enc_1_time[10:]
Dec_1_time = Dec_1_time[10:]
Enc_1_time_ave = sum(Enc_1_time)/len(Enc_1_time)
Dec_1_time_ave = sum(Dec_1_time)/len(Dec_1_time)

print("\t1's enc and dec time: %.2f and %.2f\n" % (Enc_1_time_ave, Dec_1_time_ave))

Enc_0_time = np.array(Enc_0_time)
Dec_0_time = np.array(Dec_0_time)
Enc_1_time = np.array(Enc_1_time)
Dec_1_time = np.array(Dec_1_time)

fig1, ax1 = plt.subplots(1,1,figsize=(10,6))
textstr1 = "\n".join((
	"Enc 0's average time: %.2f" % (Enc_0_time_ave),
	"Enc 1's average time: %.2f" % (Enc_1_time_ave)))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

ax1.plot(x, Enc_0_time, 'k-')
ax1.plot(x, Enc_1_time, 'r-')
#ax1.set_ylim(25000, 40000)
ax1.legend(["Enc 0's time", "Enc 1's time"], loc='upper right')
ax1.text(0.6, 0.8, textstr1, transform=ax1.transAxes, fontsize=12,
	verticalalignment='top', bbox=props)

#fig.savefig("")
fig2, ax2 = plt.subplots(1,1,figsize=(10,6))
textstr2 = "\n".join((
	"Dec 0's average time: %.2f" % (Dec_0_time_ave),
	"Dec 1's average time: %.2f" % (Dec_1_time_ave)))

ax2.plot(x, Dec_0_time, 'k-')
ax2.plot(x, Dec_1_time, 'r-')
#ax2.set_ylim(3000, 5000)
ax2.legend(["Dec 0's time", "Dec 1's time"], loc='upper right')
ax2.text(0.6, 0.8, textstr2, transform=ax2.transAxes, fontsize=12,
	verticalalignment='top', bbox=props)
plt.show()


