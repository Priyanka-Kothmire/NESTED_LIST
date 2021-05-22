marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
] 
i=0
average=0 
while i<len(marks):
    j=0
    k=0
    sum=0
    while j<len(marks[i]):
        k=k+marks[i][j]
        j=j+1
    sum=sum+k
    average=sum//len(marks[i])
    print(average)
    i+=1

