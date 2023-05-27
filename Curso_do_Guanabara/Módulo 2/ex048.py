acumulador = 0
contador = 0
for c in range(3,500,6):
  acumulador = acumulador + c
  contador += 1
print(f'A soma de todos os {contador} números é {acumulador}')