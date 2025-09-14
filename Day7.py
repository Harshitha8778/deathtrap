import random
lives = 6

#import word list
from hangman_words import word_list

#import logo, stages and print logo
from hangman_art import logo, stages
print(logo)

#generate a chosen word for the player to guess
chosen_word = random.choice(word_list)

#Create a string with as many blanks as the letters in the chosen word
size = len(chosen_word)
placeholder = ""
for pos in range(size):
    placeholder += "_"
print(placeholder)
print("YOU HAVE",lives,"LIVES LEFT!!!!!")

game_over = False
correct_letters = []

#Guess letters and turn the input into lower case. Iterate this until game is over
while game_over == False:
    guess = input("Guess the letter: \n").lower()

    #For every right guess, display the letter and for every other one display a blank until game is over
    display = ""
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        #add previously correctly guessed letters too to display
        elif letter in correct_letters:
            display += letter 
        else:
            display += "_" 
    print(display)

    #Specify game over conditions 
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("YOU LOSE")
            print("THE WORD IS:",chosen_word)
    if "_" not in display:
        game_over = True
        print("YOU WIN")

    #print no. of lives left and the hangman stage
    print(stages[lives])
    print("YOU HAVE",lives,"LIVES LEFT!!!!!")



