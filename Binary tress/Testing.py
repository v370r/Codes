"""
from collections import Counter
def check(A):
    b = Counter(A)
    dict(sorted(x.items(), key=lambda item: item[1]))



A ="aaaabb,sdsffsfseaf"
A =list(A)
print(check(A))
"""
n  =10
for i in range(1,n+1):
    print("."*(n-i),end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()