class nodo:
    def __init__(self, idPersona,numCarrito):
        self.idPersona = idPersona
        self.numCarrito = numCarrito
        self.siguiente = None
        self.anterior = None

class cola():
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def agregar(self,idPersona,numCarrito):
        nuevo=nodo(idPersona, numCarrito)
        if (self.primero==None):
            self.primero=nuevo
        else:
            nuevo.anterior=self.ultimo
            self.ultimo.siguiente=nuevo
        self.ultimo=nuevo

    def imprimir(self):
        aux = self.primero
        while (aux != None):
            print(aux.idPersona)
            aux = aux.siguiente


    def pop(self):
        aux = self.primero
        if (aux.siguiente != None):
            self.primero = aux.siguiente
            aux.siguiente.anterior = None
        else:
            self.primero = None
            self.ultimo = None
        del aux

x=cola()
x.agregar(1,1)
x.agregar(2,2)
x.agregar(3,3)
x.imprimir()
x.pop()
x.pop()
print("----------------")
x.agregar(6,6)
x.imprimir()