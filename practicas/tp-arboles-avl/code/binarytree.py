from mylinkedlist import *
from myqueue import *

class BinaryTree:
  root=None

class BinaryTreeNode:
  key=None
  value=None
  leftnode=None
  rightnode=None
  parent=None

#search(B,element)
#Descripción: Busca un elemento en el TAD árbol binario.
#Entrada: El árbol binario B en el cual se quiere realizar la búsqueda (BinaryTree) y el valor del elemento (element) a buscar.
#Salida: Devuelve la key asociada a la primera instancia del elemento. Devuelve None si el elemento no se encuentra.

def searchR(currentNode,element):
  if currentNode==None:
    return None
  if currentNode.value==element:
    return currentNode
  #Busqueda por el lado izquierdo
  left=searchR(currentNode.leftnode,element)
  if left!=None: #Si encuentra el elemento por el lado izquierdo
    return left
  #Busca por el lado derecho si no lo encuentra en el izquierdo
  return searchR(currentNode.rightnode,element)

def search(B,element):
  if B.root==None:
    return None
  Node=searchR(B.root,element)
  if Node==None:
    return None  
  return Node.key
  
#insert(B,element,key)
#Descripción: Inserta un elemento con una clave determinada del TAD árbol binario.
#Entrada: El árbol B sobre el cual se quiere realizar la inserción (BinaryTree), el valor del elemento (element) a insertar y la clave (key) con la que se lo quiere insertar.
#Salida: Si pudo insertar con éxito devuelve la key donde se inserta el elemento. En caso contrario devuelve None.

def insertR(newNode,currentNode):
  if newNode.key<currentNode.key:
    if currentNode.leftnode==None:
      newNode.parent=currentNode
      currentNode.leftnode=newNode
      return newNode
    else:
      return insertR(newNode,currentNode.leftnode)
  elif newNode.key>currentNode.key:
    if currentNode.rightnode==None:
      newNode.parent=currentNode
      currentNode.rightnode=newNode
      return newNode
    else:
      return insertR(newNode,currentNode.rightnode)
  else: #newNode.key==currentNode.key es decir la clave ya existe.
    return None 

def insert(B,element,key):
  newNode=BinaryTreeNode()
  newNode.key=key
  newNode.value=element
  if B.root==None:
    B.root=newNode
    return newNode.key
  else:
    newNode=insertR(newNode,B.root)
    if newNode!=None:
      return newNode.key
    else:
      return None
      
#delete(B,element)
#Descripción: Elimina un elemento del TAD árbol binario.
#Poscondición: Se debe desvincular el Node a eliminar.
#Entrada: El árbol binario B sobre el cual se quiere realizar la eliminación (BinaryTree) y el valor del elemento (element) a eliminar.
#Salida: Devuelve clave (key) del elemento a eliminar. Devuelve None si el elemento a eliminar no se encuentra.

def delete(B,element):
  currentNode=searchR(B.root,element)
  if currentNode==None: 
    return None

  #El elemento a eliminar es una hoja.
  if currentNode.leftnode==None and currentNode.rightnode==None:
    if currentNode.key<currentNode.parent.key: #Nodo a la izquierda del padre.
      currentNode.parent.leftnode=currentNode.leftnode
    else: #Nodo a la derecha del padre.
      currentNode.parent.rightnode=currentNode.rightnode
    return currentNode.key

  #El nodo tiene un hijo a la izquierda.
  if currentNode.leftnode!=None and currentNode.rightnode==None:
    if currentNode.key<currentNode.parent.key: #Nodo a la izquierda del padre.
      currentNode.parent.leftnode=currentNode.leftnode
    else: #Nodo a la derecha del padre.
      currentNode.parent.rightnode=currentNode.leftnode
    return currentNode.key

  #El nodo tiene un hijo a la derecha.
  if currentNode.leftnode==None and currentNode.rightnode!=None:  
    if currentNode.key<currentNode.parent.key: #Nodo a la izquierda del padre.
      currentNode.parent.leftnode=currentNode.rightnode
    else: #Nodo a la derecha del padre.
      currentNode.parent.rightnode=currentNode.rightnode
    return currentNode.key

  #El nodo tiene dos hijos. 
  if currentNode.leftnode!=None and currentNode.rightnode!=None:
    
    newNode=currentNode.rightnode #Menor de sus mayores.
    newNode=MenordesusMayores(newNode)

    oldkey=currentNode.key
    
    currentNode.key=newNode.key
    currentNode.value=newNode.value 
    #Se desvincula el nodo menor de sus mayores.
    newNode.parent.leftnode=newNode.leftnode #Sabemos que a su izquierda no hay ningún nodo.
    return oldkey

def MenordesusMayores(currentNode):
  if currentNode.leftnode!=None:
    return MenordesusMayores(currentNode.leftnode)
  else: #Si el nodo a su izquierda está vacío.
    return currentNode

#deleteKey(B,key)
#Descripción: Elimina una clave del TAD árbol binario.
#Poscondición: Se debe desvincular el Node a eliminar.
#Entrada: El árbol binario B sobre el cual se quiere realizar la eliminación (BinaryTree) y el valor de la clave (key) a eliminar.
#Salida: Devuelve clave (key) a eliminar. Devuelve None si el elemento a eliminar no se encuentra.

def deleteKey(B,key):
  currentNode=accessR(B.root,key)
  if currentNode==None: 
    return None

  #El elemento a eliminar es una hoja.
  if currentNode.leftnode==None and currentNode.rightnode==None:
    if currentNode.key<currentNode.parent.key: #Está a la izquierda del padre.
      currentNode.parent.leftnode=currentNode.leftnode
    else: #A la derecha del padre.
      currentNode.parent.rightnode=currentNode.rightnode
    return currentNode.value

  #El nodo tiene un hijo a la izquierda.
  if currentNode.leftnode!=None and currentNode.rightnode==None:
    if currentNode.key<currentNode.parent.key: #A la izquierda del padre.
      currentNode.parent.leftnode=currentNode.leftnode
    else:
      currentNode.parent.rightnode=currentNode.rightnode
    return currentNode.value

  #El nodo tiene un hijo a la derecha.
  if currentNode.leftnode==None and currentNode.rightnode!=None:  
    if currentNode.key<currentNode.parent.key:
      currentNode.parent.leftnode=currentNode.leftnode
    else:
      currentNode.parent.rightnode=currentNode.rightnode
    return currentNode.value

  #El nodo tiene dos hijos. 
  if currentNode.leftnode!=None and currentNode.rightnode!=None:
    newNode=currentNode.rightnode #Menor de sus mayores.
    newNode=MenordesusMayores(newNode)
    oldvalue=currentNode.value
    currentNode.key=newNode.key
    currentNode.value=newNode.value 
    #Se desvincula el nodo menor de sus mayores.
    newNode.parent.leftnode=newNode.leftnode #Sabemos que a su izquierda no hay ningún nodo.
    return oldvalue

def MenordesusMayores(currentNode):
  if currentNode.leftnode!=None:
    return MenordesusMayores(currentNode.leftnode)
  else: #Si el nodo a su izquierda está vacío.
    return currentNode

#access(B,key)
#Descripción: Permite acceder a un elemento del árbol binario con una clave determinada.
#Entrada: El árbol binario (BinaryTree) y la key del elemento al cual se quiere acceder.
#Salida: Devuelve el valor de un elemento con una key del árbol binario, devuelve None si no existe elemento con dicha clave.

def accessR(currentNode,key):
  if key<currentNode.key:
    if currentNode.leftnode==None:
      return None
    else:
      return accessR(currentNode.leftnode,key)
  elif key>currentNode.key:
    if currentNode.rightnode==None:
      return None
    else:
      return accessR(currentNode.rightnode,key)
  else:
    return currentNode

def access(B,key):
  if B.root==None:
    return None
  Node=accessR(B.root,key) 
  if Node==None:
    return None
  return Node.value 

#update(B,element,key)
#Descripción: Permite cambiar el valor de un elemento del árbol binario con una clave determinada.
#Entrada: El árbol binario (BinaryTree) y la clave (key) sobre la cual se quiere asignar el valor de element.
#Salida: Devuelve None si no existe elemento para dicha clave. Caso contrario devuelve la clave del nodo donde se hizo el update.

def update(B,element,key):
  currentNode=accessR(B.root,key)
  if currentNode==None:
    return None
  currentNode.value=element
  return currentNode.key

#traverseInOrder(B)
#Descripción: Recorre un árbol binario en orden.
#Entrada: El árbol binario (BinaryTree).
#Salida: Devuelve una lista (LinkedList) con los elementos del árbol en orden. Devuelve None si el árbol está vacío.

def traverseInOrderR(L,currentNode):
  if currentNode!=None:
    traverseInOrderR(L,currentNode.rightnode) #Empieza por el lado derecho porque add agrega al ppio de la lista.
    add(L,currentNode.value)
    traverseInOrderR(L,currentNode.leftnode)

def traverseInOrder(B):
  if B.root==None:
    return None
  L=LinkedList()
  traverseInOrderR(L,B.root)
  return L
  
#traverseInPostOrder(B)
#Descripción: Recorre un árbol binario en post-orden.
#Entrada: El árbol binario (BinaryTree).
#Salida: Devuelve una lista (LinkedList) con los elementos del árbol en post-orden. Devuelve None si el árbol está vacío.

def traverseInPostOrderR(L,currentNode):
  if currentNode!=None:        
    add(L,currentNode.value)
    traverseInPostOrderR(L,currentNode.rightnode)
    traverseInPostOrderR(L,currentNode.leftnode)

def traverseInPostOrder(B):
  if B.root==None:
    return None
  L=LinkedList()
  traverseInPostOrderR(L,B.root)
  return L

#traverseInPreOrder(B)
#Descripción: Recorre un árbol binario en pre-orden.
#Entrada: El árbol binario (BinaryTree).
#Salida: Devuelve una lista (LinkedList) con los elementos del árbol en pre-orden. Devuelve None si el árbol está vacío.

def traverseInPreOrderR(L,currentNode):
  if currentNode!=None:
    traverseInPreOrderR(L,currentNode.rightnode)
    traverseInPreOrderR(L,currentNode.leftnode)
    add(L,currentNode.value)

def traverseInPreOrder(B):
  if B.root==None:
    return None
  L=LinkedList()
  traverseInPreOrderR(L,B.root)
  return L
  
#traverseBreadthFirst(B)
#Descripción: Recorre un árbol binario en modo primero anchura/amplitud.
#Entrada: El árbol binario (BinaryTree).
#Salida: Devuelve una lista (LinkedList) con los elementos del árbol ordenados de acuerdo al modo primero en amplitud. Devuelve None si el árbol está vacío.

def traverseBreadFirst(B):
  L=LinkedList()
  Q=LinkedList()
  enqueue(Q,B.root)
  while length(Q) > 0:
    Node=dequeue(Q)
    add(L,Node.value)
    if Node.leftnode!=None:
      enqueue(Q,Node.leftnode)
    if Node.rightnode!=None:
      enqueue(Q,Node.rightnode)
  invertir(L)
  return L

#------------------------------------------------------------------------------


#verifica que un arbol este balanceado
    
def CheckBalancedBinaryTree(root):
    #si el árbol está vacío, devuelve True
    if root==None:
      return True
    #verificar la altura del subárbol izquierdo
    lheight= heightR(root.leftnode)
    rheight = heightR(root.rightnode)
    #si la diferencia de altura es mayor que 1, devuelve Falso
    if(abs(lheight-rheight)>1):
        return False
    #comprobar si el subárbol izquierdo está equilibrado
    lcheck=CheckBalancedBinaryTree(root.leftnode)
    #comprobar si el subárbol derecho está equilibrado
    rcheck=CheckBalancedBinaryTree(root.rightnode)
    #si ambos subárboles están equilibrados, devuelve True
    if lcheck==True and rcheck==True:
        return True
    else:
        return False




#determina la altura del arbol
def heightR(newnode):
    #si la raíz es None devuelve 0
        if newnode==None:
          return 0
        #encontrar la altura del subárbol izquierdo
        hleft=heightR(newnode.leftnode)
        #encontrar la altura del subárbol derecho
        hright=heightR(newnode.rightnode)  
        #encuentre el máximo de hleft y hright, agregue 1 y devuelva el valor
        if hleft>hright:
            return hleft+1
        else:
            return hright+1


def height(B):
  if B.root == None:
    return
  else:
    return(heightR(B.root))


#Sean BT1 y BT2 dos árboles binarios, donde BT1 es mayor (mayor cantidad de nodos) que BT2.Implementar un algoritmo que determine si BT2 es un subárbol de BT1.

def contadorR(newnode):
  if newnode==None:
    return 0
  return 1 + contadorR(newnode.rightnode) + contadorR(newnode.leftnode)


def subarbol(BT1,BT2):
  #chequeamos cual que el arbol bt1 sea mas grande que bt2
  if contadorR(BT1.root) < contadorR(BT2.root):
    return None
  else:
    LBT1 = traverseInPreOrder(BT1)
    LBT2 = traverseInPreOrder(BT2)
    #Comparamos las dos listas que coincidan todos los elementos, y en el mismo orden
    current = LBT1.head
    coincidencias = length(LBT2)
    contador = 0
    #se ponen en dos bucles y se comparan
    for i in range(0,length(LBT1)):
      newnode = LBT2.head
      #el contador tiene que tener el mismo valor de la dimension del arbol mas chico
      for i in range(0,length(LBT2)):
        if newnode.value == current.value:
          contador += 1
          current = current.nextNode 
          if contador == coincidencias:
            return True
        else:  
          contador = 0
        if i != length(LBT2)-1:  
          newnode = newnode.nextNode
      #eliminamos la head para que no se vuelva a repetir y vaya cambiando de posicion current     
      if i != length(LBT1)-1:
        current = current.nextNode  
        deleteposition(LBT1,0)
        current = LBT1.head
    return False



#Escribir una función checkBST(B) que verifique que un árbol binario es un Árbol Binario de Búsqueda.Es decir que se cumple la propiedad : leftnode < currentnode < rightnode.
#Nota: es posible implementar una versión cuya complejidad sea O(n).

def traverseInOrderkeyR(L,currentNode):
  if currentNode!=None:
    traverseInOrderkeyR(L,currentNode.rightnode) #Empieza por el lado derecho porque add agrega al ppio de la lista.
    add(L,currentNode.key)
    traverseInOrderkeyR(L,currentNode.leftnode)

def traverseInOrderkey(B):
  if B.root==None:
    return None
  L=LinkedList()
  traverseInOrderR(L,B.root)
  return L

def checkBST(B):
  BT1 = traverseInOrderkey(B)
  newnode = BT1.head
  while newnode.nextNode != None:
    if newnode.value > newnode.nextNode.value:
      return False
    newnode = newnode.nextNode
  return True  