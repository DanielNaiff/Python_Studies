n1 = int(input("Enter a number:"))
n2 = int(input("Enter another number:"))
if n1 > n2:
    print(f"{n1} is bigger than {n2}")
elif n2 > n1:
    print(f"{n2} is bigger than {n1}")
else:
    print("Does not exist bigger number, both are equal!")