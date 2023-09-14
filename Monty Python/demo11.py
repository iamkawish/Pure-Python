#Password Authesization
user_Id = "admin"
Password = "admin"
print("="*12,"Login Here","="*12)
usd=input("Please Enter the User Id: ")
Pwd = input("Please Enter the Password: ")
print("*"*45)

if(user_Id==usd and Password==Pwd):
    print("UserId and Password are Seccessfully  Valid:")
    print("*"*45)
else:
    
    print("UserId and Password are invalid:")
    print("*"*45)