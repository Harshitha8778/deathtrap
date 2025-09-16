#LOVE CALCULATOR
def calculate_love_score(name1,name2):
    store = []
    for letter in name1:
        store += letter
    for letters in name2:
        store += letters
    counterT = 0
    counterR = 0
    counterU = 0
    counterE = 0
    counterL = 0
    counterO = 0
    counterV = 0
    for letter1 in store:
        if letter1.lower() == "t":
            counterT += 1
        elif letter1.lower() == "r":
            counterR += 1
        elif letter1.lower() == "u":
            counterU += 1
        elif letter1.lower() == "e":
            counterE += 1
        elif letter1.lower() == "l":
            counterL += 1
        elif letter1.lower() == "o":
            counterO += 1
        elif letter1.lower() == "v":
            counterV += 1

    print(f"T occurs {counterT} times")
    print(f"R occurs {counterR} times")
    print(f"U occurs {counterU} times")
    print(f"E occurs {counterE} times")
    T1 = str(counterT+counterR+counterU+counterE)
    print("Total =",T1)
    print(f"L occurs {counterL} times")
    print(f"O occurs {counterO} times")
    print(f"V occurs {counterV} times")
    print(f"E occurs {counterE} times")
    T2 = str(counterL+counterO+counterV+counterE)
    print("Total =",T2)
    print("Love Score is",T1+T2)

a = input("name1: ")
b= input("name2: ")
calculate_love_score(a,b)