arr=[5,7,1,2,8,4,3]
target_value1=10
target_value2=19
count=0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target_value1:
            print(arr[i],arr[j])
            count+=1
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target_value2:
            print(arr[i],arr[j])
            count+=1
        


