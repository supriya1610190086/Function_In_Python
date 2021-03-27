def kbc(Question_list,option_list,solution_list,Ans,i,r,y,count,amount):
    print("welcome to kbc")
    while i<len(Question_list):
        i1=Question_list[i]
        print(i1)
        j=0
        k=i
        while j<len(option_list[i]):
            l=option_list[k][j]
            print(j+1,l)
            j=j+1
        Lifeline1=input("do you want 5050 lifeline")
        if Lifeline1=="yes":
            print("50-50")
            if count==0:
                print(Ans[y+i])
                print(Ans[y+r])
                n=int(input("enter answer"))
                if n==solution_list[i]:
                    print("your answer is correct",amount[i])
                else:
                    print("wrong")
                    break
                count+=1
            else:
                print("you already used lifeline")
                m=int(input("enter answer"))
                if m==solution_list[i]:
                    print("right")
                else:
                    print("wrong")
        elif Lifeline1=="no":
            u=int(input("choose the answer"))
            if u==solution_list[i]:
                print("your answer is correct",amount[i])
            else:
                print("you are answer is wrong")
        else:
            print("error")
        i=i+1
        r+=1
        y+=1
kbc(["how many continentes are there?",
"what is the capital of India?",
"NG mei kaun se course padhey jata hai?"
],[["Four","Nine","seven","Eight"],
["Chandigarh","Bhopal","chennai","Delhi"],
["Software engineering","Counseling","Tourism","Agriculture"]
],[3,4,1],["3.seven","4.eight","2.bhopal","4.delhi","1.software engineering","3.tourism"],0,1,0
,0,[1000,5000,10000])