def rightMost(a,b):
    a = bin(a)[2:]
    b= bin(b)[2:]
    for x in range(min(len(a),len(b))-1,-1,-1):
        if int(a[x])&int(b[x]):
            pass
        else:
            return x

a = 100
b=140
print(rightMost(a,b))