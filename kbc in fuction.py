print("WELCOME ......TO .......KBC")

def question():
    Question=["how many continentes are there?",
    "what is the capital of India?",
    "NG mei kaun se course padhey jata hai?"
    ]
    return Question
Question_list=question()

def option():
    option=[["Four","Nine","seven","Eight"],
    ["Chandigarh","Bhopal","chennai","Delhi"],
    ["Software engineering","Counseling","Tourism","Agriculture"]
    ]
    return option
option_list=option()

def solution():
    solution=[3,4,1]
    return solution
solution_list=solution()
def answer():
    answer=["3.seven","4.eight","2.bhopal","4.delhi","1.software engineering","3.tourism"]
    return answer
Ans = answer()
i=0
r=1
y=0
count=0
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
                print("right")
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
            print("your answer is correct")
        else:
            print("you are answer is wrong")
    else:
        print("error")
    i=i+1
    r+=1
    y+=1


