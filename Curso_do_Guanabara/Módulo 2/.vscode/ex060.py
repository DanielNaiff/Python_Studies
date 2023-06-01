fatorial = int(input("Digite um número para calcular o fatorial:"))
contador = fatorial
while contador > 0:
    resultado = fatorial * (fatorial - 1)
    fatorial = fatorial - 1
    contador -= 1
print(resultado)