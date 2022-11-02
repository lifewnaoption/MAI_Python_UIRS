def century(year):
    if (year % 100) > 0:
        return ((year // 100) + 1)
    else:
        return (year // 100)
    
print(century(1901))