def MaxLen(A,n,Sum):
    max_len = 0
    d= {}
    curr_sum =0
    ending_index = -1
    for x in range(n):
        curr_sum +=A[x]
        if curr_sum-Sum in d:
            if max_len<x-d[curr_sum-Sum]:
                max_len = x-d[curr_sum-Sum]
                ending_index = x
        if curr_sum not in d:
            d[curr_sum] =x
    return(max_len,ending_index-max_len+1,ending_index)

if __name__ == '__main__':
    A = [5, 6, -5, 5, 3, 5, 3, -2, 0]
    Sum = 8
    n = len(A)
    print(MaxLen(A,n,Sum))