while True:
    tuple = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorzer','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
    choice = int(input("Escolha um número entre 0 a 20:"))
    if 0 <= choice <= 20:
        print(f"Voce escolheu o número {tuple[choice]}")
        option = ' '
        while option not in 'sn':
            option = str(input("Voce deseja continuar?[s/n]")).rstrip().lower()[0]
        if option == 'n':
            break
    else:
        print("Tente novamente.",end='')