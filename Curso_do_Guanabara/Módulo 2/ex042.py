a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c: 
        print("Os valores formam um triângulo equilátero.")
    elif a == b and a == c:
        print("Os valores formam um triângulo isósceles.")
    elif a != b != c != a: 
        print("Os valores formam um triângulo escaleno.")
else:
    print("Os valores não formam um triângulo.")