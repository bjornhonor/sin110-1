import numpy as np

# Funcao que conta as colunas e linhas da matriz e cria uma string com as seguintes informacoes:
# nome_instancia + qntd_linhas + qntd_colunas
# Entrada: content = matriz gerada pelo numpy atravez do arquivo de texto | isnt = nome da instancia
# Saida: texto = string formatada com as informacoes nome_instancia + qntd_linhas + qntd_colunas


def cria_string(content, inst):
    rows, columns = content.shape
    texto = str(inst) + ',' + str(rows) + ',' + str(columns)
    return texto
