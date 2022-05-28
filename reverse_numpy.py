import numpy as np
n=int(input())
ls=list(map(int,input().split()))
arr=np.array(ls,dtype=float)
print(arr[::-1])