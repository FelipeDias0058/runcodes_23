#Entrada de dados, que são adicionados às listas
def f_AlturaLista(n):
    nome = []
    idade = []
    altura = []
    for i in range(n):
        nome.append(input())
        idade.append(int(input()))
        altura.append(float(input()))
    return nome, idade, altura

#Cálculo da média de alturas
def f_AlturaMedia(altura):
    media_altura = sum(altura)/len(altura)
    média = round(media_altura,2)
    return média

#Alunos com mais de 13 anos    
def f_Acima13(nome,idade,altura):
    nome_13 = []
    altura_13 = []
    for i in range(len(nome)):
        if idade[i] > 13:
            nome_13.append(nome[i])
            altura_13.append(altura[i])
    return nome_13, altura_13

#Alunos com altura abaixo da média
def f_Abaixo_Altura_Media(nome,altura,media):
    below_average = []
    for i in range(len(altura)):
        if altura[i] < media:
            below_average.append(nome[i])
    return below_average
    
def main():
    nome,idade,altura = f_AlturaLista(30)
    media = f_AlturaMedia(altura)
    maior_13, maior_13_1 = f_Acima13(nome,idade,altura)
    nome = f_Abaixo_Altura_Media(maior_13,maior_13_1,media)

    #Saída de Dados
    print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    print(*nome,sep='\n')


if __name__ == '__main__':
    main()

