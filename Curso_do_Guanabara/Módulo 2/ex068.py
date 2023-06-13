from random import randint
vitorias = 0
while True:
    escolha = str(input("Escolha se voce quer par ou ímpar [p/i]:")).lower().rstrip()
    n = int(input("Digite um número [0 a 10]:"))
    c = randint(0,10)
    print('-='*30)
    print(f'Sua escolha {n}, escolha do computador {c}')
    print('-='*30)
    if (n + c) % 2 == 0 and escolha == 'p':
        vitorias += 1
        print("Resultado par, vc venceu")
        print('-='*30)
    elif (n + c) % 2 == 0 and escolha == 'i':
        print("Resultado par, voce perdeu")
        print('-='*30)
        break
    elif (n + c) % 2 == 1 and escolha == 'i':
        vitorias += 1
        print("Resultado par, vc venceu")
        print('-='*30)
    elif (n + c) % 2 == 1 and escolha == 'p':
        print("Resultado impar, voce perdeu")
        print('-='*30)
        break

print("Vitórias consecutivas",vitorias)