n = int(input("Quanto valores voce quer mostrar?"))
contador = 0
primeiro = 0
segundo = 1
print("0--1--",end='')
while contador < n-2:
    soma = primeiro + segundo
    primeiro = segundo
    segundo = soma
    print(soma, end='--')
    contador += 1