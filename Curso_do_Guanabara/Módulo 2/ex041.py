from datetime import date
atual = date.today().year
ano = int(input('Digte o ano do seu nascimento:'))
idade = atual - ano
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Senior')
else:
    print('Master') 
