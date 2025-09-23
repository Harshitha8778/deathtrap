#   number guessing game
from guess_art import logo
import random
print(logo)
print("welcome to the number guessing game!".title())
number = random.randint(1,100)
difficulty = input("Choose difficulty, easy or hard: ")
if difficulty == "easy":
    counter = 10
else:
    counter = 5
for go in range(counter):
    guess = int(input("guess a number from 1 to 100: ".title()))
    counter -= 1
    if counter == 0:
        print("YOU LOSE")
        print("Your number is".title(),number)
    elif guess == number:
        print("YOU WON")
        print("You guessed in",counter,"tries")
        break
    elif guess > number:
        print("Go lower".title())
    elif guess < number:
        print("Go higher".title())







