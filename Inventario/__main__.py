import funciones_inventario
import datetime


def mostrar_menu(): 
    print ('1. Registrar nuevo producto')
    print ('2. Vender producto')
    print ('3. Buscar producto por su codigo')
    print ('4. Cambiar la disponibilidad del producto ')
    print ('5. Productos vendidos en rango de fecha')
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



        
            
def main():
    productos = []
    ventas = []

    while True:
        while  True:
            try:
                mostrar_menu()
                opción = int(input('Digita la opción: '))
                if 0 <= opción <=7 :
                    break
                else: 
                    print ('MENSAJE: Debe digitar un número mayor o igual a cero.')
            except ValueError:
                print('ERROR: Debe digitar un número entero valido.')
        if opción == 0:
            break
        
        #opcion 1
        
        elif opción == 1: 
            while True: 
                id_producto = capturar_entero('Digita el ID de el producto nuevo')
                
                producto = buscar_producto(productos, id_producto)

                if producto is None:
                    break
                else:
                    print ('MENSAJE: Ya existe un producto con el ID digitado.')

            nombre_producto = capturar_cadena('Digita el nombre del nuevo producto')
            while True:
                precio_producto = capturar_real('Digita el precio del nuevo producto')
                
                if precio_producto > 0:
                    break
                else:
                    print ('MENSAJE: El precio del producto debe de ser mayor a 0 .') 

            while True:
                cantidad_producto = capturar_entero('Digita la cantidad del nuevo producto')

                if cantidad_producto > 0:
                    break
                else:
                    print ('MENSAJE: El precio del producto debe de ser mayor a 0 .')

            
            while True:
                print ('1. Disponible')
                print ('2. No disponible')
                disponible = capturar_entero('Digita la opción para la disponibilidad del producto')

                if disponible == 1 or disponible == 2:
                    disponible == 1 
                    break
                

            nuevo_producto = {'Id_producto': id_producto, 'nombre': nombre_producto, 'precio': precio_producto, 
            'cantidad': cantidad_producto,'disponible': disponible} 

            registrar_producto(productos, nuevo_producto)

            print ('MENSAJE: El producto ha sido creado exitosamente')

        #opcion 2

        if opcion == 2:
            if len(productos):
                while True: 
                    listar_producto(productos)
                    id_producto = capturar_entero('Digita el id del producto') 

                    producto = buscar_producto(producto, id_producto)

                    if producto:
                        break
                    else:
                        print ('MENSAJE: Debe de escribir un ID de producto existente')

                while True:
                    cantidad_producto = capturar_entero('Digita la cantidad del nuevo producto')

                    if cantidad_producto > 0:
                        if cantidad_producto <= producto['cantidad']:
                            break
                        else: 
                            print ('MENSAJE: No hay existencias suficientes para la venta. Solo tenemos {} unidades.'.
                            format(producto['cantidad ']))
                    else:
                        print ('MENSAJE: El precio del producto debe de ser mayor a 0 .')

                nueva_venta = {'Id_producto': id_producto, 'cantidad': cantidad_producto, 'total_sin_iva': producto
                ['precio'] * cantidad_producto}

                realizar_venta(ventas, nueva_venta)

                print ('MENSAJE: La venta se ha realizado exitosamente')
            else:
                print('MENSAJE: Aun no ha registrado ningun producto')

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
                        print ('MENSAJE: Debe de escribir un ID de producto existente')

                mostrar_datos_producto(producto)
            
            else:
                print ('MENSAJE: Aun no ha registrado ningun producto')

        elif opción == 4:
            if len(productos):
                while True: 
                    listar_producto(productos)
                    id_producto = capturar_entero('Digita el id del producto') 

                    producto = buscar_producto(producto, id_producto)

                    if producto:
                        break
                    else:
                        print ('MENSAJE: Debe de escribir un ID de producto existente')

                cambiar_estado_producto(producto)
                mostrar_datos_producto(producto)
            
            else:
                print ('MENSAJE: Aun no ha registrado ningun producto')

        #Opción 5

        
        elif opción == 5:
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
                    print ('MENSAJE: Aun no ha registrado ningun producto')


                    while True:
                        try:
                            fecha_final = capturar_cadena('Digite la fecha de final (AAAA-MM-DD)')

                            fecha_final = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
                            break

                        except ValueError:
                            print('ERROR: Debe digitar una fecha valida con el formato AAAA-MM-DD.')

                        print()

                    ventas_rango = ventas_rango_fecha(ventas, fecha_inicio, fecha_final)

                    if len(ventas_rango):
                        for v in ventas_rango:
                            mostrar_datos_venta(v)
                            print()
                    else:
                        print ('MENSAJE: El rango de fechas seleccionado no existe.')
                

            else:
                print ('MENSAJE: Aun no ha registrado ningun producto')

        #Opción 6 

        elif opcion == 6:
            if len(productos):
                if len(ventas):
                    productos_vendidos = top5_mas_vendidos(ventas)

                    for p in productos_vendidos:
                        mostrar_datos_venta_producto(p)

                else:
                    print ('MENSAJE: Aun no se ha efectuado ninguna venta')

            else:
                print ('MENSAJE: Aun no ha registrado ningun producto')


        #opcion 7

        elif opcion == 7:
            if len(productos):
                if len(ventas):
                    productos_vendidos = top5_menos_vendidos(ventas)

                    for p in productos_vendidos:
                        mostrar_datos_venta_producto(p)

                else:
                    print ('MENSAJE: Aun no se ha efectuado ninguna venta')

            else:
                print ('MENSAJE: Aun no ha registrado ningun producto')






    
    print()
    print('El programa ha finalizado.')


if __name__ == '__main__':
    main()