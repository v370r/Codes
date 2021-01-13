def RemoveDuplicates(A):
    hash1 = [0]*(26)
    for x in range(len(A)):
        if hash1[ord(A[x])-ord("A")]==0:
            hash1[ord(A[x])-ord("A")]=1
            print(A[x],end="")
    return 
A = "AABBACXZZ"
RemoveDuplicates(A)