def missingNum(self, arr):
        # code here
        a=sum(arr)
        b=((len(arr)+1)*(len(arr)+2))//2
        return b-a