from random import randint
vitorias = 0
while True:
    jogador = int(input("Escolha um valor:"))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'pi':
        tipo = str(input("Escolha se voce quer par ou imoar [p/i]")).lower().rstrip()[0]
    print(f"Voce jogou {jogador} e o computador {computador}. Total de {total} ")
    if tipo == 'p':
        if total % 2 == 0:
            print("Voce venceu!")
            vitorias += 1
        else:
            print("Voce perdeu!")
            break
    elif tipo == 'i':
        if total % 2 == 1:
            print("Voce venceu!")
            vitorias += 1
        else:
            print("Voce perdeu!")
            break
print("Total de vitórias:",vitorias)