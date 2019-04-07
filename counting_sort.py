def counting_sort(array,maxval):
    m = maxval + 1 # 0 dan başladığı için +1 gerekir.
    count = [0] * m # max sayı kadarlık bir dizi başlatırız.
    
    for a in array:
        count[a] +=1 
    
    i = 0
    for a in range(m):
        for s in range(count[a]):
            array[i] = a
            i = i+1
            
    return array
    
counting_sort([1,2,10,9,2,3,4,1,2,3], 10);
