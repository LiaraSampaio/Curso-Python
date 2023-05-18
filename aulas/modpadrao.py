'''
Módulos Padrão do Python (import, from, as e *)

as - usa para mudar o nome do sys 
    EX: import sys as s
        sys = 'Br'
* - faça todos os imports (Má prática)

https://docs.python.org/3/py-modindex.html

'''
import sys

plataform = 'Brasil'

print(sys.platform) # mostra sistema do desktop

from sys import exit, platform

print(plataform)

# __main__ - primeiro módulo executado é chamado de main

import dict
print('Este modulo é ', __name__)