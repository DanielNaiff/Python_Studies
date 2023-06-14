mulher_menor20 = 0
maiores = 0
homens = 0
while True:
    print("-"*24)
    print("Cadastrar uma pessoa")
    print("-"*24)
    idade = int(input("Idade:"))
    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input("Sexo[m/f]:")).lower().rstrip()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'f':
        if idade < 20:
            mulher_menor20 += 1
    elif sexo == 'm':
        homens += 1
    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input("Quer continuar[s/n]?")).lower().rstrip()[0]
    if escolha == 'n':
        break
print("Mulheres com menos de 20 anos:",mulher_menor20)
print("Total de homens cadastrados:",homens)
print("Maiores de idade:",maiores)