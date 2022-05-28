print("Number Guessing Game")
print("You Get One Chance to guess the number")

number=int(input("Enter a number between 1-5 "))
chances=1
gnumber=3

if number==gnumber:
    print("You Guessed the Number")
else:
    print("The number was", gnumber)
