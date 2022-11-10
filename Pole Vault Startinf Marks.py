def starting_mark(height):
    dx = (10.67 - 9.45) / (1.83 - 1.52)
    print('Смещение на один сантиметр (см): ', dx)
    res = round((height - 1.52) * dx, 2) + 9.45
    return round(res,2)