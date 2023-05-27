from datetime import date
atual = date.today().year
m = 0
me = 0
for c in range(0,7):
  nasc = int(input('Digite a data de nascimento: '))
  if atual - nasc >= 21:
    m += 1
  else:
    me += 1
print('A quantidade de pessoas que atingiram a maioridade foi',m)
print('A quantidade de pessoas que ainda não atingiram a maioridade foi',me)