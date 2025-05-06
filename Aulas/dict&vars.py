# __dict__ e vars para atributos de instancia
# __dict__ retorna um dicionario com todos atributos naquele objeto
#vars() é uma função embutida que retorna o mesmo valor de __dict
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa("Iago", 21)

print (p1.__dict__) #Sai os dados em estilo dicionario
print (vars(p1)) #Retornando o mesmo valor de __dict__