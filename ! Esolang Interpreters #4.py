from collections import defaultdict

def find(s, open, close):
    stack = 0
    for i,c in enumerate(s, 1):
        if c == open: stack += 1
        elif c == close:
            if stack == 0: return i
            stack -= 1
    raise ErrorBrackets

def boolfuck(code, input=""):
    input = [int(b) for c in reversed(input) for b in f"{ord(c):08b}"]
    i, j, D, res = 0, 0, defaultdict(int), []
    while i < len(code):
        if   code[i] == '+': D[j] = 1 - D[j]
        elif code[i] == ',': D[j] = input.pop() if input else 0
        elif code[i] == ';': res.append(D[j])
        elif code[i] == '<': j -= 1
        elif code[i] == '>': j += 1
        elif code[i] == '[' and D[j] == 0: i += find(code[i+1:], '[', ']')
        elif code[i] == ']' and D[j] == 1: i -= find(code[i-1::-1], ']', '[')
        i += 1
    return ''.join(chr(sum(b * 2**j for j,b in enumerate(res[i:i+8]))) for i in range(0, len(res), 8))