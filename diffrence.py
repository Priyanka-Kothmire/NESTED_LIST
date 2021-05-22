list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7] 
list3=[ ]
i=0
# list3=[]
while i<len(list1):
    c=list1[i]
    if c not in list2:
        list3.append(c)
    i+=1
print(list3)
