import random
letters = ['a','b','c', 'd', 'e', 'f','g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','$','%','#', '&']

print("Welcome to the password generator..!")

no_letters = int(input("How many letters you want ?"))

no_numbers = int(input("How many numbers you want ?"))

no_symbols = int(input("How many symbols you want ?"))

password = []

for char in range(1,no_letters+1):
    password += random.choice(letters)

for num in range(1, no_numbers + 1):
    password += random.choice(numbers)

for sym in range (1, no_symbols + 1):
    password += random.choice(symbols)
    
random.shuffle(password)

passwords = ""

for char in password:
    passwords += char

print ("Your generated password is : ", passwords )