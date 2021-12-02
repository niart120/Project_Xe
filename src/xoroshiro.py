import secrets

class Xoroshiro:
    def __init__(self, s0=secrets.randbits(64),s1=secrets.randbits(64)):
        #self.seed = [seed, 0x82A2B175229D6A5B]
        self.seed = [s0,s1]

    @staticmethod
    def rotl(x, k):
        return ((x << k) | (x >> (64 - k))) & 0xFFFFFFFFFFFFFFFF

    @staticmethod
    def nextP2(x):
        x -= 1
        for i in range(6):
            x |= x >> (1<<i)
        return x

    def next(self):
        s0, s1 = self.seed
        result = (s0 + s1) & 0xFFFFFFFFFFFFFFFF

        s1 ^= s0
        self.seed[0] = self.rotl(s0, 24) ^ s1 ^ ((s1 << 16) & 0xFFFFFFFFFFFFFFFF)
        self.seed[1] = self.rotl(s1, 37)

        return result

    def get_state(self):
        return self.seed[0],self.seed[1]
        
    def nextInt(self, num = 0xFFFFFFFF):
        num2 = self.nextP2(num)
        s = self.next() & num2
        while s >= num:
            s = self.next() & num2
        return s
    