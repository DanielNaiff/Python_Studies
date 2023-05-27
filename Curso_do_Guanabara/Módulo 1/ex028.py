from random import randint
n = randint(0,5)
f = int(input("Enter a number:"))
if f == n:
    print("You win!")
else:
    print("Ooops!")