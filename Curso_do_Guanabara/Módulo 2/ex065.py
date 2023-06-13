soma = contador = 0
escolha = 'q'
while escolha != 'n':
    n = int(input("Escolha um número:"))
    soma = soma + n
    contador += 1
    if contador == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    escolha = str(input("Deseja continuar[s/n]?")).rstrip().lower()
media = soma/contador
print(f"A media entre todos os valores digitados é igual a {media}. O maior número é {maior} e o menor é {menor}")
