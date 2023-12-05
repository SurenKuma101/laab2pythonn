x=int(input("enter the number of years you want"))
i=0
B=0
while(i<x*12):
   y=int(input("enter average high temperature of each month"))
   i=i+1
   B=B+y


print("total result=",B)
average_temperature=B/(x*12)
print("average temperature for year=",average_temperature)

if(x>=average_temperature):
   print("highest temperature=",B)

