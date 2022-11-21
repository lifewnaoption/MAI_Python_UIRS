def pattern(n):
    if n < 1:
        return ''
    walkList = ['1','2','3','4','5','6','7','8','9','0']
    fillList = ['1']
    
    #заношу числа в массив
    for i in range(0,n-1,1):
        fillList.append('')
        j=0
        k=0
        
        while j <= i:
            fillList[-1] += walkList[k]
            j += 1
            k += 1
            if k > 9:
                k=0
                
        while j >= 0:   
            fillList[-1] += walkList[k]
            j -= 1
            k -= 1
            if k < 0:
                k=9
    #print(fillList)
    
    # вставляю пробелы
    for i in range(len(fillList)):
        j=0
        while j <= (len(fillList) - i - 2 ):
            fillList[i] = ' ' + fillList[i] + ' '
            j += 1
    #print(fillList)
    
    # отзеркаливаю верхнюю часть алмаза
    for i in range(len(fillList)-2,-1,-1):
        fillList.append(fillList[i])
        
        
    # обьединяю элементы массива в одну строку
    res = '\n'.join(fillList)
    print(res)

    
pattern(0)