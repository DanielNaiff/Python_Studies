from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade, comendo=False, falando= False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} esta comendo, nao pode falar')
            return
        
        if self.falando:
            print(f'{self.nome} ja esta falando')
            return
        
        print(f'{self.nome} esta falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} nao esta falando')
            return
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja esta comendo.')
            return
        
        if self.falando:
            print(f'{self.nome} nao pode comer falando')
            return 
        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} nao esta comendo')
            return
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade