arr=[1,2,3,5,6,7,9]
n=len(arr)
for i in range(n-1):
    if (arr[i+1]-arr[i])!=1:
        print(arr[i]+1)