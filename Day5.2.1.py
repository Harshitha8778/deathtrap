#PASSWORD GENERATOR USING FOR LOOP
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
l = int(input("How many letters would you like in your password?\n"))
s = int(input(f"How many symbols would you like?\n"))
n = int(input(f"How many numbers would you like?\n"))
password = ""
list = []
for char in range(1,l+1):
    a = random.choice(letters)
    list.append(a)
#    password += random.choice(letters)
for char in range(1,s+1):
    b = random.choice(symbols)
    list.append(b)
#    password += random.choice(symbols)
for char in range(1,n+1):
    c = random.choice(numbers)
    list.append(c)
#    password += random.choice(numbers)
print(list)
random.shuffle(list)
password = "".join(list)
print(password)






