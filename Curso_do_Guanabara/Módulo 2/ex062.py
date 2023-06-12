primeiro_termo = int(input("Digite o primeiro termo:"))
razao = int(input("Digite a razão: "))
contador_primario = 0
escolha = 1
total = 0
escolha = 10

while escolha != 0:
    total = total + escolha
    while contador_primario < total:
        termo = primeiro_termo + (contador_primario*razao)
        print(f"{termo}-",end=" ")
        contador_primario += 1
    print("PAUSA")
    escolha = int(input("\nQuantos termos voce quer amostrar a mais?"))
print(f"Prohrma finalizado com {total} itens escolhidos")
