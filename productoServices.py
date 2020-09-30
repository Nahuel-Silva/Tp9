from repositorios import Repositorios
from producto import Producto


class ProductoService():

    def get_productosList(self):
        return Repositorios.productosList

    def crearProducto(self):
        print("\n----Agregando producto----")
        descripcion = input('Ingrese una descripcion: ')
        precio = int(input('Ingrese un precio: '))
        tipo = input('Ingrese el tipo de producto: ')
        estado = input("Ingrese el estado del producto: ")
        return Producto(descripcion, precio, tipo, estado)

    def add_producto(self, producto=None):
        if producto is None:
            producto.crearProducto()
        lastKey = -1
        for productKey in Repositorios.productosList:
            lastKey = productKey
        lastKey = lastKey + 1
        Repositorios.productosList[lastKey] = producto.__dict__
        return lastKey

    def update_producto(self, key):
        num = 1
        while num != 0:
            num2 = 1
            if num2 == 1:
                print("-----Modificando-----")

                descripcion = input('Introduzca la nueva descripcion: ')
                Repositorios.productosList[key]["_descripcion"] = descripcion
                print(Repositorios.productosList)

                precio = int(input('Introduzca el nuevo precio: '))
                Repositorios.productosList[key]["_precio"] = precio
                print(Repositorios.productosList)

                tipo = input('Introduzca el nuevo tipo de producto: ')
                Repositorios.productosList[key]["_tipo"] = tipo
                print(Repositorios.productosList)

                estado = input('Introduzca el nuevo estado: ')
                Repositorios.productosList[key]["_estado"] = estado
                print(Repositorios.productosList)

            terminar = str(input("Quiere volver a corregirlo: "))
            if terminar == "no":
                break

    def delete_producto(self, key):
        if key not in Repositorios.productosList:
            raise ValueError("El legajo a eliminar no existe")
        del Repositorios.productosList[key]

    def insertion_sort_precio(self, lista, tipo_orden):
        lista_ordenada = lista.copy()
        if tipo_orden == "ascendente":
            for i in range(0, len(lista_ordenada)):
                valorNuevo = lista_ordenada[i]
                posicion = i - 1
                while posicion >= 0 and \
                    lista_ordenada[posicion]["_precio"] > \
                        valorNuevo["_precio"]:
                    lista_ordenada[posicion + 1] = lista_ordenada[posicion]
                    posicion = posicion - 1
                lista_ordenada[posicion + 1] = valorNuevo

        if tipo_orden == "descendente":
            for i in range(0, len(lista_ordenada)):
                valorNuevo = lista_ordenada[i]
                posicion = i - 1
                while posicion >= 0 and \
                    lista_ordenada[posicion]["_precio"] < \
                        valorNuevo["_precio"]:
                    lista_ordenada[posicion + 1] = lista_ordenada[posicion]
                    posicion = posicion - 1
                lista_ordenada[posicion + 1] = valorNuevo
        return lista_ordenada

    def busqueda_binaria(self, lista_ordenada, precio_buscado):
        lista_ordenada = self.insertion_sort_precio(
            lista_ordenada, "descendente"
        )
        medio = int(len(lista_ordenada)/2)
        while lista_ordenada[medio]["_precio"] != precio_buscado:
            if lista_ordenada[medio]["_precio"] < precio_buscado:
                medio = int(medio/2)
            if lista_ordenada[medio]["_precio"] > precio_buscado:
                medio += int(medio/2)
            if lista_ordenada[medio]["_precio"] == precio_buscado:
                return lista_ordenada[medio]

        lista_ordenada = self.insertion_sort_precio(
            lista_ordenada, "ascendente"
        )
        medio = int(len(lista_ordenada)/2)
        while lista_ordenada[medio]["_precio"] != precio_buscado:
            if lista_ordenada[medio]["_precio"] > precio_buscado:
                medio = int(medio/2)
            if lista_ordenada[medio]["_precio"] < precio_buscado:
                medio += int(medio/2)
            if lista_ordenada[medio]["_precio"] == precio_buscado:
                return lista_ordenada[medio]

    def get_lista_estado(self, lista):
        repositorio = dict()
        for i in lista:
            if lista[i]['_estado'] == 'disponible':
                repositorio[i] = lista[i]
        return repositorio
