def isLucky(n):
    next_position = n
    if isLucky.counter >n:
        return 1
    if n%isLucky.counter ==0:
        return 0
    next_position = next_position-next_position//isLucky.counter
    isLucky.counter = isLucky.counter +1
    return isLucky(next_position)

isLucky.counter =2 # satatic variable
x = 5
if isLucky(x):
    print(x," is a lucky number")
else:
    print(x,"not a lucky number") 