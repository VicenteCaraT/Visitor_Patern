from Ivisitable import Visitable
from Ivisitor import Visitor

class ProductoDescuento(Visitable):
    def __init__(self, precio):
        self.__precio = precio
    
    def accept(self, visitor: Visitor):
        return visitor.visit_descuento(self)

    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, nuevoPrecio):
        self.__precio = nuevoPrecio