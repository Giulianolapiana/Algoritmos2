class AVLTree:
	root = None

class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None
  height = None
  
#Ejercicio 1:
#rotateRight(Tree,avlnode) 
#Descripción: Implementa la operación rotación a la derecha 
#Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  derecha
#Salida: retorna la nueva raíz

def rotateRight(B,rotroot):
  newroot = rotroot.leftnode
  rotroot.leftnode = newroot.rightnode
  #
  if newroot.rightnode != None:
    newroot.rightnode.parent = rotroot
  newroot.parent = rotroot.parent

  if rotroot.parent == None:
    B.root = newroot
  else:
    if rotroot.parent.rightnode == rotroot:
      rotroot.parent.rightnode = newroot
    else:
      rotroot.parent.leftnode = newroot
  newroot.rightnode = rotroot
  rotroot.parent = newroot

#rotateRight(Tree,avlnode) 
#Descripción: Implementa la operación rotación a la derecha 
#Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  derecha
#Salida: retorna la nueva raíz

def rotateLeft(B,rotroot):
  newroot = rotroot.rightnode
  rotroot.rightnode = newroot.leftnode
  #
  if newroot.leftnode != None:
    newroot.leftnode.parent = rotroot
  newroot.parent = rotroot.parent

  if rotroot.parent == None:
    B.root = newroot
  else:
    if rotroot.parent.leftnode == rotroot:
      rotroot.parent.leftnode = newroot
    else:
      rotroot.parent.rightnode = newroot
  newroot.leftnode = rotroot
  rotroot.parent = newroot

#Ejercicio 2:
#calculateBalance(AVLTree) 
#Descripción: Calcula el factor de balanceo de un árbol binario de búsqueda. 
#Entrada: El árbol AVL  sobre el cual se quiere operar.
#Salida: El árbol AVL con el valor de balanceFactor para cada subarbol

#altura del arbol año pasado binary tree

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

######################################################################
#Funcion recursiva que busca la altura del arbol
def update_bf(root,height):
  if(root.rightnode == None and root.leftnode == None):
    return height
  else:
    if(root.leftnode != None):
      leftHeight = update_bf(root.leftnode,height+1)
    else:
      leftHeight = 0
    if(root.rightnode != None):
      rightHeight = update_bf(root.rightnode,height+1)
    else:
      rightHeight = 0
    if(leftHeight > rightHeight):
      return leftHeight
    else:
      return rightHeight
#########################################################
##########################################################


def calculateBalance(B):
  if B.root != None:
    calculateBalanceR(B.root)
  else:
    return


#Funcion recursiva que asigna el balanceFactor a cada nodo
def calculateBalanceR(newnode):
  if(newnode.leftnode != None):
    leftHeight = height(newnode.leftnode)
    calculateBalanceR(newnode.leftnode)
  else:
    leftHeight = 0
  if(newnode.rightnode != None):
    rightHeight = height(newnode.rightnode)
    calculateBalanceR(newnode.rightnode)
  else:
    rightHeight = 0
  newnode.bf = rightHeight - leftHeight

#Ejercicio 3:
#reBalance(AVLTree) 
#Descripción: balancea un árbol binario de búsqueda. Para esto se deberá primero calcular el balanceFactor del árbol y luego en función de esto aplicar la estrategia de rotación que corresponda.
#Entrada: El árbol binario de tipo AVL  sobre el cual se quiere operar.
#Salida: Un árbol binario de búsqueda balanceado. Es decir luego de esta operación se cumple que la altura (h) de su subárbol derecho e izquierdo difieren a lo sumo en una unidad.


def reBalance(B):
  calculateBalance(B)
  reBalanceR(B,B.root)


#Funcion recursiva encargada de realizar las rotaciones necesaria para hacer cumplir la condicion de AVL
def reBalanceR(B,newnode):
    if(newnode.bf <= -2):
      rotateRight(B,newnode.leftnode)
    elif(newnode.bf >= 2):
      rotateLeft(B,newnode.rightnode)
    else:
      if(newnode.leftnode != None):
        reBalanceR(B,newnode.leftnode)
      if(newnode.rightnode != None):
        reBalanceR(B,newnode.rightnode)
#Verificamos que se haya rotado correctamente, caso contrario volvemos a rotar



#Ejercicio 4:
#Implementar la operación insert() en  el módulo avltree.py garantizando que el árbol  binario resultante sea un árbol AVL

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
  newNode=AVLNode()
  newNode.key=key
  newNode.value=element
  if B.root==None:
    B.root=newNode
    return newNode.key
  else:
    current = B.root
    newNode=insertR(newNode,B.root)
  reBalance(B)
  return newNode
      
#Ejercicio 5:
#Implementar la operación delete() en  el módulo avltree.py garantizando que el árbol  binario resultante sea un árbol AVL.


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
    reBalance(B)  
    return currentNode.key

  #El nodo tiene un hijo a la izquierda.
  if currentNode.leftnode!=None and currentNode.rightnode==None:
    if currentNode.key<currentNode.parent.key: #Nodo a la izquierda del padre.
      currentNode.parent.leftnode=currentNode.leftnode
    else: #Nodo a la derecha del padre.
      currentNode.parent.rightnode=currentNode.leftnode
    reBalance(B)    
    return currentNode.key

  #El nodo tiene un hijo a la derecha.
  if currentNode.leftnode==None and currentNode.rightnode!=None:  
    if currentNode.key<currentNode.parent.key: #Nodo a la izquierda del padre.
      currentNode.parent.leftnode=currentNode.rightnode
    else: #Nodo a la derecha del padre.
      currentNode.parent.rightnode=currentNode.rightnode
    reBalance(B)    
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
    reBalance(B)  
    return oldkey

def MenordesusMayores(currentNode):
  if currentNode.leftnode!=None:
    return MenordesusMayores(currentNode.leftnode)
  else: #Si el nodo a su izquierda está vacío.
    return currentNode


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
      
