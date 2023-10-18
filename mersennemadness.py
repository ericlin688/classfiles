class pnf3000:
    
    def __init__(self,np):
        self.np = np
        self.plist = self.findprimes(np)
        return

    def findprimes(self,np = 100):
        primes = [2]
        n=3
        while len(primes)<np:
            isprime = True
            for p in primes:
                r = n%p
                if r == 0:
                    isprime = False
                    break

            if isprime:
                primes.append(n)
            n += 1
        return primes
    
    def mersenne(self,n,size):
        if size > self.np:
            print('{} is larger than {}. Please pick an appropriate size.'.format(size,self.np))
        else:
            mlist = []
            for i in range(size):
                m = n**self.plist[i]-1
                mlist.append(m)
        return mlist

bob = pnf3000(1000)
print(bob.mersenne(2,30))