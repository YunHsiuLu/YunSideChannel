import Linder_Peikert_PKEscheme as LP

a = LP.LPscheme(7, 4, 13)
m = 1
pk, sk = a.KeyGen()
cipher = a.Enc(pk, m)
print(cipher)
plain = a.Dec(sk, cipher)
print(plain)