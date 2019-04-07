def insertion_sort(arr):
    for i in range(1,len(arr)):
        current_value = arr[i]
        position = i
        
        #sublist 
        while position > 0 and arr[position-1] > current_value:
            arr[position] = arr[position-1]
            position -= 1
            
        arr[position]=current_value
    return arr
    
print(insertion_sort([1,3,6,1,5,9]))
        
