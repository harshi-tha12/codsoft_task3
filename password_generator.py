import random
import string 

def password_generator(length):
    password_characters=string.digits+string.ascii_lowercase+string.ascii_uppercase+string.punctuation
    password=''.join(random.choice(password_characters) for i in range(length))
    return password
    
def generator():
    print('\n****PASSWORD GENERATOR****')
    while True:
        try:
            length=int(input('Enter desired length for your password: '))
            if length<=0:
               print('Invalid input!!Enter correct number...\n')
            else:
               break
        except ValueError:
         print('Invalid input!!Enter valid input..\n')
    generated_password=password_generator(length)
    print(f"Generated password: {generated_password}")
generator()         
    
    
