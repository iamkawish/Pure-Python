def finpower(x,y):
    res=x**y
    print(x,"Power",y,"=",res)#10 power 2 = 100
    
#finpower(10,2)
#num1=int(input("Enter a first number :"))
#num2 = int(input("Enter a Second number :"))
print("="*30)
#finpower(num1,num2) #Five time call karna ka liye yah use kare ga or second method jo haii wo loo loop kare ga
#finpower(num1,num2)
#finpower(num1,num2)
#finpower(num1,num2)
#finpower(num1,num2)
for i in range(5):
    num1=int(input("Enter a first number :"))
    num2 = int(input("Enter a Second number :"))
    #print("="*30)
    finpower(num1,num2)