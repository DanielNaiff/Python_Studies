nota1 = float(input('Digite a sua primeira nota:'))
nota2 = float(input('Digite a sua segunda nota:'))
if (nota1+nota2)/2 >= 7:
    print('Voce está aprovado!')
elif (nota1+nota2)/2 <= 7:
    print('Voce está reprovado!')
else:
    print('Digite um valor válido!')