# Métodos de classe
# São os métodos onde "self" será "cls", cls = Classe
# ira recever a instancia no primeiro parametro, recebemos a propria classe
# cls → referência à classe em si, usada em métodos de classe.

class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("Hey")

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls("Anônimo", idade)

p1 = Pessoa("Iago", 21)
p2 = Pessoa.criar_com_50_anos("Maria")
p3 = Pessoa("Maria Clara", 20)
p4 = Pessoa.criar_sem_nome(30)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)