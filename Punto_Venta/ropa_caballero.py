from producto import Producto


class RopaCaballero(Producto):

    def __init__(self, nombre, categoria, precio, stock):
        super().__init__(nombre, categoria, precio, stock)
        self.tipo = "Caballero"