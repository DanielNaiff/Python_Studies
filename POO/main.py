from pessoa import Pessoa

p1 = Pessoa('Luis', 29)

p1.comer('maçã')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')

print(p1.ano_atual)
print(p1.get_ano_nascimento())
print(Pessoa.gera_id())