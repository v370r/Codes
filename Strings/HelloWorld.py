def Print(n):
    if n==0:
        return 
    else:
        print("Hello World")
        return(Print(n-1))
print(Print(5))
print("HelloWorld \n"*5)