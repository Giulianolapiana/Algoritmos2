from mylinkedlist import *

#Implementar un algoritmo Contiene-Suma(A,n) que recibe una lista de enteros A y un entero n y devuelve True si existen en A un par de elementos que sumados den n. Analice el costo computacional.

vector = [1,2,3,4]
print(len(vector))
print(vector)

def contienesuma(A,n):
  cont = 1
  for i in range(len(A)-1):
    for j in range(cont,len(A)):
      if A[i]+(A[j]) == n:
        return True
    cont += 1  
  return False
  
print(contienesuma(vector,20))
