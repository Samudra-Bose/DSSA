def isPrime(self, n):
        # code here
        f=0
        if n < 2:   
            return False
        for i in range(2,(n//2)+1):
            if i != n:
                if n%i==0:
                    f=1
                    break
        if f==0:
            return True
        else:
            return False