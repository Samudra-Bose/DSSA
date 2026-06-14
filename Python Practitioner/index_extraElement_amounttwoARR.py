def findExtra(self,a,b):
        x=sum(a)-sum(b)
        for i in range(0,len(a)):
            if(a[i]==x):
                return i