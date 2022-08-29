from Control.StringCreator import cria_string
from Control.TxtControl import le_arquivo, salva_arquivo

# Funcao main. Vai pegar o nome da instancia que o usuario digitar chamar a funcao para ler esse arquivo,
# depois criar a string que sera tanto printada no console quanto adicionada no arquivo csv
# Entrada: "instancia = nome da instancia digitado pelo usuario"
# Saida: texto = vai printar a string criada no console


def main():
    instancia = input("Digite o nome do arquivo: ")
    arq = le_arquivo(instancia)
    texto = cria_string(arq, instancia)
    print(texto)
    salva_arquivo(texto)


if __name__ == '__main__':
    main()
