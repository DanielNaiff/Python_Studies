mais_1000 = produtos = total_gasto = barato = 0

while True:
    produto = str(input("Nome do produto:")).capitalize()
    preco = float(input("Preço do produto: R$"))

    total_gasto += preco
    produtos += 1
    mais_barato = ' '
    if preco > 1000:
        mais_1000 += 1
    if produtos == 1:
        barato = preco
        mais_barato = produto
    else:
        if preco < barato:
            mais_barato = produto
    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input("Voce deseja cadastrar outro produto[s/n]?"))[0]
    if escolha == 'n':
        break
print("Total gasto:",total_gasto)
print("Quantidade de produtos que custam mais de 1000 reais:",mais_1000)
print("Nome do produto mais barato:",mais_barato)
print("Fim do programa!")
