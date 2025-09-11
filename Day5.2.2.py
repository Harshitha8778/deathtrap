#PASSWORD GENERATOR USING RANDOM MODULE
import random
from random import Random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
l = int(input("How many letters would you like in your password?\n"))
s = int(input(f"How many symbols would you like?\n"))
n = int(input(f"How many numbers would you like?\n"))
passcodes = []
passcodes.extend(random.sample(letters,l))
passcodes.extend(random.sample(numbers,n))
passcodes.extend(random.sample(symbols,s))
random.shuffle(passcodes)
password = "".join(passcodes)
print(passcodes)
print(password)







