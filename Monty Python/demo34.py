#Calculation in Function
def calulator():
     num1=int(input("Enter a First Number :"))
     num2=int(input("Enter a Second Number :"))
     operator = input("Please Select Operator")
     if operator=="+":
        res=num1+num2;
        print("The sum is:",res)
        print("*"*30)
        
    elif operator=="-":
        res=num1-num2;
        print("The Minus is:",res)
        print("*"*30)
        
    elif operator=="*":
        res=num1*um2;
        print("The Times is:",res)
        print("*"*30)
    elif operator=="/":
        res=num1/num2;
        print("The sum is:",res)
        print("*"*30)
    else:
        print("Please Enter a Valid Operator")
calulator()