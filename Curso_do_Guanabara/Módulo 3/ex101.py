def voto(n):
    if (2023 - n < 16):
        voto = 'Voto negado'
    elif (2023 - n >= 16 and 2023 - n < 18):
        voto = 'Voto opcional'
    else:
        voto = 'Voto obrigatório'
    return voto

nascimento = int(input('Digite o ano que voce nasceu:'))
print(voto(nascimento))