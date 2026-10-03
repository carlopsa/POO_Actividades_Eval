from producto import Producto


class Venta:

    def __init__(self, productos):
        self.productos = productos

    def calcular_subtotal(self):
        subtotal = 0

        for producto, cantidad in self.productos:
            subtotal += producto.get_precio() * cantidad

        return subtotal

    def calcular_iva(self):
        return self.calcular_subtotal() * Producto.IVA

    def cantidad_total_productos(self):
        cantidad_total = 0

        for producto, cantidad in self.productos:
            cantidad_total += cantidad

        return cantidad_total

    def calcular_descuento(self):
        total_con_iva = self.calcular_subtotal() + self.calcular_iva()

        if self.cantidad_total_productos() > 3:
            return total_con_iva * 0.20
        else:
            return 0

    def calcular_total(self):
        total_con_iva = self.calcular_subtotal() + self.calcular_iva()
        descuento = self.calcular_descuento()

        return total_con_iva - descuento

    def realizar_venta(self):
        for producto, cantidad in self.productos:
            if cantidad > producto.get_stock():
                return False

        for producto, cantidad in self.productos:
            producto.disminuir_stock(cantidad)

        return True