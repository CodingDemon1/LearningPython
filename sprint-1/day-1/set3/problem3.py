# 3. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"

li = [2, 7, 11, 15]

target = 9

for i in range(len(li)):
    j = len(li)-1
    while(j>i):
        if li[i]+li[j] == target:
            print([i,j])
