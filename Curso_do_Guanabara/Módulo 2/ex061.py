primeiro_termo = int(input("Digite o primeiro termo:"))
razao = int(input("Digite a razão: "))
contador = 0
while contador < 10:
    termo = primeiro_termo + (contador*razao)
    print(f"{termo}-",end=" ")
    contador += 1
print("FIM")
