marks = [ 
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 
i=0
# sum=0
average=0
while i<len(marks):
    j=0
    k=0
    sum=0
    while j<len(marks[i]):
        k=k+(marks[i][j])
        j=j+1
    sum=sum+k
    # i+=1
    average=sum//len(marks[i])
    print(average)
    i=i+1