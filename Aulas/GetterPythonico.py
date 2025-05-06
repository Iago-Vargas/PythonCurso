# @property - é um getter no modo pythonico
# getter - metodo que obtem atributo
# utilizado como um getter em python
# ela é uma propriedade do objeto mas se comporta como um atributo
# Código cliente - é o codigo que usa seu codigo


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    def get_cor(self): #Aqui estamos basicamente usando "private String cor"
        return self.cor_tinta

caneta = Caneta("Convencional")
print (caneta.get_cor())


#------------------------

#Metodo property

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta


caneta = Caneta("Property")
print (caneta.cor)
