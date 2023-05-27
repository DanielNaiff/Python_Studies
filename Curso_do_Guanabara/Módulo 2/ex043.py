peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura:'))
imc = peso/(altura**2)
print(f'Seu imc é {imc}')
if imc < 18.5:
    print('Voce está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Voce está na faixa do peso normal')
elif 25 <= imc < 30:
    print('Você está em sobrepeso')  
elif 30 <= imc < 40:
    print('Você está em sobrepeso')
elif imc >= 40:
    print('Você está em obesidade mórbida!')
