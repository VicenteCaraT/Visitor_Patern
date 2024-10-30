from productoDescuento import ProductoDescuento
from productoNormal import ProductoNormal
from iva import IVA

producto1 = ProductoDescuento(100)
producto2 = ProductoNormal(100)

iva = IVA(1.21, 1.105)
result1 = producto1.accept(iva)
result2 = producto2.accept(iva)

print("IVA para Producto con Descuento:", result1)
print("IVA para Producto Normal:", result2)