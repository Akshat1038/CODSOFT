import random
import string

def generate_password(length):
    all_characters=string.ascii_letters+string.digits+string.punctuation
    ## "Sring.ascii_letters ()"

    password=""
    for i in range(length):
        password = password + random.choice(all_characters)

    return password
length = int(input("Enter the  password length: "))


   
generate_password=generate_password(length)
print(f"Generated Password:{generate_password}")