arr=[1,10,20,0,59,63,0,88,0]
# display a orginal array
for i in range(len(arr)):
    print(arr[i])

temp=0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

print()

for i in range(0,len(arr)):
    print(arr[i])