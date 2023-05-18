# Modularização
# main o primeiro módulo é executado chama-se __main__

import aula28

print('Este modulo se chama', __name__)

import importlib # recarrega o modulo
import aula28

print(aula28)
for i in range(10):
    importlib.reload(aula28)
    print(i)
print('FIM')