import pandas as pd
import numpy as np
#Vladimir Ariel Lizarro Velasquez
url='https://raw.githubusercontent.com/Uve-Lizarro/2do_Parcial_245_Vladimir_Lizarro/main/Iris.csv'
datos=pd.read_csv(url)
datos['species']=datos['species'].astype('category').cat.codes
x=datos.drop(columns=['species']).values
y=datos['species'].values
x=(x-x.mean(axis=0))/x.std(axis=0)
codigo=np.zeros((y.size, y.max()+1))
codigo[np.arange(y.size), y]=1
pesos=x.shape[1]
sesgos=codigo.shape[1]
salida=10
w1=np.random.randn(pesos, 10)*0.01
w2=np.random.randn(10, salida)*0.01
w3=np.random.randn(10, sesgos)*0.01
s1=np.zeros((1, salida))
s2=np.zeros((1, salida))
s3=np.zeros((1, sesgos))
b1=0.9
b2=0.999
ep=1e-8
aw1, bw1=np.zeros_like(w1), np.zeros_like(w1)
aw2, bw2=np.zeros_like(w2), np.zeros_like(w2)
aw3, bw3=np.zeros_like(w3), np.zeros_like(w3)
as1, bs1=np.zeros_like(s1), np.zeros_like(s1)
as2, bs2=np.zeros_like(s2), np.zeros_like(s2)
as3, bs3=np.zeros_like(s3), np.zeros_like(s3)
def funcion_escalon(x):
    return np.where(x>=0, 1, 0)
def entropia(p, x):
    return -np.mean(x*np.log(p))
tasaAprendizaje=0.2
generaciones=2000
for i in range(1, generaciones+1):
    z1=np.dot(x, w1)+s1
    a1=funcion_escalon(z1)
    z2=np.dot(a1, w2)+s2
    a2=funcion_escalon(z2)
    z3=np.dot(a2, w3)+s3
    a3=np.exp(z3)/np.sum(np.exp(z3), axis=1, keepdims=True)
    error=a3-codigo
    perdida=entropia(a3, codigo)
    graPesos3=np.dot(a2.T, error)
    graSesgos3=np.sum(error, axis=0, keepdims=True)
    graOculto2=np.dot(error, w3.T)*a2
    graPesos2=np.dot(a1.T, graOculto2)
    graSesgos2=np.sum(graOculto2, axis=0, keepdims=True)
    graOculto1=np.dot(graOculto2, w2.T)*a1
    graPesos1=np.dot(x.T, graOculto1)
    graSesgos1=np.sum(graOculto1, axis=0, keepdims=True)
    for (j, p, k, m) in zip([w1, w2, w3, s1, s2, s3],
                            [graPesos1, graPesos2, graPesos3, graSesgos1, graSesgos2, graSesgos3],
                            [aw1, aw2, aw3, as1, as2, as3],
                            [bw1, bw2, bw3, bs1, bs2, bs3]):
        k[:]=b1*k+(1-b1)*p
        m[:]=b2*m+(1-b2)*(p**2)
        aux1=k/(1-b1**i)
        aux2=m/(1-b2**i)
        j-=tasaAprendizaje*aux1/(np.sqrt(aux2)+ep)
z1=np.dot(x, w1)+s1
a1=funcion_escalon(z1)
z2=np.dot(a1, w2)+s2
a2=funcion_escalon(z2)
z3=np.dot(a2, w3)+s3
a3=np.exp(z3)/np.sum(np.exp(z3), axis=1, keepdims=True)
prediccion=np.argmax(a3, axis=1)
preciso=np.mean(prediccion==y)
print(f'Precision: {preciso}')