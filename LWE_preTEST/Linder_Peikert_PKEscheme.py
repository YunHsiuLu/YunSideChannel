import numpy as np

class LPscheme:
    def __init__(self, M=20, N=20, q=97):
        self.debug = False
        self.M = M
        self.N = N
        self.q = q
        
        # set random seed
        self.__s_A  = np.random.randint(0, 1000)
        self.__s_e  = np.random.randint(0, 1000)
        self.__s_s  = np.random.randint(0, 1000)
        self.__s_s1 = np.random.randint(0, 1000)
        self.__s_e1 = np.random.randint(0, 1000)
        self.__s_e2 = np.random.randint(0, 1000)
        
    def KeyGen(self):
        np.random.seed(self.__s_A)
        A = np.array([[np.random.randint(0, self.q) for _ in range(self.N)] for __ in range(self.M)])
        np.random.seed(self.__s_e)
        #e = np.random.binomial(n=2, p=0.5, size=self.M)-1
        e = [np.random.randint(2) for _ in range(self.M)]
        np.random.seed(self.__s_s)
        #s = np.random.binomial(n=2, p=0.5, size=self.N)-1
        s = [np.random.randint(2) for _ in range(self.N)]
        if np.all(s==0):
            np.random.seed(self.__s_s + self.__s_A)
            s = np.random.binomial(n=2, p=0.5, size=self.N)-1
        if self.debug:
            print("A = \n", A)
            print("error = \n", e)
            print("s = \n", s)
        # Public key b ---->
        b = (np.matmul(A, s) + e) % self.q
        return (A, b), s
    
    def encode(self, x): # x in {0, 1}
        return (self.q//2)*x

    def decode(self, c_v): # c_v is c-v
        return abs(int(round(c_v/(self.q//2))))
    
    def Enc(self, pk, m): # public key = (A,b)  message m in {0, 1}
        np.random.seed(self.__s_s1)
        #s1 = np.random.binomial(n=2, p=0.5, size=self.M)-1
        s1 = [np.random.randint(2) for _ in range(self.N)]
        np.random.seed(self.__s_e1)
        #e1 = np.random.binomial(n=2, p=0.5, size=self.N)-1
        e1 = [np.random.randint(2) for _ in range(self.N)]
        np.random.seed(self.__s_e2)
        #e2 = np.random.binomial(n=2, p=0.5)-1
        e2 = np.random.randint(2)
        
        A = pk[0]
        b = pk[1]
        b1 = (np.matmul(s1, A) + e1) % self.q

        # inner product <r, b>
        v1 = (np.inner(s1, b) + e2) % self.q
        c = (self.encode(m) + v1) % self.q

        if self.debug:
            print(s1, e1, e2)
            print("b1 = \n", b1)
            print("v1 = \n", v1)
        return (b1, c)
    
    def Dec(self, s, cipher): # s = secret key, cipher = (b1, c)
        b1 = cipher[0]
        c  = cipher[1]
        v = np.inner(b1, s) % self.q
        if self.debug:
            print(v)
        return self.decode(c-v)
