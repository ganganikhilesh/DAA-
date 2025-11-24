def LCS(S1, S2):
    m = len(S1)
    n = len(S2)
    s=""
    dp = [[0]*(n+1) for x in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if S1[i-1]==S2[j-1]:
                if(s.count(S1[i-1])==0):
                    s+=S1[i-1]
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print("dp table is")
    for i in range(0,m+1):
        for j in range(0,n+1):
            print(dp[i][j],end=" ")
        print()
    print("The length of LCS is",dp[m][n])
    print("the LCS string is",s)
    return dp[m][n]

S1 = "AGGTAB"
S2 = "GXTXAYB"
l=(LCS(S1,S2))