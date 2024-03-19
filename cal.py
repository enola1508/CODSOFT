# calculator
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVIDE")
print("5 .Exponetial power")
p=int (input("Which no.operation do you want?"))
a= int(input("enter the first value="))
b= int(input("enter the second value="))
if p==1:
    s1= a+b
    print("The answer is ", s1)
elif p==2:
    s2= a-b
    print("the answer is", s2)
elif p==3 :
    s3= a*b
    print("the answer is", s3)
elif p==4:
    s4= a/b
    print("the answer is",s4)
elif p==5:
    s5= a**b
    print("the answer is",s5)
else :
    print("Ooops...No operation found")
Y=input("do you want to continue?Y/N=")
while Y==Y:
        continue
