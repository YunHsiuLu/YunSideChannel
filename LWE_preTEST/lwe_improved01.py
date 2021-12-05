import Linder_Peikert_PKEscheme as LP
import numpy as np
import matplotlib.pyplot as plt
from time import time_ns
from utility import *

print("Program Start---------------\n")
print("Run LWE with same key\n")

for f in range(8):
	Cipher = []
	Plain = []
	Enc_0_time = []
	Dec_0_time = []
	Enc_1_time = []
	Dec_1_time = []

	a = LP.LPscheme(100, 100, 1023)
	pk, sk = a.KeyGen()
	print("Secret key:\n", sk)
	print("Secret key distance square: ", vec_dis(sk))
	print("Public key A:\n", pk[0])
	print("Public key distance: ", mat_dis(pk[0]))
	print("Public key b:\n", pk[1])
	print("Public key distance square: ", vec_dis(pk[1]))
	run = 200
	x = np.arange(0, run)

	for _ in range(run+10):
		# 0's enc and dec time
		start = time_ns()
		cipher = a.Enc(pk, 0)
		end = time_ns()
		Enc_0_time.append(end - start)

		start = time_ns()
		plain = a.Dec(sk, cipher)
		end = time_ns()
		Dec_0_time.append(end - start)

		# 1's enc and dec time
		start = time_ns()
		cipher = a.Enc(pk, 1)
		end = time_ns()
		Enc_1_time.append(end - start)

		start = time_ns()
		plain = a.Dec(sk, cipher)
		end = time_ns()
		Dec_1_time.append(end - start)

	Enc_0_time = data_improved(Enc_0_time[10:], 800000)
	Dec_0_time = data_improved(Dec_0_time[10:], 15000)
	Enc_1_time = data_improved(Enc_1_time[10:], 800000)
	Dec_1_time = data_improved(Dec_1_time[10:], 15000)

	Enc_0_time, Enc_1_time = align_list(Enc_0_time, Enc_1_time)
	Dec_0_time, Dec_1_time = align_list(Dec_0_time, Dec_1_time)
	print("\n\tEnc time length: %d, %d" % (len(Enc_0_time), len(Enc_1_time)))
	print("\tDec time length: %d, %d\n" % (len(Dec_0_time), len(Dec_1_time)))

	Enc_0_time_ave = sum(Enc_0_time)/len(Enc_0_time)
	Dec_0_time_ave = sum(Dec_0_time)/len(Dec_0_time)
	Enc_1_time_ave = sum(Enc_1_time)/len(Enc_1_time)
	Dec_1_time_ave = sum(Dec_1_time)/len(Dec_1_time)
	print("\t0's enc and dec time: %.2f and %.2f\n" % (Enc_0_time_ave, Dec_0_time_ave))
	print("\t1's enc and dec time: %.2f and %.2f\n" % (Enc_1_time_ave, Dec_1_time_ave))

	Enc_0_time = np.array(Enc_0_time)
	Dec_0_time = np.array(Dec_0_time)
	Enc_1_time = np.array(Enc_1_time)
	Dec_1_time = np.array(Dec_1_time)
	Enc_len = len(Enc_0_time) # same as Enc_1_time
	Dec_len = len(Dec_0_time) # same as Dec_1_time

	fig, ax = plt.subplots(2,1,figsize=(10,8))
	fig.suptitle("Run with the same key: Run %d" % (f+1), fontsize=16)
	textstr1 = "\n".join((
		"Enc 0's average time: %.2f" % (Enc_0_time_ave),
		"Enc 1's average time: %.2f" % (Enc_1_time_ave)))
	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

	ax[0].plot(x[:Enc_len], Enc_0_time, 'k-')
	ax[0].plot(x[:Enc_len], Enc_1_time, 'r-')
	ax[0].set_ylim(top=800000)
	ax[0].legend(["Enc 0's time", "Enc 1's time"], loc='upper right')
	ax[0].text(0.62, 0.75, textstr1, transform=ax[0].transAxes, fontsize=12, verticalalignment='top', bbox=props)

	#fig2, ax2 = plt.subplots(1,1,figsize=(10,6))
	textstr2 = "\n".join((
		"Dec 0's average time: %.2f" % (Dec_0_time_ave),
		"Dec 1's average time: %.2f" % (Dec_1_time_ave)))

	ax[1].plot(x[:Dec_len], Dec_0_time, 'k-')
	ax[1].plot(x[:Dec_len], Dec_1_time, 'r-')
	ax[1].set_ylim(top=16000)
	ax[1].legend(["Dec 0's time", "Dec 1's time"], loc='upper right')
	ax[1].text(0.62, 0.75, textstr2, transform=ax[1].transAxes, fontsize=12, verticalalignment='top', bbox=props)
	#plt.show()
	fig.savefig("Run_SameKey_fig%d_improved.png" % (f+1))

