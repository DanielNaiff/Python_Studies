soma_idade = 0
media = 0
femeas = 0
maior = 0
nome_do_velho= ' '
for i in range(1,5):
    print(f"-------Pessoa {i}-------")
    nome = str(input("Nome:")).strip()
    idade = int(input("Idade:"))
    soma_idade += idade
    sexo = str(input("Digite o seu sexo[F/M]:")).strip().capitalize()
    if sexo == 'F' and idade < 20:
      femeas += 1
    if sexo == 'M':
       if i == 1:
          nome_do_velho = nome
          maior = idade
       else:
          if idade > maior:
             nome_do_velho = nome
             maior = idade
media = soma_idade / 4
print("Médias das idade:",media)
print("Homem mais velho:", nome_do_velho.title(),"Tem idade de",maior)
print("Quantidade de mulhres mais novas que 20 anos:",femeas)
