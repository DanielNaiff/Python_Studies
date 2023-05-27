preco  = float(input('Digite o preço do produto:'))
print('''[1] à vista: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2X no cartão: preço normal
[4] 3X ou mais no cartão: 20% de juros''' )
op = int(input('Digite a opção: '))
if op == 1:
    print(f'Preço total: {preco*0.9}')
elif op == 2:
    print(f'Preço total: {preco*0.95}')
elif op == 3:
    print(f'Preço total: {preco}')
elif op == 4:
    print(f'Preço total: {preco*1.2}')
else:
    print('Opção inválida')