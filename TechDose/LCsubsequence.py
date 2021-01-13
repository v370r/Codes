def LCsubstr(X,Y):
	m = len(X)
	n = len(Y)
	result= 0
	end =0
	dp = [[0 for x in range(m)] for y in range(2)]
	currRow = 0
	for i in range(0,m+1):
		for j in range(0,n+1):
			if i==0 or j==0:
				length[currRow][j]=0
			elif (X[i-1]==Y[i-1]):
				len



# Driver program 
X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
m = len(X) 
n = len(Y) 
lcs(X, Y, m, n) 
