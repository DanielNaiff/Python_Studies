vel = float(input("Digite a velocidade:"))
if vel >= 80:
    print(f"Multa: {(vel-80)*7}")
else:
    print("Não tá fazendo mais que a obrigação!")