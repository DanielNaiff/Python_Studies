def maior(* num):
    print('Analisando os valores dados...')
    maior = menor = cont = 0
    for n in num:
        cont += 1
        print(n,end=' ')
        if cont == 1:
            maior = menor = n
            print(menor)
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    print(f'O maior número é {maior} e o menor número é {menor}')


maior(2,9,4,5,7,11)