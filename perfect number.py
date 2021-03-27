def perfect(num):
    i=1
    sum=0
    while i<num:
        if num%i==0:
            print(i)
            sum=sum+i
        i=i+1
    if num==sum:
        print("perfect number",sum)
    else:
        print("not perfect number",sum)
perfect(int(input("enter the number")))