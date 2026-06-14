def findDuplicates(self, arr):
        # code here
        a=[]
        seen=set()
        for i in range(0,len(arr)):
            if(arr[i] not in seen):
                seen.add(arr[i])
            else:
                a.append(arr[i])
                
        return a