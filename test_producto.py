import unittest
from producto import Producto
from productoServices import ProductoService
from repositorios import Repositorios
from parameterized import parameterized


class TestProducto(unittest.TestCase):
    maxDiff = None

    def test_uso_property(self):
        producto = Producto()
        producto.descripcion = 'acer A515'
        producto.precio = 500000
        producto.tipo = 'computadoras'
        producto.estado = "disponible"
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'acer A515',
                                                 '_precio': 500000,
                                                 '_tipo': 'computadoras',
                                                 '_estado': 'disponible',
                                                 })

    def test_constructor_con_valores_iniciales(self):
        producto = Producto("Lenovo 450", 300000, 'computadoras', "disponible")
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'Lenovo 450',
                                                 '_precio': 300000,
                                                 '_tipo': 'computadoras',
                                                 '_estado': 'disponible',
                                                 })

    @parameterized.expand([
            ("lenovo t490", 6000000, 'computadoras', "disponible"),
            ("samsung s10", 200000, 'celular', "disponible"),
            ("samsung s20", 400000, 'celular', "disponible"),
            ("acer", 6000500, 'computadoras', "disponible"),
            ("HP", 6000000, 'computadoras', "disponible"),
        ])
    # Agregar un producto
    def test_add_producto(
        self, descripcion, precio, tipo, estado
    ):
        producto = Producto(
            descripcion, precio, tipo, estado
        )
        productoKey = ProductoService().add_producto(producto)
        self.assertDictEqual(Repositorios.productosList[productoKey],
                             producto. __dict__)

    @parameterized.expand([
        ("ascendente", {0: {
                '_descripcion': 'samsung s10', '_precio': 200000,
                '_tipo': 'celular', "_estado": "disponible"
             }, 1: {
                '_descripcion': 'samsung s20', '_precio': 400000,
                '_tipo': 'celular', "_estado": "disponible"
             }, 2: {
                '_descripcion': 'lenovo t490', '_precio': 6000000,
                '_tipo': 'computadoras', "_estado": "disponible"
            }, 3: {
                '_descripcion': 'HP', '_precio': 6000000,
                '_tipo': 'computadoras', "_estado": "disponible"
            }, 4: {
                '_descripcion': 'acer', '_precio': 6000500,
                '_tipo': 'computadoras', "_estado": "disponible"
            }}),
        ("descendente", {0: {
                '_descripcion': 'acer', '_precio': 6000500,
                '_tipo': 'computadoras', "_estado": "disponible"
            }, 1: {
                '_descripcion': 'lenovo t490', '_precio': 6000000,
                '_tipo': 'computadoras', "_estado": "disponible"
            }, 2: {
                '_descripcion': 'HP', '_precio': 6000000,
                '_tipo': 'computadoras', "_estado": "disponible"
            }, 3: {
                '_descripcion': 'samsung s20', '_precio': 400000,
                '_tipo': 'celular', "_estado": "disponible"
            }, 4: {
                '_descripcion': 'samsung s10', '_precio': 200000,
                '_tipo': 'celular', "_estado": "disponible"
            }}),
    ])
    # Ordenar lista
    def test_insertion_sort_precio(self, tipo_orden, list_ordenada):
        lista_ordenada = ProductoService().\
            insertion_sort_precio(Repositorios.productosList, tipo_orden)
        self.assertDictEqual(lista_ordenada, list_ordenada)

    # Eliminar un producto
    def test_delete_producto(self):
        producto = Producto("HP", 45555, 'computadora', "disponible")
        productoKey = ProductoService().add_producto(producto)
        ProductoService().delete_producto(productoKey)
        self.assertEqual(Repositorios.productosList.get(productoKey), None)

    @parameterized.expand([
        (200000, {
                    '_descripcion': 'samsung s10',
                    '_precio': 200000, '_tipo': 'celular',
                    "_estado": "disponible"
        }),
        (400000, {
                    '_descripcion': 'samsung s20',
                    '_precio': 400000, '_tipo': 'celular',
                    "_estado": "disponible"
        }),
    ])
    # Busqueda binaria
    def test_busqueda_binaria(self, precio_buscado, producto):
        busqueda = ProductoService().\
            busqueda_binaria(Repositorios.productosList, precio_buscado)
        self.assertDictEqual(busqueda, producto)

    @parameterized.expand([
        ("lenovo t490", 6000000, 'computadoras', "disponible")
    ])
    # Verificar la exeptionfrom person import Person
    def test_delete_producto_value_error(
        self, descripcion, precio, tipo, estado
    ):
        long_list = len(Repositorios.productosList)
        with self.assertRaises(ValueError):
            ProductoService().delete_producto(long_list+1)

    @parameterized.expand([
        ("lenovo t490", -5000, 'computadoras', "disponible")
    ])
    def test_valor_negativo(self, descripcion, precio, tipo, estado):
        with self.assertRaises(ValueError):
            producto = Producto(descripcion, precio, tipo, estado)
            producto

    @parameterized.expand([({
        0: {'_descripcion': 'lenovo t490', '_precio': 6000000,
            '_tipo': 'computadoras', '_estado': 'disponible'
            },
        1: {'_descripcion': 'lenovo t490', '_precio': 6000000,
            '_tipo': 'computadoras', '_estado': 'disponible'}},
    )])
    def test_get_lista(self, repo):
        lista = ProductoService()\
            .get_lista_estado(Repositorios.productosList)
        self.assertDictEqual(lista, repo)


if __name__ == '__main__':
    unittest.main()
