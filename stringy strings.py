def stringy(size):
    finalStr = '0'
    for i in range(size):
        if finalStr[i] == '0':
            finalStr += '1'
        if finalStr[i] == '1':
            finalStr += '0'
    return(finalStr[1:])

print(stringy(10))