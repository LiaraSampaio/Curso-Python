# And (TODAS CONDIÇÕES PRECISA SER VERDADEIRAS)
    # Considerado falso: 0 0.0 '' 
# Or (qualquer condição verdadeira avalia a expressao verdadeira)
# Not (Inverter expresssões)

entrada = input('[E]ntar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '12345'

if entrada == 'E' and senha_digitada == senha_digitada:
    print('Entrou')
else:
    print('Saiu')


entrada = input('[E]ntar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '12345'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_digitada:
    print('Entrou')
else:
    print('Saiu')


senha = input('Senha: ')

if not senha:
    print('Você não digitou nada!')
else:
    print('Entrou')