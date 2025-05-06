#Exercicio - Salvar classe em JSON
#Salvar os dados da classe em JSON
import json

CAMINHO_AQUIVO = "aquivo.json"

class Pessoa:
    def __init__(self, nome, idade ):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Iago", 22)
p2 = Pessoa("Maria", 19)
p3 = Pessoa("Jemerson", 10)

bd = [vars(p1), vars(p2), vars(p3)] #Sem vars nao iria ficar salvo e iria dar erro

with open(CAMINHO_AQUIVO, "w") as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)