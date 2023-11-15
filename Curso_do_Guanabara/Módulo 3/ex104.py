def leiaint():
  while True:
    n = str(input('Digite um numero'))
    if n.isnumeric():
      return f'Voce acabou de digitar o numero {n}'
    else:
      print('Erro!! voce não digitou nenhum número')

resultado = leiaint()
print(resultado)