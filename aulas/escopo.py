'''
escopo global - onde todo código é alcançável.
escopo local - onde apenas nomes do local pode ser
alcançados.

'''
x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print(x,y)
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)

'''
return - retorno de valores das funções

'''
def soma(x, y):
    return x + y

soma1 = soma(2,5)
soma2 = soma(3,4)
print(soma1 + soma2)