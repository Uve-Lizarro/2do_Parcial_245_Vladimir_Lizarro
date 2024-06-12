import random
import numpy as np
#Vladimir Ariel Lizarro Velasquez
distancia=np.array([
    [0, 2, 4, 3, 6, 0, 2],
    [2, 0, 2, 4, 3, 3, 3],
    [4, 2, 0, 4, 7, 3, 3],
    [3, 4, 4, 0, 7, 3, 3],
    [6, 3, 7, 7, 0, 4, 7],
    [0, 3, 3, 3, 4, 0, 2],
    [2, 3, 3, 3, 7, 2, 0]
])
def evaluaDistancia(v):
    s=0
    for i in range(len(v)):
        if (i==len(v)-1):
            s+=distancia[v[i],v[0]]
        else:
            s+=distancia[v[i],v[i+1]]
    return s
def evaluaMochila(pesObj, com):
    s=0
    for i in com:
        s+=pesObj[i]
    return s

def generaVecino(solucion, objetos):
    vecino=solucion[:]
    i=random.randint(0, len(solucion) - 1)
    j=random.choice([x for x in objetos if x not in solucion])
    vecino[i]=j
    return vecino
def acepta(sol_actual, sol_vecina, temp):
    if (sol_vecina<sol_actual):
        return True
    else:
        prob=np.exp((sol_actual-sol_vecina)/temp)
        return random.random()<prob
def recocidoSimulado(lim, pesos, objetos, te, re, n):
    sol=random.sample(objetos, len(objetos))
    peso=evaluaMochila(pesos, sol)
    dist=evaluaDistancia(sol)
    solFinal=sol[:]
    pesoFinal=peso
    distFinal=dist
    while (te>1):
        for i in range(n):
            vecino=generaVecino(sol, objetos)
            pesoVecino=evaluaMochila(pesos, vecino)
            if (pesoVecino<=lim):
                distVecina=evaluaDistancia(vecino)
                if (acepta(dist, distVecina, te)):
                    sol=vecino[:]
                    peso=pesoVecino
                    dist=distVecina
                    if (distVecina<distFinal):
                        solFinal=vecino[:]
                        pesoFinal=pesoVecino
                        distFinal=distVecina
        te*=re
    return solFinal, pesoFinal, distFinal
solucion=[1, 2, 3, 4, 5, 6, 0]
pesoMochila=15
objetos=[0, 1, 2, 3, 4, 5, 6]
pesos=[1, 2, 3, 1, 4, 5, 0]
te=1000
re=0.95
n=100
c, p, d=recocidoSimulado(pesoMochila, pesos, objetos, te, re, n)
print("Mejor combinación:", c)
print("Peso total:", p)
print("Distancia total:", d)