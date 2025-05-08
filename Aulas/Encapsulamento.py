#Encapsulamento (Public, Protected, private)
#Publico sem underline
#Protected um underline - somente na classe que esta e nas subclasses
#Private dois underline - somente na classe que foi chamado

class Foo:
    def __init__(self):
        self.public = "metodo público"
        self._protected = "metodo protected"
        self.__private = "metodo private"

    def metodo_publico(self):
        return 'def metodo publico'

    def _metodo_protected(self):
        return 'def metodo protected'

    def __metodo_private(self):
        return 'def metodo private'

f = Foo()

print(f.__private)
print(f._protected)
print(f._metodo_protected())
print(f.metodo_publico())
print(f.public)

