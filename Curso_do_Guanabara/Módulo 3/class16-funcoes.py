def mensagem(msg):
    print("-="*20)
    print(msg)
    print("-="*20)


mensagem("Sistema de alunos")

def contador(*num):
    print(num)

contador(2, 1, 7)
contador(8,0)
contador(4,4,7,6,2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)
