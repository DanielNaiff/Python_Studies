num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(bin(num))
elif opcao == 2:
    print(oct(num))
elif opcao == 3:
    print(hex(num))
else:
    print('Opção inválida!')