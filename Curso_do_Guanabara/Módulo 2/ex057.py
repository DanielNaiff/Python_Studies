sexo = ''
while (sexo != 'M' and sexo != 'F'):
    sexo = str(input("Enter your gender: ")).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('Wrong data')
