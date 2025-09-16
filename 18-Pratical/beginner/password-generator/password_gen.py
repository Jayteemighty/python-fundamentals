# Randomly generate password for users
# collect data from user about length and kind of characters they want. 

import json
import random
from datetime import datetime

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$#%().,?0123456789'

def generate_password():
    try:
        no_of_pwds = int(input("How many passwords would you like to generate?: "))
        length_of_pwd = int(input("Enter desired length of password: "))
        
        if no_of_pwds <= 0 or length_of_pwd <= 0:
            print("Please input a positive number")
        

        print("\nThese are your passwords: ")
        all_passwords = []
        
        for pwd in range(no_of_pwds):
            passwords = ''
            for char in range(length_of_pwd):
                passwords += random.choice(chars)
            print(passwords)
            all_passwords.append(passwords)
        
        # save to a file in json format
        passwords_data = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "passwords": all_passwords,
            "length": length_of_pwd,
            "count": no_of_pwds
        }
            
        with open('passwords.json', 'a') as f:
            f.write(json.dumps(passwords_data) + '\n')
        
        print(f"\n{no_of_pwds} passwords saved to passwords.json")
    
    except Exception as e:
        print(f"Please enter a valid number! Error is {e}")

if __name__ == '__main__':
    generate_password()
    