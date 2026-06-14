def findFloor( arr, x):
        # code here
        a=-1
        for i in range(len(arr)):
            if arr[i]<=x:
                a=i
            else:
                break
        return a

# floor is number that is largest index wise which is less than or equal to that target number