#Instead of converting 0 to N convert N to 0 and rprint steps stesp *2 or +1
def steps(N,count):
    if N&1:
        N -=1
        count +=1
        return(steps(N,count))
    else:
        if N>0:
            N //=2
            count +=1
            return(steps(N,count))
        if N==0:
            return(count)
print(steps(9,0))
    