import datetime
from collections import Counter

def registrar_producto(productos,producto):
    productos.appen(producto)


def realizar_venta(ventas, venta):
    venta["fecha"] = datetime.now()
    venta.append(venta)

def buscar_producto(productos, id_productos):
    
    for p in productos:
        if p["id_productos"] == id_productos:
            return p 
        
    return None 

def cambiar_estado_producto(produto, nuevo_estado):

    produto['Disponible'] =  not produto['Disponible']


def ventas_rango_fecha(ventas, fecha_inicio, fecha_final):

    for v in ventas:
        if fecha_inicio <= v ['fecha'] <= fecha_final: 
            ventas_rango.append(v)

    return ventas_rango


def top5_mas_vendidos(ventas):
    conteo_ventas = {}

    for v in ventas:

        for v['id_producto'] in conteo_ventas:
            conteo_ventas[v['id_producto']] += v['cantidad']
        else:
            conteo_ventas[v['id_producto']] = v['cantidad']

    conteo_ventas = {key: valor for key, v in sorted(conteo_ventas.items(), key=lambda item: item[1], reversed=True) }  #realiza el ordenamiento de mayor a menor. 


    contador = Counter(conteo_ventas)
    
    return contador.most_common(5)  
                                        #.most_common = retorna los elementos que mas se repiten de una tupla.


def top5_menos_vendidos(ventas):
    conteo_ventas = {}

    for v in ventas:

        for v['id_producto'] in conteo_ventas:
            conteo_ventas[v['id_producto']] += v['cantidad']
        else:
            conteo_ventas[v['id_producto']] = v['cantidad']

    conteo_ventas = {key: valor for key, v in sorted(conteo_ventas.items(), key=lambda item: item[1]) }

    contador = Counter(conteo_ventas)
    
    return contador.most_common()[:-6:-1]

def mostrar_datos_producto(producto):
    print ('ID: %i' %producto['id_producto'])
    print ('Nombre: %s' %producto['nombre'])
    print ('Nombre: $%.2f' %producto['precio'])
    print ('Cantidad: %i' %producto['cantidad'])
    print ('¿Disponible?')
    if producto == 1:
        print ('Sí')
    else:
        print ('No')



def mostrar_datos_venta(ventas):
    print ('ID producto: %i' %venta['id_producto'])
    print ('Fecha: %s' %venta['nombre'])
    print ('Cantidad: $%i' %venta['cantidad'])
    print ('Total sin IVA: $%.2f' %venta['total_sin_IVA'])
    print ('Total: $%.2f' %venta['total_sin_IVA'] * 1.19)
    print()
    print ('Datos del producto:')
    mostrar_datos_producto(venta['id_producto'])



def mostrar_datos_venta_producto(datos_venta):
    producto = buscar_producto(datos_venta[0])
    mostrar_datos_producto()
    print('Cantidad vendida: %i'% datos_venta[1])


