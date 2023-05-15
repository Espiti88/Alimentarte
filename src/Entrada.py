from src.Gestion.AdminCategorias import AdminCategorias
from src.Gestion.AdminClientes import AdminClientes
from src.Gestion.AdminPedidos import AdminPedidos
from src.Gestion.AdminPlatos import AdminPlatos
from src.Gestion.AdminRestaurantes import AdminRestaurantes
from src.Gestion.Consultas import Consultas

class Entrada:

    def __init__(self):
        print('Objeto tipo Entrada creado y listo para usarse..!!')
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:
            print('==================================')
            print('............OPCIONES..............')
            print('==================================')
            print('0. SALIR')
            print('1. CATEGORIAS')
            print('2. CLIENTES')
            print('3. PEDIDOS')
            print('4. PLATOS')
            print('5. RESTAURANTES')
            print('6. CONSULTAS')

            opcion = int(input('Digite su opción: '))

            if opcion == 0:
                print("Adios ..!!")

            elif opcion == 1:
                AdminCategorias()

            elif opcion == 2:
                AdminClientes()

            elif opcion == 3:
                AdminPedidos()

            elif opcion == 4:
                AdminPlatos()

            elif opcion == 5:
                AdminRestaurantes()

            elif opcion == 6:
                Consultas()

            else:
                print('Esa opción NO existe..!!!')


Entrada()
