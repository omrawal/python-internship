n=int(input("Enter the order\n"))
print("the magic sum is %d\n"%(n*(n**2+1)//2) )
mat=[]
for k in range(n):
    mat.append([])
for k in range(n):
    for l in range(n):
        mat[k].append(l)
        mat[k][l]=0
    i=n//2
    j=n-1
mat[i][j]=1
for a in range (2,n**2+1):
    i=i-1
    j=j+1
    if (i == -1 and j != n):
            i=n-1
    elif (j == n and i != -1):
            j=0
    elif (i == -1 and j == n):
            i = 0
            j = n - 2
    if (mat[i][j]!=0):
            i=i+1
            j=j-2
    mat[i][j]=a
print("Magic square is\n")
for i in range (n):
        print(mat[i])