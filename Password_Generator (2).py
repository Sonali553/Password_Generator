3import random
print("Welcome to Password Generator")
limit = input("Enter the number of passwords to be generated:")
limit = int(limit)
length = input("Enter the length of the password")
length = int(length)

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_'
for pwd in range(limit):
    Passwords = '' 
    for ch in range(length):
        Passwords += random.choice(chars)
    print(Passwords)
