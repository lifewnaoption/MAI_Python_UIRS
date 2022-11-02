def compare(s1,s2):
    compOne = 0
    compTwo = 0

    if s1 == None:
        s1 = ''
    if s2 == None:
        s2 = ''

    if s1.isalpha():
        for i in s1:
            compOne += ord(i.upper())

    if s2.isalpha():
        for i in s2:
            compTwo += ord(i.upper())

    if compOne == compTwo:
        return True
    else:
        return False

print(compare("AD", "BC"))

