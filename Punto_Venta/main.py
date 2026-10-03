from ropa_dama import RopaDama
from ropa_caballero import RopaCaballero
from venta import Venta

ventas = []


producto1 = RopaDama("Vestido", "Vestidos", 60000, 5)

producto2 = RopaCaballero("Camisa", "Camisas", 35000, 10)

producto3 = RopaDama("Jean", "Pantalones", 250000, 8)

producto4 = RopaCaballero("Chaqueta", "Chaquetas", 450000, 6)


print("PRODUCTO 1")
print("Nombre:", producto1.nombre)
print("Categoría:", producto1.categoria)
print("Tipo:", producto1.tipo)
print("Precio:", producto1.get_precio())
print("Stock:", producto1.get_stock())

print()

print("PRODUCTO 2")
print("Nombre:", producto2.nombre)
print("Categoría:", producto2.categoria)
print("Tipo:", producto2.tipo)
print("Precio:", producto2.get_precio())
print("Stock:", producto2.get_stock())

print()

print("PRODUCTO 3")
print("Nombre:", producto3.nombre)
print("Categoría:", producto3.categoria)
print("Tipo:", producto3.tipo)
print("Precio:", producto3.get_precio())
print("Stock:", producto3.get_stock())

print()

print("PRODUCTO 4")
print("Nombre:", producto4.nombre)
print("Categoría:", producto4.categoria)
print("Tipo:", producto4.tipo)
print("Precio:", producto4.get_precio())
print("Stock:", producto4.get_stock())

print()

venta1 = Venta([
    (producto1, 2),
    (producto2, 2)
])

print("VENTA")
print("Cantidad total de productos:", venta1.cantidad_total_productos())
print("Subtotal:", venta1.calcular_subtotal())
print("IVA:", venta1.calcular_iva())
print("Descuento:", venta1.calcular_descuento())
print("Total:", venta1.calcular_total())

resultado = venta1.realizar_venta()

if resultado:
    print("Venta realizada correctamente")
else:
    print("No hay suficiente stock")

if resultado:
    ventas.append(venta1)

print("Stock después de la venta:", producto1.get_stock())


print()

venta2 = Venta([
    (producto3, 1),
    (producto4, 1)
])

print("VENTA 2")
print("Cantidad total de productos:", venta2.cantidad_total_productos())
print("Subtotal:", venta2.calcular_subtotal())
print("IVA:", venta2.calcular_iva())
print("Descuento:", venta2.calcular_descuento())
print("Total:", venta2.calcular_total())

resultado2 = venta2.realizar_venta()

if resultado2:
    print("Venta realizada correctamente")
else:
    print("No hay suficiente stock")
    
if resultado2:
    ventas.append(venta2)

print("Stock después de la venta:")
print("Jean:", producto3.get_stock())
print("Chaqueta:", producto4.get_stock())

print()
print("VENTAS REGISTRADAS:", len(ventas))

total_ventas = 0

for venta in ventas:
    total_ventas += venta.calcular_total()

print("Total de ventas:", total_ventas)

promedio_ventas = total_ventas / len(ventas)

print("Promedio de ventas:", promedio_ventas)

print()
print("PRODUCTOS VENDIDOS")

for venta in ventas:
    for producto, cantidad in venta.productos:
        print(producto.nombre, "=", cantidad)

productos_vendidos = {}

for venta in ventas:
    for producto, cantidad in venta.productos:
        if producto.nombre in productos_vendidos:
            productos_vendidos[producto.nombre] += cantidad
        else:
            productos_vendidos[producto.nombre] = cantidad

producto_mas_vendido = None
mayor_cantidad = 0

for nombre in productos_vendidos:
    if productos_vendidos[nombre] > mayor_cantidad:
        mayor_cantidad = productos_vendidos[nombre]
        producto_mas_vendido = nombre

print()
print("PRODUCTO MÁS VENDIDO:", producto_mas_vendido)
print("Cantidad vendida:", mayor_cantidad)

categorias = {}

for venta in ventas:
    for producto, cantidad in venta.productos:
        categoria = producto.categoria

        if categoria in categorias:
            categorias[categoria] += cantidad
        else:
            categorias[categoria] = cantidad

print()
print("VENTAS POR CATEGORÍA:")

for categoria in categorias:
    print(categoria, "=", categorias[categoria])

categoria_mas_vendida = None
mayor_cantidad = 0

for categoria in categorias:
    if categorias[categoria] > mayor_cantidad:
        mayor_cantidad = categorias[categoria]
        categoria_mas_vendida = categoria

print()
print("Categoría con más ventas:", categoria_mas_vendida)
print("Cantidad vendida:", mayor_cantidad)

ventas_por_tipo = {}

for venta in ventas:
    for producto, cantidad in venta.productos:
        tipo = producto.tipo

        if tipo in ventas_por_tipo:
            ventas_por_tipo[tipo] += cantidad
        else:
            ventas_por_tipo[tipo] = cantidad

print()
print("VENTAS POR TIPO:")

for tipo in ventas_por_tipo:
    print(tipo, "=", ventas_por_tipo[tipo])

cantidad_dama = ventas_por_tipo.get("Dama", 0)
cantidad_caballero = ventas_por_tipo.get("Caballero", 0)

if cantidad_dama > cantidad_caballero:
    print("Se vendieron más prendas de Dama")
elif cantidad_caballero > cantidad_dama:
    print("Se vendieron más prendas de Caballero")
else:
    print("Se vendió la misma cantidad de prendas de Dama y Caballero")
    
productos = [producto1, producto2, producto3, producto4]

precio_maximo = productos[0].get_precio()
precio_minimo = productos[0].get_precio()

for producto in productos:
    if producto.get_precio() > precio_maximo:
        precio_maximo = producto.get_precio()

    if producto.get_precio() < precio_minimo:
        precio_minimo = producto.get_precio()

print()
print("PRECIO MÁXIMO:", precio_maximo)
print("PRECIO MÍNIMO:", precio_minimo)

stock_maximo = productos[0].get_stock()
stock_minimo = productos[0].get_stock()

for producto in productos:
    if producto.get_stock() > stock_maximo:
        stock_maximo = producto.get_stock()

    if producto.get_stock() < stock_minimo:
        stock_minimo = producto.get_stock()

print()
print("STOCK MÁXIMO:", stock_maximo)
print("STOCK MÍNIMO:", stock_minimo)

print()
print("---- RESUMEN GENERAL ----")

print("Cantidad de productos registrados:", len(productos))
print("Cantidad de ventas realizadas:", len(ventas))
print("Total vendido:", total_ventas)
print("Promedio de ventas:", promedio_ventas)
print("Producto más vendido:", producto_mas_vendido)
print("Categoría más vendida:", categoria_mas_vendida)
print("Precio máximo:", precio_maximo)
print("Precio mínimo:", precio_minimo)
print("Stock máximo:", stock_maximo)
print("Stock mínimo:", stock_minimo)