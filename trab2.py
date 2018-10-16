import random

def generateRandomMatrix(n, maxNum):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = random.randint(1,maxNum)

def adicionaOuSubtrai(matrizA, matrizB,  ehAdicao):
    n = len(matrizA)
    matrizC = [[0 for j in xrange(0, n)] for i in xrange(0, n)]


    for i in xrange(0, n):
        for j in xrange(0, n):
            if ehAdicao:
                matrizC[i][j] = matrizA[i][j] + matrizB[i][j]
            else:
                matrizC[i][j] = matrizA[i][j] - matrizB[i][j]
    return matrizC




def multiplicaMatrizes (matrizA, matrizB, n):
    # C matriz resultado
    C = [[0 for col in range(n)] for row in range(n)]
    print C

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += matrizA[i][k] * matrizB[k][j]
    return C

def zeraMatriz(n):
    return  [[0 for j in xrange(0, n)] for i in xrange(0, n)]

def divisaoEConquistaStrassen(A,B,N):
    n = len(A)

    if n == 1:
        return [ [A[0][0]*B[0][0]] ]

    n = n/2
    
    

    a = zeraMatriz(n)
    b = zeraMatriz(n)
    c = zeraMatriz(n)
    d = zeraMatriz(n)
    e = zeraMatriz(n)
    f = zeraMatriz(n)
    g = zeraMatriz(n)
    h = zeraMatriz(n)
    i = zeraMatriz(n)
    auxMatriz1 = zeraMatriz(n)
    auxMatriz2 = zeraMatriz(n)

    # pegando as 8 submatrizes
    for i in xrange(0, n):
        for j in xrange(0, n):
            a[i][j] = A[i][j]
            b[i][j] = A[i][j+n]
            c[i][j] = A[i+n][j]
            d[i][j] = A[i+n][j+n]

            e[i][j] = B[i][j]
            f[i][j] = B[i][j+n]
            g[i][j] = B[i+n][j]
            h[i][j] = B[i+n][j+n]

    #Agora que ja montamos as sub matrizes, vamos montar calcular p1,p2...p6

    #p1 = a * (f - h)
    auxMatriz1 = adicionaOuSubtrai(f, h, False)
    p1 = divisaoEConquistaStrassen(a,auxMatriz1,n)

    #p2 = (a+b)*h
    auxMatriz1 = adicionaOuSubtrai(a, b, True)
    p2 = divisaoEConquistaStrassen(auxMatriz1,h,n)

    #p3 = (c+d)*e
    auxMatriz1 = adicionaOuSubtrai(c, d, True)
    p3 = divisaoEConquistaStrassen(auxMatriz1,e,n)


    #p4 = d*(g-e)
    auxMatriz1 = adicionaOuSubtrai(g, e, False)
    p4 = divisaoEConquistaStrassen(d,auxMatriz1,n)

    
    #p5 = (a+d)*(e+h)
    auxMatriz1 = adicionaOuSubtrai(a, d, True)
    auxMatriz2 = adicionaOuSubtrai(e, h, True)
    p5 = divisaoEConquistaStrassen(auxMatriz1,auxMatriz2,n)

    #p6 = (b-d)*(g+h)
    auxMatriz1 = adicionaOuSubtrai(b, d, False)
    auxMatriz2 = adicionaOuSubtrai(g, h, True)
    p6 = divisaoEConquistaStrassen(auxMatriz1,auxMatriz2,n)

    #p7 = (a-c)*(e+f)
    auxMatriz1 = adicionaOuSubtrai(a, c, False)
    auxMatriz2 = adicionaOuSubtrai(e, f, True)
    p7 = divisaoEConquistaStrassen(auxMatriz1,auxMatriz2,n)

    # agora precisamos calcular a matriz resultado
    
    #c11
    auxMatriz1 = adicionaOuSubtrai(p5, p4, True)
    auxMatriz2 = adicionaOuSubtrai(auxMatriz1, p2, False)
    c11 = adicionaOuSubtrai(auxMatriz2, p6, True)

    #c12
    c12 = adicionaOuSubtrai(p1, p2, True)
    c21 = adicionaOuSubtrai(p3, p4, True)

    #c22
    auxMatriz1 = adicionaOuSubtrai(p1, p5, True)
    auxMatriz2 = adicionaOuSubtrai(auxMatriz1, p3, False)
    c22 = adicionaOuSubtrai(auxMatriz2, p7, False)
    print c22


    # vamos montar matriz resposta
    # 2*n pois no inicio do metodo
    # atualizamos o novo valor para n/2
    tamanhoPassoAnterior = 2*n
    res = [[0 for j in xrange(0, tamanhoPassoAnterior)] for i in xrange(0, tamanhoPassoAnterior)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            res[i][j] = c11[i][j]
            res[i][j + n] = c12[i][j]
            res[i + n][j] = c21[i][j]
            res[i + n][j + n] = c22[i][j]
    return res
    

print "Meu teste"
matrizA = [[2,4],[6,1]]
matrizB = [[1,2],[3,4]]
# res = multiplicaMatrizes(matrizA, matrizB, 2)
# res2 = adicionaOuSubtrai(matrizA, matrizB, False)
# print (res)
# print (res2)
# res3 = divisaoEConquistaStrassen(matrizA,matrizB,2)
# print "Responsta Strassen"
# print (res3)

matrizC = [[2,4,2,4],[6,1,3,5], [1,4,3,5],[5,2,1,0]]
matrizD = [[1,2,3,4],[0,4,6,2], [4,5,6,7],[1,0,2,1]]
res = multiplicaMatrizes(matrizC, matrizD, 4)
print res
res2 = divisaoEConquistaStrassen(matrizC,matrizD,4)
print res2