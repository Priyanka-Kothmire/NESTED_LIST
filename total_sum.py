number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
i=0
a=[ ]
while i<len(n):
    if n[i]+n(i+1)==number:
        a.append(n)
    i=i+1
print(a)