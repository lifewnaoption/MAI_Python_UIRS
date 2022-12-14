def match(s):
    Match={'A':'B','B':'A','X':'Y','Y':'X'}
    n=len(s)
    f=[[0]*n for i in range(n+1)]
    for i in range(n-1,-1,-1):
        t=Match[s[i]]
        g=[]
        for j in range(i+1,n):
            c=0
            f[i][j]=f[i+1][j]
            g.append(j)
            for k in g:
                if s[k]==t:
                    if  f[i][j]<f[i+1][k-1]+f[k+1][j]+1:
                        f[i][j]=f[i+1][k-1]+f[k+1][j]+1
                        c=k
            if c!=j:g.pop()
    return f[0][n-1]