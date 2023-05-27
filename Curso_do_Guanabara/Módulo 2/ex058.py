from random import randint
num = randint(0,10)
count = 0
while True:
    choice = int(input("Choose a number:"))
    if choice == num:
        print("You won")
        break
    else:
        print("Ooops!! that was close!")
        count += 1
print('Number of attempts', count)
