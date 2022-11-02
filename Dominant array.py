def solve(arr):
    size = len(arr) 
    lisso = []
    max_from_right = arr[size-1]  
    lisso.append(max_from_right) 
    for i in range( size-2, -1, -1):       
        if max_from_right < arr[i]:       
            lisso.append(arr[i])
            max_from_right = arr[i]
    return(lisso[::-1])
# Driver function
arr=[75, 56, 13, 55]
print(printLeaders(arr))
 