#Entrada de Dados
def f_Jogador(n):
    lnome = []
    laltura  = []
    for i in range(n):
        lnome.append(input())
        laltura.append(float(input()))
    return lnome,laltura

def f_JogadorAltura(lnome,laltura):
    altura = 0
    nome = 0
    indice = 0
    altura = max(laltura)
    indice = laltura.index(altura)
    nome = lnome[indice]
    return nome,altura

#Cálculos das médias
def f_AlturaMedia(lista):
    media = 0
    altura = sum(lista)
    media = altura/len(lista)
    return media

def f_AcimaAMedia(lista,lista2,media):
    a_acima=[]
    n_acima=[]
    for i in range(len(lista)):
        if lista[i]> media:
            a_acima.append(lista2[i])
            n_acima.append(lista[i])
    return n_acima, a_acima
  
        
def main():
    var,var2 = f_Jogador(12)
    var3,var4 = f_JogadorAltura(var,var2)
    var5 = f_AlturaMedia(var2)
    var6,var7 = f_AcimaAMedia(var2,var,var5)

    #Saída de Dados
    print("JOGADOR MAIS ALTO DO TIME",var3,f'{var4:.2f}',sep="\n")
    print("ALTURA MÉDIA DO TIME",f'{var5:.2f}',sep='\n')
    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    for i in range(len(var6)):
        print(var7[i])
        print(f'{var6[i]:.2f}')
    
    
if __name__=="__main__":
    main()
