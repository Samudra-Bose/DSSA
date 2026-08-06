a=29
flag=0
for i in range(2,a//2):
    if(a%i==0):
        flag=1

if(flag):
    print("not prime")
else:
    print("Prime")

