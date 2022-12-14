position = [0,0]
direction = 0

def i_am_here(path):
    global position
    global direction
    i = 0
    while i < len(path):
        
        if path[i] == 'R' or path[i] == 'L':
            if direction > 1:
                direction -= 2
            else:
                direction += 2
        
        elif path[i] == 'r':            
            if direction == 3:
                direction = 0
            else:
                direction += 1
        
        elif path[i] == 'l':
            if direction == 0:
                direction = 3
            else:
                direction -= 1
        
        else:
            steps=path[i]
            while i < len(path)-1 and path[i+1].isdigit():
                steps += path[i+1]
                i += 1
            doMove(position, direction, int(steps))
    
        i += 1
            
    return position
    
def doMove(position, direction, steps):
    if direction == 0:
        position[0] -= steps
    if direction == 1:
        position[1] += steps
    if direction == 2:
        position[0] += steps
    if direction == 3:
        position[1] -= steps