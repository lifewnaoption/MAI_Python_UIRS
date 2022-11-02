def pluck(objs, name): 
    coll = []
    for i in range(len(objs)):
        coll.append(objs[i].get(name, None))
    return coll

print(pluck([{'a':1, 'b':2, 'c': 3}, {'a':4, 'b':5, 'c': 6}, {'a':7, 'b':8, 'c': 9}, {'a':10, 'b':11}], 'a'))
