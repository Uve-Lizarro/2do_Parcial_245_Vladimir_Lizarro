import random
import numpy as np
#Vladimir Ariel Lizarro Velásquez
distancia = np.array([
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
def generaVecinos(solucion, objetos):
    vecinos=[]
    for i in range(len(solucion)):
        for i in objetos:
            if (i not in solucion):
                vecino=solucion[:]
                vecino[i]=i
                vecinos.append(vecino)
    return vecinos
def busqueda(lim, pesos, objetos):
    sol=random.sample(objetos, len(objetos))
    comb=sol
    peso=evaluaMochila(pesos, comb)
    dist=evaluaDistancia(comb)
    while (True):
        vecinos=generaVecinos(sol, objetos)
        mejora=False
        for i in vecinos:
            aux=evaluaMochila(lim, pesos, i)
            if (aux<=lim):
                valor_actual=evaluaDistancia(i)
                if (valor_actual<dist):
                    comb=i
                    peso=aux
                    dist=valor_actual
                    mejora=True
        
        if (mejora):
            sol=comb
        else:
            break
    return comb, peso, dist
solucion=[1, 2, 3, 4, 5, 6, 0]
pesoMochila = 15
objetos = [0, 1, 2, 3, 4, 5, 6]
pesos = [1, 2, 3, 1, 4, 5, 0]
c,p,d=busqueda(pesoMochila, pesos, objetos)
print("Mejor combinación:", c)
print("Peso total:", p)
print("Distancia total:", d)