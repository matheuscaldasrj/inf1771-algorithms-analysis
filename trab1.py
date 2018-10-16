import math
import time
from random import randint
import random

ANDAR_CRITICO = 99
tentativas = 0
testeMaxTentativas = 0

# apenas verifica se no andar
# recebido o frasco quebraria
def testeQuebra(andar):
    global ANDAR_CRITICO
    global tentativas

    tentativas = tentativas + 1
    if andar >= ANDAR_CRITICO:
        return True
    return False

#1a e 1b
# recebe o numero de frascos (k)
# recebe o numero de andaresTotais (n)
# e o andarBase que eh o andar de inicio da busca
def generalizacao(k,n, andarBase):

    if k == 0:
        # 0 frascos, acabaram as tentativas
        return 1

    if k==1:
        # 1 fraco apenas
        passo = 1
    else:
        # > 1 frasco, vamos achar o intervalo
        passo = long( n ** (1. / k) )
        passo = passo ** (k-1)

    andar = 0
    while True:
        andar = andar + passo
        andarTestado = andarBase + andar
        quebrou = testeQuebra(andarTestado)
        if quebrou:
            antesDeQuebrar = andar - passo
            antesDeQuebrar = antesDeQuebrar + generalizacao(k-1, passo, andarTestado - passo)
            return antesDeQuebrar



# 1c
def buscaBinaria (vetor, inicio, fim, valorBuscado): 
    if fim >= inicio: 
        metade =  (fim - inicio)/2 + inicio
  
        if vetor[metade] == valorBuscado: 
            return metade 
          
        # vamos buscar na primeira metade
        elif vetor[metade] > valorBuscado: 
            return buscaBinaria(vetor, inicio, metade-1, valorBuscado) 
        # se nao, buscamos na segunda metdade
        else: 
            return buscaBinaria(vetor, metade+1, fim, valorBuscado) 
  
    else: 
        return -1



# baseado no numero de andares totais
# e de frascos recebido chama a funcao
# generalizacao
# metodo eh util caso queria printar para debug
# cada passo executado
def generateTests(totalFloors, frascos):
    global tentativas
    global ANDAR_CRITICO
    global testeMaxTentativas
    andarEncontrado = generalizacao(frascos,totalFloors,0)
    if tentativas > testeMaxTentativas:
        testeMaxTentativas = tentativas
    # print ANDAR_CRITICO, "==", andarEncontrado,  ", max tentativas deve ser: ", frascos* ( int( totalFloors ** (1. / frascos) ) ), ".Encontrou em ", tentativas, "tentativas"
    tentativas = 0



#  apenas le o arquivo recebido
#  e chama a funcao de generalizacao
#  vai ser testado com frascos, frascos*2, frascos*4
#  e assim por diante, ate o limite de 16 frascos
def readFiles(fileName, frascos):
    global ANDAR_CRITICO
    global testeMaxTentativas
    testeMaxTentativas = 0
    with open(fileName) as infile:
        content = infile.read().split()
        size = int(content[0])
        maxNumber = long (pow(2,size))
        print "==================== ", fileName, " - ", size , "bits ==========================="

        totalNumber = long (content[1])       
        while True:
            print "", frascos, " frascos"
            start_time = time.time()
            for index, number in enumerate(content):
                if index == 0 or index == 1:
                    continue
                else:
                    ANDAR_CRITICO = long(number,2)
                    # ANDAR_CRITICO = number
                    generateTests(maxNumber, frascos)
           
          
            mediaTempo = (time.time() - start_time) / totalNumber
            print "Media tempo: ", mediaTempo
            print "Max tentativas: ", testeMaxTentativas, ". O pior caso seria: ", frascos* ( (int) ( maxNumber ** (1. / frascos) ) )

            if frascos == 16:
                print "Chegou a 16 frascos. Teste finalizado para este arquivo \n\n"
                return 

            frascos = frascos * 2
            testeMaxTentativas = 0

  
global ANDAR_CRITICO
global tentativas
print "Questao 1a"

print "\n\n\n\n"
readFiles("bignum_32_01.dat",2)
readFiles("bignum_32_02.dat",2)

readFiles("bignum_64_01.dat",4)
readFiles("bignum_64_02.dat",4)

readFiles("bignum_128_01.dat",8)
readFiles("bignum_128_02.dat",8)

readFiles("bignum_192_01.dat",16)
readFiles("bignum_192_02.dat",16)

readFiles("bignum_256_01.dat",16)
readFiles("bignum_256_02.dat",16)



print "1c - Busca Binaria"
vetor = [ 1, 2, 7, 8, 10 ]
for x in range(1, 11):
    resultado = buscaBinaria(vetor, 0, len(vetor)-1, x) 
    if resultado == -1: 
        print x, "Nao encontrado"
    else: 
        print x, " encontrado na posicao ", resultado
