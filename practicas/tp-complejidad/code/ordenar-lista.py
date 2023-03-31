from mylinkedlist import *
from algo1 import *
lista = [5,2,3,7,8,1]

def ordenar_lista(lista):
    if len(lista) <= 1:
        return lista
    
    medio = lista[len(lista) // 2]
    menores = []
    mayores = []
    
    for elemento in lista:
        if elemento < medio:
            menores.append(elemento)
        elif elemento > medio:
            mayores.append(elemento)
    
    menores_ordenados = ordenar_lista(menores)
    mayores_ordenados = ordenar_lista(mayores)
    
    return menores_ordenados + [medio] + mayores_ordenados

#crear un vector
def vector(longitud,elemento,vectoranterior):
  vector = Array(longitud+1, 0)
  for i in range (0,longitud):
    if i == len(vector)+1:
      vector[i] = elemento
    else:
      print(vector)
      vector[i] = vectoranterior[i]
  return vector 


def addvector(vector,elemento):
  
  for i in range(len(vector)+1):
    if i == len(vector):
      newvector = [elemento]
    else:
      newvector = [vector[i]]
  print(newvector)
  return newvector

vector(len(lista),1000,lista)
    
print(ordenar_lista(lista))