#to find the second largest
    
def second(arr):  #this is a function to find the largest element
    length1=len(arr)    
    firstmaximum=-2**31  #by default considering first maximum as -2**31
    secmaximum=-2**31     #by default considering second maximum as -2**31
    for i in range(0,length1):  #traversing a array
        if (arr[i]>firstmaximum):  
            secmaximum=firstmaximum
            firstmaximum=arr[i]
        elif (firstmaximum!=arr[i] and secmaximum<arr[i]):
            secmaximum=arr[i]
    return firstmaximum,secmaximum

arr=[15,22,54,54]
res1,res2=second(arr)   #function call to a secondarray
print(f"the second largest is : {res2}")




