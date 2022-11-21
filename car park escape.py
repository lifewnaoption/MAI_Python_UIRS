def escape(carpark):
    floor, car = next((floor, car)
                      for floor, f in enumerate(carpark)
                      for car, c in enumerate(f) if c == 2)
    route, carpark[-1][-1] = [], 1
    while floor < len(carpark) - 1 or carpark[floor][car] != 1:
        start = floor, car
        while floor < len(carpark) - 1 and carpark[floor][car] == 1:
            floor += 1
        if floor > start[0]: route.append('D%d' % (floor - start[0]))
        car = carpark[floor].index(1)
        if car > start[1]: route.append('R%d' % (car - start[1]))
        if car < start[1]: route.append('L%d' % (start[1] - car))
    return route