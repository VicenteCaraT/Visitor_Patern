from Ivisitor import Visitor
from productoNormal import ProductoNormal
from productoDescuento import ProductoDescuento

class IVA(Visitor):
    def __init__(self, impuestoNormal, impuestoReducido):
        self.__impuestoNormal = impuestoNormal
        self.__impuestoReducido = impuestoReducido

    def visit_normal(self, normal: ProductoNormal):
        return normal.getPrecio() * self.__impuestoNormal

    def visit_descuento(self, reducido: ProductoDescuento):
        return reducido.getPrecio() * self.__impuestoReducido