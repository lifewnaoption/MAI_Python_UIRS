def compose(s1, s2):
    s1 = s1.split("\n")
    s2 = s2.split("\n")[::-1]
    
    n = len(s1)
    out = []
    
    for i in range(n):
        out.append(s1[i][:i+1] + s2[i][:(n-i)])
    
    return "\n".join(out)



print(compose("byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB"))