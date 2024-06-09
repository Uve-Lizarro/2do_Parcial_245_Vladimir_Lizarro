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
w1=np.random.randn(pesos, 5)
w2=np.random.randn(5, sesgos)
s1=np.zeros((1, 5))
s2=np.zeros((1, sesgos))
def funcion_sigmoide(x):
    return 1/(1+np.exp(-x))
def derivada_sigmoide(x):
    return x*(1-x)
def entropia(p, x):
    return -np.mean(x*np.log(p))
tasaAprendizaje=0.4
generaciones=10000
for i in range(0,generaciones+1):
    z1=np.dot(x, w1)+s1
    a1=funcion_sigmoide(z1)
    z2=np.dot(a1, w2)+s2
    a2=funcion_sigmoide(z2)
    error=a2-codigo
    perdida=entropia(a2, codigo)
    gradiente=error*derivada_sigmoide(a2)
    gradiente_Pesos=np.dot(gradiente, w2.T)
    gradiente_Sesgos=gradiente_Pesos*derivada_sigmoide(a1)
    w2-=tasaAprendizaje*np.dot(a1.T, gradiente)
    s2-=tasaAprendizaje*np.sum(gradiente, axis=0, keepdims=True)
    w1-=tasaAprendizaje*np.dot(x.T, gradiente_Sesgos)
    s1-=tasaAprendizaje*np.sum(gradiente_Sesgos, axis=0, keepdims=True)
z1=np.dot(x, w1)+s1
a1=funcion_sigmoide(z1)
z2=np.dot(a1, w2)+s2
a2=funcion_sigmoide(z2)
prediccion=np.argmax(a2, axis=1)
preciso=np.mean(prediccion==y)
print(f'Precision: {preciso}')
