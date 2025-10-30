#BLACKJACK
import random
import sys
from blackjack_art import logo,win,lose
def game():
    yn = input("""Do you want to play a game of BLACKJACK?
               type\'Y\' to play or \'N\' to not: """)
    if yn.lower() =="y":
        blackjack()
    else:
        return

def blackjack():
    print(logo)
    deck = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "J": 10, "Q": 10, "K": 10}
    A1 = random.choice(list(deck.keyYs()))
    A2 = random.choice(list(deck.keys()))
    B1 = random.choice(list(deck.keys()))
    B2 = random.choice(list(deck.keys()))
    player = [deck[A1], deck[A2]]
    dealer = [deck[B1], deck[B2]]
    player_score = sum(player)
    dealer_score = sum(dealer)
    print("Your cards are", player)
    print("Current Score: ", player_score)
    print("dealer's revealed card is", deck[B1])
    cont = True
    while cont:
        draw = input("Type \'Y\' to get another card, Type \'N\' to pass:")
        if draw.lower() == "y":
            a = random.choice(list(deck.keys()))
            if a == "A":
                if (player_score + 11) > 21:
                    deck[a] = 1
                else:
                    deck[a] = 11
            player.append(deck[a])
            b = random.choice(list(deck.keys()))
            dealer.append(deck[b])
            player_score = sum(player)
            dealer_score = sum(dealer)
            print("Here you go", a)
            print("Your cards are", player)
            print("Current Score: ", player_score)
            print("dealer's revealed card is", deck[B1])
            if player_score > 21:
                print(lose)
                print("Player's final hand: ", player)
                print("Final player Score: ", player_score)
                print("Dealer's final hand:", dealer)
                print("Final dealer Score: ", dealer_score)
                return game()
            elif dealer_score > 21:
                print(win)
                print("Player's final hand: ", player)
                print("Final player Score: ", player_score)
                print("Dealer's final hand:", dealer)
                print("Final dealer Score: ", dealer_score)
                return game()
            else:
                cont = True
        if draw.lower() == "n":
            cont = False
            break
    if player_score >= dealer_score:
        print(win)
    elif dealer_score > player_score:
        print(lose)
        print("Player's final hand: ", player)
    print("Final player Score: ", player_score)
    print("Dealer's final hand:", dealer)
    print("Final dealer Score: ", dealer_score)
    game()
game()








