def deleter(leest):
    collector = []
    for i in leest[::-1]:
        if i not in collector:
            collector.append(i)
    return(collector[::-1])

print(deleter([3,4,4,3,6,3]))