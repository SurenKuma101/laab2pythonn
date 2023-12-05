A=int(input("comsumption of calories"))
B=int(input("average daily percentage decrease"))
C=int(input("the number of days"))
i=1
while(i<=C):
    i=i+1
    A=A-(A*(B/100))

    print(f"first day=",A)
    if A<1200:
        break
    print("you must stop decrease")