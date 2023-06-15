valor = int(input("Valor a ser sacado:"))
total = valor
ced = 50
total_cedulas = 0
while True:
    if total >= ced:
        total -= ced
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f"total de {total_cedulas} de R$ {ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_cedulas = 0
        if total == 0:
            break
