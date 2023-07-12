# CLASSES DECORADORAS

class Multiplicar:
    def __init__(self, func):
        self.fun = func 

    def __call__(self, *args, **kwargs):
        resultado = self.fun(*args, **kwargs)
        return resultado  
    
@Multiplicar
def soma(x,y):
    return x + y

res = soma(2,4)
print(res)