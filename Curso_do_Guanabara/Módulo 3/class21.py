def somar(a=0,b=0,c=0):
    s = a+b+c
    return s
r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)

print('Os resultados foram:', r1, r2, r3)

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite o valor para o fatorial:'))
print('resultado:', fatorial(n))