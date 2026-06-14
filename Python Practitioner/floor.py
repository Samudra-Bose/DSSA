def findFloor(self, arr, x):
        # code here
        a=-1
        for i in range(len(arr)):
            if arr[i]<=x:
                a=i
            else:
                break
        return a