from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
if idade == 18:
    print('Voce precisa se alistar imediatamente!')
elif idade > 18:
    print(f'Voce ter se alistado a {idade - 18} anos')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para voce se alistar')
else:
    print('Digite um valor válido!')