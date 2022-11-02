def find_needle(haystack):
    regul = haystack.index('needle')
    return (f'found the needle at position {regul}')

find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])