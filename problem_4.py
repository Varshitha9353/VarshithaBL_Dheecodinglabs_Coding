#Sum pairs

def sum(arr):
    target=5
    list=[]
    n=len(arr)
    for i in range(0,n):
        for j in range(1,n):
            res=arr[i]+arr[j]
            if(res==target):
                list.append(arr[i])
                list.append(arr[j])
    return list

arr=[1, 2, 3, 4, 5]
print(sum(arr))