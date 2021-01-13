class AreaHist:
    @staticmethod
    def Bruteforce(A):
        Max_Area = 0
        for i in range(0,len(A)):
            min_height = A[i]
            for j in range(i,len(A)):
                min_height =min(min_height,A[j])
                curr_Area = (j-i+1)*min_height
                Max_Area =max(curr_Area,Max_Area)
        return(Max_Area)
        

A = [4,1,3,2,3]
area = AreaHist.Bruteforce(A)
print(area)
