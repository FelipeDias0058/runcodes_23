#Recebe o input do usuário
def f_input(lista):
    while True:
        n = int(input())
        if n == 0:
            break
        lista.append(n)

#Lê a qtd de itens na lista
def f_len(lista):
    count = 0
    for i in lista:
        count += 1
    return count

#Imprime a lista em ordem reversa
def f_reverse(lista):
    return lista[::-1]

#Mostra o menor número da lista
def f_min(lista):
    lista_o = lista[:]
    lista_o.sort()
    return lista_o[-1]

#Mostra o maior número da lista
def f_max(lista):
    lista_o = lista[:]
    lista_o.sort()
    return lista_o[0]

#Soma todos os itens na lista
def f_sum(lista):
    total = 0
    for i in lista:
        total += i
    return total

def main():

    lista = []
        
    #Entrada de Dados
    f_input(lista)
        
    comprimento = f_len(lista)
    revertido = f_reverse(lista)
    minimo = f_min(lista)
    maximo = f_max(lista)
    soma = f_sum(lista)

    #Saída de Dados
    print(lista)
    print(comprimento)
    print(revertido)
    print(maximo)
    print(minimo)
    print(soma)

if __name__ == '__main__':
    main()
    
