 # 6. **Missing Number**: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
 #     - *Input*: [3, 0, 1]
 #     - *Output*: "2"

ar = [3,0,1]
ar.sort()

till = ar[-1]

for i in range(till):
    if ar[i] != i+1:
        ans = i+1
    

print(ans)