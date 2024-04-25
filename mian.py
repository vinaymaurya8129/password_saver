from saveJson import SavePassword
import json

# def create_account():
#     name = input("please enter your name : ")
#     pin = input("\nset your pin : ")
#     user1.makedirectory(name)
#     user1.new_Account_Create(name, pin)
#     ask_add_pass()
    
    
# def ask_create_account():
#     ask_user=input("Do you want to create an account(Y/N)").lower()
#     if ask_user =='y':
#         create_account()
#     elif ask_user=='n':
#         print('okey ,bye')
#     else:
#         ask_create_account()


# def ask_add_pass():
#     ask_user=input("Do you want to add Password (Y/N): ").lower()
#     if ask_user =='y':
#         user1.add_password()
#     elif ask_user=='n':
#         print('okey ,bye')
#     else:
#         ask_add_pass()
   
    
#creating user
user1 = SavePassword()
# menus
user_choice = user1.menu()
if user_choice == 1:
    user1.create_account()
else:
    [auth_status, user_name]= user1.auth()   #returns two values  
    if auth_status == True:
        user1.add_password(user_name)
    else:
        user1.ask_create_account()
            
            
