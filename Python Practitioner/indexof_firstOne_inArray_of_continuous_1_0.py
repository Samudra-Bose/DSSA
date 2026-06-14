def transitionPoint(self, arr): 
        # Code here
        for i in range(0,len(arr)):
            if arr[i]==1:
                return i
        return -1