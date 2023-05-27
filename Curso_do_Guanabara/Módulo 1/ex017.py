ca=float(input("Digite o cateto adjacente:"))
co=float(input("Digite o catetto oposto:"))
h = ((ca**2) + (co**2))**(1/2)
if type(h) == 'float':
  print("A hipotenusa é:",h)
else:
  print("A hipotenusa é:",int(h))
