import random
from higherORlower_art import logo,vs
from game_data import data
def initial():
    print(logo)
    score = 0
    a = random.choice(data)
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    game(a,b,score)

def game(a,b,score):
    print(f"Compare A: {a['name']},a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']},a {b['description']}, from {b['country']}")
    lost = False
    c = []
    while not lost:
        guess = input("GUESS: ")
        if guess.lower() == "a":
            if a['follower_count'] > b['follower_count']:
                score += 1
                a = a
                b = random.choice(data)
                while a == b and b not in c:
                    b = random.choice(data)
                    c.append(b)
                game(a,b,score)
            else:
                print('you lost')
                print("SCORE",score)
                lost = True
                play()
        elif guess.lower() == "b":
            if a['follower_count'] < b['follower_count']:
                score += 1
                a = b
                b = random.choice(data)
                while a == b and b not in c:
                    b = random.choice(data)
                    c.append(b)
                game(a,b,score)
            else:
                print('you lost')
                print("SCORE",score)
                lost = True
                play()
def play():
    play = input("DO YOU WANNA PLAY(Y/N):")
    if play.lower() == 'y':
        initial()
    else:
        return
play()














