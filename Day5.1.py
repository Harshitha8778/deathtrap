for num in range(1,101):
    a = str(num)
    if num % 3 == 0:
        if a == str(num):
            a = "Fizz"
    if num % 5 == 0:
        if a == str(num):
            a = "Buzz"
    if num % 3 == 0 and num % 5 == 0:
        if a == str(num):
            a == "FizzBuzz"
    print(a)