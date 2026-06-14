def leaders(self, arr):
        l=[]
        m=float('-inf') 
        for i in range(len(arr)-1,-1,-1):
            if(arr[i] >=m):
                l.append(arr[i])
                m=arr[i]
        l.reverse()  
        return l