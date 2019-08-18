duplicates=[2,2,5,5,8,8,7,7,4,4,1,1]
def Remove(duplicates):
    L1=[]
    L2=[]
    for num in duplicates:
        if num not in L1:
            L1.append(num)
        else:
            L2.append(num)

    print(sorted(L1))
    print(sorted(L2))

(Remove(duplicates))