mulheres_menos20 = 0
maiores = 0
homens = 0

while True:
    sexo = str(input("Digite o seu sexo[m/f]:")).lower().rstrip()
    idade = int(input("Digite a sua idade:"))
    if sexo == 'f':
        if idade < 20:
            mulheres_menos20 += 1
        if idade > 18:
            maiores += 1
    if sexo == 'm':
        homens += 1
        if idade > 18:
            maiores += 1
    escolha = str(input("Deseja continuar?[s/n]"))
    if escolha == 's':
        continue
    else:
        break
print("Pessoas maiores de 18:",maiores)
print("Quantidade de homens cadastrados:",homens)
print("Mulheres com menos de 20 anos:",mulheres_menos20)