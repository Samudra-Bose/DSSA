def getSecondLargest(self, arr):
        # Code Here
        a=max(arr)
        b=[x for x in arr if x!=a]
        if not b:
            return -1
        return max(b)