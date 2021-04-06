import funciones_inventario
import datetime
import os
import pickle



def mostrar_menu(): 
    print ('1. Registrar nuevo producto')
    print ('2. Vender producto')
    print ('3. Buscar producto por su codigo')
    print ('4. Cambiar la disponibilidad del producto ')
    print ('5. Productos vendidos en rango de fechas ')
    print ('6. Top 5 de los productos más vendidos')
    print ('7. Top 5 de los procutos menos vendidos')
    print ('0. Salir')



def capturar_entero(mensaje):           #Valida el ingreso de datos.(función axuliar)
    while True:
        try:
            numero = int(input(f'{mensaje}: '))

            return numero
    
        except ValueError:
            print ('ERROR: Debe digitar un número entero')


def capturar_real(mensaje):           #Valida el ingreso de datos.(función auxiliar)
    while True:
        try:
            numero = float(input(f'{mensaje}: '))

            return numero
    
        except ValueError:
            print ('ERROR: Debe digitar un número real')


def capturar_cadena(mensaje):           #Valida el ingreso de datos.(función auxiliar)
    while True:

        cadena = input(f'{mensaje}: ').strip()

    if len(cadena):
        return cadena
    else:
        print('MENSAJE: Debe de digitar una cadena de caracteres con texto.')


def listar_producto(producto):
    if p in productos:
        print (f"{p['id_producto']} - {p['nombre']}")       #muestra el nombre del producto

def continuar():
    print()
    print('Presiona enter para continuar . . . ', end='')
    input()
    print()



def cargar_inventario():
    while True:
        print('¿Desea cargar los datos del inventario y las ventas?')
        print('1. Sí ')
        print('2. No ')
        opcion = capturar_entero('Digita la opción')

        if opcion == 1 or opcion == 2 : 
            break

    if opcion == 1:
        with open('inventario/inventario.pickle', 'rb') as f:
            inventario = pickle.load(f)
            return inventario                                      
    return None


def guardar_datos(productos, ventas):
    while True:
        print("¿Desea cargar los datos de productos y ventas en el 'archivo.pickle'?: ")
        print('1. Sí ')
        print('2. No ')
        opcion = capturar_entero('Digita la opción')

        if opcion == 1 or opcion == 2 : 
            break

    if opcion == 1:
        with open('inventario/archivo.pickle', 'wb') as f:
            inventario = {'productos': productos, 'ventas': ventas}

            pickle.dump(inventario, f)
        return True
    else: 
        return False
            
def main():
    

    if os.path.isfile('inventario/inventario.pickle'):
        inventario = cargar_inventario()

        if inventario:
            productos = inventario['productos']                      
            ventas = inventario['ventas']

        else:
            productos = []
            ventas = []
    
    else:
        productos = []
        ventas = []

    while True:
        while  True:
            try:
                mostrar_menu()
                opcion = int(input('Digita la opción: '))
                if 0 <= opcion <=7 :
                    break
                else: 
                    print()
                    print ('MENSAJE: Debe digitar un número mayor o igual a 0 y menor o igual a 7.')
            except ValueError:
                print()
                print('ERROR: Debe digitar un número entero valido.')

            continuar()

        print()
            
        if opcion == 0:
            break
        
        #opcion 1
        
        elif opcion == 1: 
            while True: 
                id_producto = capturar_entero('Digita el ID de el producto nuevo')

                if id_producto >0 : 
                    producto = buscar_producto(productos, id_productos)

                    if producto is None:
                        break
                    else:
                        print()
                        print ('MENSAJE: Ya existe un producto con el ID digitado.')
                    continuar()

                else:
                    print()
                    print('MENSAJE: El ID del producto debe de ser un numero positivo')
                continuar()


            nombre_producto = capturar_cadena('Digita el nombre del nuevo producto')
            while True:
                precio_producto = capturar_real('Digita el precio del nuevo producto')
                
                if precio_producto > 0:
                    break
                else:
                    print ('MENSAJE: El precio del producto debe de ser mayor a 0 .')
                    print()


            while True:
                cantidad_producto = capturar_entero('Digita la cantidad del nuevo producto')

                if cantidad_producto > 0:
                    break
                else:
                    print ('MENSAJE: El precio del producto debe de ser mayor a 0 .')
                    print()

            
            while True:
                print ('1. Disponible')
                print ('2. No disponible')
                disponible = capturar_entero('Digita la opción para la disponibilidad del producto')

                if disponible == 1 or disponible == 2:
                    disponible == 1 
                    break
                else:
                    print()
                    print('MENSAJE: La opcion {} de disponibilidad no existe'.format(disponible))

                continuar()
                

            nuevo_producto = {'Id_producto': id_producto, 'nombre': nombre_producto, 'precio': precio_producto, 
            'cantidad': cantidad_producto,'disponible': disponible} 

            registrar_producto(productos, nuevo_producto)
            print()
            print ('MENSAJE: El producto ha sido creado exitosamente')

        #opcion 2

        elif opcion == 2:
            if len(productos):
                while True: 
                    listar_producto(productos)
                    id_producto = capturar_entero('Digita el id del producto') 

                    producto = buscar_producto(producto, id_producto)

                    if producto:
                        break
                    else:
                        print()
                        print ('MENSAJE: Debe de escribir un ID de producto existente')
                        

                while True:
                    cantidad_producto = capturar_entero('Digita la cantidad del producto')

                    if cantidad_producto > 0:
                        if cantidad_producto <= producto['cantidad']:
                            break
                        else: 
                            print ('MENSAJE: No hay existencias suficientes para la venta. Solo tenemos {} unidades.'.
                            format(producto['cantidad ']))
                    else:
                        print()
                        print ('MENSAJE: Debe de digitar una cantidad positiva para el producto.')
                    continuar()
                    


                nueva_venta = {'Id_producto': id_producto, 'cantidad': cantidad_producto, 'total_sin_iva': producto
                ['precio'] * cantidad_producto}

                realizar_venta(ventas, nueva_venta)

                print ('Total: $%.2f' % (nueva_venta['total_sin_iva'] * 1.19))

                print()
                print ('MENSAJE: La venta se ha realizado exitosamente')
            else:
                print()
                print('MENSAJE: Aun no ha registrado ningun producto')
            continuar()
                

        #Opcion 3

        elif opcion == 3:
            if len(productos):
                while True: 
                    listar_producto(productos)
                    id_producto = capturar_entero('Digita el id del producto') 

                    producto = buscar_producto(producto, id_producto)

                    if producto:
                        break
                    else:
                        print()
                        print ('MENSAJE: Debe de escribir un ID de producto existente')

                    continuar()

                mostrar_datos_producto(producto)
            
            else:
                print()
                print ('MENSAJE: Aun no ha registrado ningun producto')
                
        elif opcion == 4:
            if len(productos):
                while True: 
                    listar_producto(productos)
                    id_producto = capturar_entero('Digita el id del producto') 

                    producto = buscar_producto(producto, id_producto)

                    if producto:
                        break
                    else:
                        print()
                        print ('MENSAJE: Debe de escribir un ID de producto existente')

                    continuar()


                cambiar_estado_producto(producto)
                mostrar_datos_producto(producto)
            
            else:
                print()
                print ('MENSAJE: Aun no ha registrado ningun producto')
                

        #Opción 5

        
        elif opcion == 5:
            if len(productos):
                if len(ventas):
                    while True:
                        try:
                            fecha_inicio = capturar_cadena('Digite la fecha de inicio (AAAA-MM-DD)')

                            fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
                            break

                        except ValueError:
                            print('ERROR: Debe digitar una fecha valida con el formato AAAA-MM-DD.')
                        
                        
                        print()
                else:
                    print()
                    print ('MENSAJE: Aun no ha registrado ningun producto')
                    


                    while True:
                        try:
                            fecha_final = capturar_cadena('Digite la fecha de final (AAAA-MM-DD)')

                            fecha_final = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
                            break

                        except ValueError:
                            print()
                            print('ERROR: Debe digitar una fecha valida con el formato AAAA-MM-DD.')

                        print()

                    ventas_rango = ventas_rango_fecha(ventas, fecha_inicio, fecha_final)

                    if len(ventas_rango):
                        for v in ventas_rango:
                            mostrar_datos_venta(productos, v)
                            print()
                    else:
                        print()
                        print ('MENSAJE: El rango de fechas seleccionado no existe.')


            else:
                print()
                print ('MENSAJE: Aun no ha registrado ningun producto')

        #Opción 6 

        elif opcion == 6:
            if len(productos):
                if len(ventas):
                    productos_vendidos = top5_mas_vendidos(ventas)
                    print(productos_vendidos)

                    print('Top 5 de los productos mas vendidos ')
                    for p in productos_vendidos:
                        mostrar_datos_venta_producto(productos, p)
                        print()


                else:
                    print()
                    print ('MENSAJE: Aun no se ha efectuado ninguna venta')



            else:
                print()
                print ('MENSAJE: Aun no ha registrado ningun producto')



        #opcion 7

        elif opcion == 7:
            if len(productos):
                if len(ventas):
                    productos_vendidos = top5_menos_vendidos(ventas)

                    print('top 5 de los productos menos vendidos')
                    for p in productos_vendidos:
                        mostrar_datos_venta_producto(productos, p)
                        print()

                else:
                    print()
                    print ('MENSAJE: Aun no se ha efectuado ninguna venta')


            else:
                print()
                print ('MENSAJE: Aun no ha registrado ningun producto')




        continuar()


    print()

    if len(productos):
        if guardar_datos(productos, ventas):
            print ('Los datos del inventario (productos y ventas) se han guardado en disco.')
        else:
            print ('ha omitido almacenar los datos en disco.')

    print()


    print('El programa ha finalizado.')


if __name__ == '__main__':
    main()