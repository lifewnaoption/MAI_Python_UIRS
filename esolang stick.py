def interpreter(tape):
    stack = [0]
    output = []
    skip = False
    skipi = 0
    i = 0
    while i < len(tape):
        c = tape[i]
        if skip:
            if c == "]":
                skip = False
        elif c == "]" and stack[-1]!=0:
            i = skipi
        elif c == "^":
            stack.pop()
        elif c == "!":
            stack.append(0)
        elif c == "+":
            stack[-1] = stack[-1]+1 if stack[-1]<255 else 0
        elif c == "-":
            stack[-1] = stack[-1]-1 if stack[-1]>0 else 255
        elif c == "*":
            output.append(stack[-1])
        elif c == "[" and stack[-1]==0:
            skip = True
            skipi = i
        i += 1
    out = "".join([chr(i) for i in output])
    return out