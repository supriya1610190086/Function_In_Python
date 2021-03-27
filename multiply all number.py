def mult(num):
    i=0
    sum=1
    while i<len(num):
        # k=num[i]
        sum=sum*num[i]
        i=i+1
    print(sum)
mult([8,2,3,-1,7])