primeiro_termo = int(input("Digite o primeiro termo:"))
razao = int(input("Digite a razão: "))
contador_primario = 0
contador_geral = 0
escolha = 1
while contador_primario < 10:
    termo = primeiro_termo + (contador_primario*razao)
    print(f"{termo}-",end=" ")
    contador_primario += 1
print("PAUSA")
while escolha != 0:

    escolha = int(input("\nQuantos termos voce quer amostrar a mais?"))
    contador_secundario = 0
    primeiro_termo = termo + razao

    if escolha != 0: 

        while contador_secundario < escolha :

            termo = primeiro_termo + (contador_secundario*razao)
            print(f"{termo}-",end=" ")
            contador_secundario += 1

        print("PAUSA")

    contador_geral = contador_geral + contador_secundario
contador_geral = contador_geral + contador_primario
print("FIM")
print("Total de numeros:", contador_geral)
