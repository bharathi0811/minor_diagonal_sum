R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries rowwise:")
for i in range(R):
    a =[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
i = 0
j = R-1
sum_=[]
while i<R and j>=0:
    sum_.append(matrix[i][j])
    i+=1
    j-=1
print(sum(sum_))