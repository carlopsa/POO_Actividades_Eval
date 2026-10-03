class Producto:
    IVA = 0.19

    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio
        self.__stock = stock

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    def aumentar_stock(self, cantidad):
        self.__stock += cantidad

    def disminuir_stock(self, cantidad):
        self.__stock -= cantidad