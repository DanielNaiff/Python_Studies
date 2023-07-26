from random import randint

def sorteia(lista=()):
    for cont in range(0,5):
        lista.append(randint(1,45))


def somaPar(lista):
    soma = 0
    for cont in lista:
        if cont % 2 == 0:
            soma += cont
    print(f'O resultado dos números pares é {soma}')


numeros = list()
sorteia(numeros)
print(numeros)
somaPar(numeros)
