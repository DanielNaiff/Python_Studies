numero = int(input("Digite um número para calcular o fatorial:"))
fatorial = 1
for i in range (numero,0,-1):
    fatorial = fatorial * i
print("Fatorial:",fatorial)
