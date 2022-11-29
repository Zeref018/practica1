# crea una clase llamada Producto
# nombre, unidades y precio
# creas un producto camisa, 10, 9.95 de precio
# muestra el nombre de producto por consola
class Producto:
    def __init__(self, nombre, unidades, precio):
        self.nombre = nombre
        self.unidades = unidades
        self.precio = precio

    def mostrar(self):
        print(f'el nombre es: {self.nombre}')

    def infoProducto(self):
        print(f'nombre: {self.nombre}, unidades: {self.unidades}, precio: {self.precio}')
        print(f'inventario valorado: {self.unidades * self.precio}')


producto1 = Producto('camisa', 10, 9.95)
producto1.mostrar()
producto1.infoProducto()


# crea un método de infoProducto. Muestra el nombre, unidades, precio y inventario valorado (uxp)

# práctica de sobreescritura.
# crea una clase llamada Servicio
# tiene un método llamado consultarDetalle que muestra. el servicio es básico.
# la empresa tiene dos servicios. estándar y premium. Son dos clases que derivan de Servicio
# la clase Estandar y Premium tienen un método llamado consultarDetalle y explican que son
# servicio estándar y premium respectivamente.
# pide por consola un servicio. Elegimos premium y te muestra el resultado de consultarDetalle

class Servicio:
    def consultarDetalle(self):
        print('el servicio es basico')


class Estandar(Servicio):
    def consultarDetalle(self):
        print('servicio estandar')


class Premium(Servicio):
    def consultarDetalle(self):
        print('servicio premium')


producto2 = Premium()
producto2.consultarDetalle()
