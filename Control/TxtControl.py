import numpy as np

# Funcao que le um arquivo dentro da pasta /home/bcarrara/Documentos/a/datasets/, recebendo seu nome (instancia) como parametro,
# a fim acertar o caminho
# Entrada: instancia = nome do arquivo desejado
# Saida: data = conteudo do arquivo aberto em formato de matriz pelo numpy
n = 0

def le_arquivo(instancia):
    path = '/home/bcarrara/Documentos/a/datasets/' + str(instancia) + '.txt'
    with open(path, 'rb') as f:
        n = len(f.readlines())

    with open(path, 'rb') as f:
        data = np.genfromtxt(f, dtype="int32", max_rows=int(n))
    return data

# Funcao que recebe um conteudo e o adiciona dentro de um arquivo CSV
# Entrada: cont = string com o conteudo formatado para salvar no arquivo
# Saida: Nao possui saida


def salva_arquivo(cont):
    arq = open('/home/bcarrara/Documentos/a/results/results.csv', 'a+')
    arq.writelines(cont + '\n')
    arq.close()
