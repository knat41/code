l = [7,5,1,6,4,3]
for i in range(len(l)-1,0,-1):
    for j in range(0,i):
        if l[j] > l[j+1]:
            tmp = l[j]
            l[j] = l[j+1]
            l[j+1] = tmp
    print(l)
