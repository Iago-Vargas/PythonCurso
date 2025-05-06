# method vs @classmethod vs @staticmethod
# method - self, metodo de intancia
# @classmethod - cls, metodo de classe
# @staticmethod - metodo estatico (Sem self e cls)
# self é instancia

class Connection:
    #esse é o metodo normal com self, com o method
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password


    @classmethod
    #pegamos os dados direto da class, metodo classmethod
    def create_with_auth(cls, user, password): #auth é autentificação
        connections = cls()
        connections.user = user
        connections.password = password
        return connections

    @staticmethod
    #static nao tem acesso a cls nem a self, inutil ao python
    #somente retorna
    def soma (x, y):
        return x + y

# c1 = Connection()
c1 = Connection.create_with_auth("Iago", "123")
print(c1.user)
print(c1.password)