
 
 
def getPairsCount(arr, n, sum):
 
    count = 0 
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j+1,n):
                if arr[i] + arr[j]+arr[k] <sum:
                    count += 1
                    print(arr[i],arr[j],arr[k])
 
    return count
 
 
# Driver function
arr = [-1,0,2,3]
n = len(arr)
sum = 3
print("Count of pairs is",
      getPairsCount(arr, n, sum))

arr=[-1,4,2,1,3]
n=len(arr)
sum=5
print("Count of pairs is",
      getPairsCount(arr,n,sum))