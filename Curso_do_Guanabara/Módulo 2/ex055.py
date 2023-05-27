menor = 0
maior = 0
for i in range(0,5):
    peso = int(input("Digite o peso: "))
    if i == 0:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print("O maior peso foi de",maior)
print("O menor peso foi de",menor)
