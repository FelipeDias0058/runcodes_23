def AListaInput(lista_a):
    for n in range(20):
        lista_a.append(int(input("Digite os 20 itens da lista A: ")))     
    
def BListaInput(lista_b):
    for n in range(20):
        lista_b.append(int(input("Digite os 20 itens da lista B: ")))


def main():

    lista_a = []
    lista_b = []

    #Entrada de Dados
    AListaInput(lista_a)
    BListaInput(lista_b)

    #Saída de Dados
    lista_c = [x + y for x, y in zip(lista_a, lista_b)]

    print(lista_a)
    print(lista_b)
    print(lista_c)
    

if __name__ == '__main__':
    main()
