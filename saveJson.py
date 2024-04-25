import json
import os

class SavePassword:
    # static variable /class variable
    index_json = 2

    # init
    def __init__(self):
        self.pin = 0
        self.name = ""
        self.index_json = SavePassword.index_json

    # option on login/ as created object
    def menu(self):
      try:
        user_choice = input(
                """Hello, How would you like to proceed: 
                             Choose : 
                             1: for create new Account
                             2: Add password, Already have an Account 
                             
                             ctrl+C : for exit
                             
                          """
            )
        
        user_choice=int(user_choice)
  
        if user_choice in [1,2]:
          return user_choice
        else:
          print("please choose an applicable option.")
          return self.menu()
      except:
        print("Not applicable!")
        self.menu()
          
    
    # account creation
    def new_Account_Create(self,name,pin):
        
        self.name = name
        self.pin = pin

        #user login data
        user_auth_data={
            "name":f"{self.name}"
            ,"pin":f'self.pin'
          }
        user_pass_data={
          'data':[]
        }
        user_auth_data = {"data": [{"name": f"{self.name}", "pin": f"{self.pin}"}]}

        data_json = json.dumps(user_auth_data, indent=1)

        with open(f"./users/{self.name}_auth_pass/{self.name}_auth.json", "w") as f:
            f.write(data_json)
        with open(f"./users/{self.name}_auth_pass/{self.name}_password.json", "w") as d:
            # d.write(user_pass_data)
            json.dump(user_pass_data,d, indent=1)
        # msg acct created
        print(
            f"Congretulations {self.name}! \nYour Account has been created successfuly!"
        )
        
  
    # authenticate
    def auth(self):
        user_name = input("\nPlease provide your @username : ")
        user_pin = int(input("\nplease enter you #PIN : "))
        # try:
        #   user_pin=int(user_pin_1)
        # except:
        #   print("Pin should contain only 0 t0 9.\n\nTry agian : ")
        #   self.auth()
          
        if(type(user_pin)==int):  
          try:
            with open(f"./users/{user_name}_auth_pass/{user_name}_auth.json", "r") as f:
                authdata = json.load(f)
            auth_user_name = authdata["data"][0]["name"]
            auth_user_pin = int(authdata["data"][0]["pin"])
            print(type(auth_user_name), type(auth_user_pin))

            if auth_user_name == user_name and auth_user_pin == user_pin:
                print(f"You are authenticated successfuly!")
                return [True,user_name]
            else:
                print("NAME or PIN did't matched!")
                auth_list=self.auth()
                return auth_list
          except:
            print("Did not find user account with provided creadentials. \nPlease Create your account to save your password!")
            return [False,user_name]
        else:
          print("Pin should contain only 0 t0 9.\n\nTry agian : ")
          self.auth()
            
                              
    def add_password(self,user_name):
      add_email=input("\nEnter your email Id: ")
      add_password=input('\nEnter your password for this account : ')
      add_hint=input('\nEnter you hint for this account : ')
      
      add_data={
        "email":add_email,
        "password":add_password,
        "hint":add_hint
      }
      
      with open(f"./users/{user_name}_auth_pass/{user_name}_password.json", "r") as f:
            authdata = json.load(f)
          
      # appending data
      authdata["data"].append(add_data)

      with open(f"./users/{user_name}_auth_pass/{user_name}_password.json","w") as f:
        json.dump(authdata,f,indent=1)
        print('Password has been recorded successfully')
        #self.ask_add_more_pass(user_name)


    def makedirectory(self,user_name):
      path=f"./users/{user_name}_auth_pass"
      os.makedirs(path)
      
  
    def create_account(self):
      name = input("please enter your name : ")
      pin = input("\nset your pin : ")
      self.makedirectory(name)
      self.new_Account_Create(name, pin)
      self.ask_add_pass(name)
      
 
    def ask_add_pass(self,user_name):
      ask_user=input("Do you want to add Password (Y/N): ").lower()
      if ask_user =='y':
          self.add_password(user_name)
      elif ask_user=='n':
          print('okey ,bye')
      else:
          self.ask_add_pass(user_name)
          
              
    def ask_create_account(self):
      ask_user=input("Do you want to create an account(Y/N)").lower()
      if ask_user =='y':
          self.create_account()
      elif ask_user=='n':
          print('okey ,bye')
      else:
          self.ask_create_account()
          
    
    def ask_add_more_pass(self,user_name):
      print('Hello',user_name)
      ask_user=input("Do you want to add another Password (Y/N): ").lower()
      if ask_user =='y':
          self.add_password(user_name)
      elif ask_user=='n':
          print('okey ,bye')
      else:
          self.ask_add_pass(user_name) 
    
    