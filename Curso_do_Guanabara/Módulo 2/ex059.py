n1 = float(input("Escolha um número:"))
n2 = float(input("Escolha outro número:"))

while True:
    
    escolha = int(input("""Escolhas as opções:

    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] novos números
    [5] Sair"""))

    if escolha == 4:
        n1 = float(input("Escolha um número:"))
        n2 = float(input("Escolha outro número:"))
    elif escolha == 2:
        print("Multiplicação:",n1*n2)
    elif escolha == 3:
        if n1 > n2:
            print(f"{n1} é maior do que {n2}")
        elif n2 == n1:
            print(f"{n1} é igual a {n2}")
        else:
            print(f"{n2} é maior do que {n1}")
    elif escolha == 1:
        print("Soma:",n1 + n2)
    else:
        break
