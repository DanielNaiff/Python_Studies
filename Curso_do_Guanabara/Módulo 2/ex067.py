while True:
    n = int(input("Digite um número para fazer tabuada:"))
    if n < 0:
        break
    print('-='*30)
    for i in range(0,11):
        print(f"{i} x {n} = {n*i}")
    print('-='*30)
print("Programa finalizado")
