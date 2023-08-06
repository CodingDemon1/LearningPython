#Bubble Sort

def bubble_sort(ar,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if ar[j]<ar[i]:
                temp = ar[j]
                ar[j] = ar[i]
                ar[i] = temp
    return ar
    
ar = [789,23,65,23,86,23765,26]

sorted = bubble_sort(ar,len(ar))

print(sorted)