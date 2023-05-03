"""
Repetições:
while (enquanto) 
    - loop infinito em quanto nao tem fim
break (pausa/termina)
continue ()

+= soma mais 1
-= diminui 1
*= multiplica mais 1
/= dividi mais 1
//= divisao inteira
**= exponiaçao
%= resto

"""
condicao = True
while condicao:
    nome = input("Qual seu nome: ")
    print(f'Seu nome é {nome}')
    break

contador = 0
while contador < 10:
    contador += 1
    print(contador)
print("Acabou")

while contador <= 100:
    contador += 1

    if contador == 6:
        print("Nao vou contar o 6")
        continue

    if contador >= 10 and contador <= 27:
        print("Nao vou mostrar o ", contador)
        continue

    print(contador)

    if contador == 40:
        break