def money_value(s):
    s = s.replace(' ', '')
    s = s.replace('$' , '')

    if s == '':
        return 0.0

    if s[0] == '.':
        s = '0' + s

    if s[0] == '0' and s[1] == '0':
        s = s.replace('0', '')

    if len(s) < 4:
        if '.' not in s:
            s += '.'
        start_length = 0
        zero_len = 4 - len(s)

        while start_length < zero_len:
            s += '0'
            start_length += 1    

    return float(s)
