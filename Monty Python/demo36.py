# using while loop in Function
def powerFind(x,y):
    result=x**y
    print(x,"power",y,"=",result)
    print("="*30)
i=0;
while i<5:
    num1 = int(input("Enter a First Number: "))
    num2 = int(input("Enter a Second Number: "))
    print("="*30)
    powerFind(num1,num2)
    i=i+1