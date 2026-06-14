def findTwoElement(self, arr):
        # code here
        mis=0
        seen=set()
        d=0
        for i in range(0,len(arr)):
            if(arr[i]  in seen):
                d=arr[i]
            else:
                seen.add(arr[i])
        for i in range(1,len(arr)+1):
            if(i not in seen):
                mis=i
                break
        return [d,mis]