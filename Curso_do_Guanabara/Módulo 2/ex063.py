n = int(input("Quanto valores voce quer mostrar?"))
contador = 0
primeiro = 0
segundo = 1

while contador < n:
    soma = primeiro + segundo
    primeiro = segundo
    segundo = soma
    print(soma, end='--')
    contador += 1