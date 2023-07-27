def fatorial(num = 1, mostrar = False):
    """
    Calcula o fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        if mostrar:
            if c == 1:
                print(f' {c} = ',end='')
                break
            print(f' {c} X', end='')
        f *= c
    return f

print(fatorial(5,mostrar=True))
help(fatorial)
