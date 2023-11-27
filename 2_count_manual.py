#Recebe o input do usuário
def f_input(lista):
    while True:
        n = int(input("Digite os números da lista: "))
        if n == 0:
            break
        lista.append(n)

#Conta quantas vezes um elemento repete
def f_contagem(valor, lista):
    cont = 0
    for x in lista:
        if x == valor:
            cont += 1
        else: cont += 0
    return cont
            

def main():

    #Entrada de Dados
    lista = []
    f_input(lista)
    valor = int(input("Digite o valor a ser pesquisado: "))

    qtd_repeticoes = f_contagem(valor, lista)

    #Saída de Dados
    print(lista)
    print(valor)
    print(qtd_repeticoes)

if __name__ == '__main__':
    main()
