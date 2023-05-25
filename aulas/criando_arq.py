import os
# Criando arquivos no windows
# Modos:
    # r (leitura), w (escrita/cria), x (para criação)
    # a (escreve ao final), b (binário)
    # t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis:
    # write, read (escrever e ler)
    # writelines (escrever várias linhas)
    # seek (move o cursor)
    # readline (ler linha)
    # readlines (ler linhas)

# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

# M�dulo json, mas:
    # json.dump = Gera um arquivo json
    # json.load

# caminho_arquivo = 'C:\\Users\\Liara\Documents\\Curso Python\\Nova pasta atencao'
caminho_arquivo = 'aula01.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Atenção\n')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

# os.unlink(caminho_arquivo)