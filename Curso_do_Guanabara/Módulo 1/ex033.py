a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c 
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c 

print(maior,menor)