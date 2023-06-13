contador = -1
soma = 0
n = 0
while n != 999:
    n = int(input("Digite um número[999 para parar]:"))
    soma = soma + n
    contador += 1
print(f"A soma dos {contador} números digitados é igual a {soma - 999}")