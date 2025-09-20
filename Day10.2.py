import sys
from calc_art import logo
print(logo)
def calculator(first, sign, second):
    if sign == "+":
        return first + second
    elif sign == "-":
        return first - second
    elif sign == "*":
        return first * second
    elif sign == "/":
        return first / second
    else:
        print("Invalid operation")
        return None
def inputs():
    cont = False
    output = None
    while True:
    # while true loop runs infinitely unless you use statements such as sys.exit() or break to exit
        if not cont:
            a = int(input("What is your first number: "))
        else:
            a = output
        b = int(input("What is your second number: "))
        s = input("""What operation would you like to perform?
              +
              -
              *
              / \n
        """)
        output = calculator(a, s, b)
        print(f"Result: {output}")
        next_step = input("Do you want to continue (type y), start fresh (type n), or exit (type x)?: ").lower()
        if next_step == "x":
            sys.exit()
        elif next_step == "y":
            cont = True
        elif next_step == "n":
            cont = False
        else:
            print("Invalid input, exiting.")
            sys.exit()
inputs()