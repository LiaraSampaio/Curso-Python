# Encapsulamento (public, protected, private)
# (SEM UNDERLINE) = public
    # Pode ser usado quaisquer lugar

# (UM UNDERLINE) = protected 
    # Não dever ser usado fora da classe ou suas subclasses

# (DOIS UNDERLINES) = private
    # Só dever ser usado na clasee em que foi declarado

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é privado'
        
    def metodo_public(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__exemplo)
        self.__metodo_private()
        return 'metodo_public'
    
    def _metodo_protected(self):
        print('_metodo_protected')
    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'

f = Foo()
print(f.metodo_public())
