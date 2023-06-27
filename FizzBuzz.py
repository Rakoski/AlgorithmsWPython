# Write a program that takes a user’s input and prints the numbers from one to the number the user entered. However, for
# multiples of three print Fizz instead of the number and for the multiples of five print Buzz.
# For numbers which are multiples of both three and five print FizzBuzz

usrInp = int(input("Número: "))
for c in range(1, usrInp + 1):
    print(c)
    if c % 5 == 0 and c % 3 == 0:
        print("FizzBuzz")
    elif c % 3 == 0:
        print("Fizz")
    elif c % 5 == 0:
        print("Buzz")

