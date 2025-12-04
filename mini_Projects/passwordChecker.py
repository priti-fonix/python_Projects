# password Strength checker

import re

def password_strength(password):

    # print("welcome to the pass- strngth block")
    # password length
    #length,digit,uppercase,lowercase

    if(len(password) < 8):
        return "Weak, enter a password more than length of 8"
    
    if not any(char.isdigit() for char in password):
        return "Weak,password must have a digit in it"
     
    if not any(char.isupper() for char in password):
        return "Weak,password must have an uppercase in it"
     
    if not any(char.islower() for char in password):
        return "Weak,password must have an lowercase in it"
     
    if not re.search(r'[~!@#$%^&*()<>.(){}]',password):
        return "medium : password must have special characters in it"
    
    return "strong : password is strong and secure now "

def password_checker():
    
    print("------------------Welcome to password checker -------------")


    while True:
        password = input("Enter a password to be checked its strength or ( exit or Quit to quit)")

        if password.lower() == "quit" or password.lower() == "exit":
            print("ok , thanks for visiting")
            break
        
        result = password_strength(password)
        print(result)
# Run the password function 

if __name__ == "__main__":
    password_checker()

    


       
   
    