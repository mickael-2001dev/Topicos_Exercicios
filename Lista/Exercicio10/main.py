
#def intercalar(vetor1, vetor2):

    #vetorIntercalado = []

    #for v1, v2 in zip(vetor1, vetor2):
        #vetorIntercalado.append(v1)
        #vetorIntercalado.append(v2)

    #return vetorIntercalado

def intercalar(lG):
    lI = []
    for i in range(len(lG) + 1):
        for j in range(len(lG)):
            lI.append(lG[j][i])
    return lI

vetor1 = []
vetor2 = []

for i in range(10):
    vetor1.append(input("Digite um valor pro vetor 1: "))
    vetor2.append(input("Digite um valor por vetor 2: "))

lG = []
lG.append(vetor1)
lG.append(vetor2)

vetorIntecalado = intercalar(lG)

print(vetorIntecalado)