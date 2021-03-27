def prime(num):
    i=1
    sum=0
    while i<num:
        if num%i==0:
            print(i)
            sum=sum+num
            print(sum)
        i=i+1
    if sum==num:
        print(sum,"prime number")
    else:
        print("not prime number")
prime(int(input("enter the number")))

