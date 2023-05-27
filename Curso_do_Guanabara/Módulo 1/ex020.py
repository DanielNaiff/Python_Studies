from random import shuffle
n1 = str(input("Enter a name:"))
n2 = str(input("Enter a name:"))
n3 = str(input("Enter a name:"))
n4 = str(input("Enter a name:"))
lista = [n1,n2,n3,n4]
shuffle(lista)
print(lista)