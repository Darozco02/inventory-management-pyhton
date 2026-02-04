# Mensaje de Bienvenida
# Implementar una manera para solicitar usuario y contraseña
nombre_usuario = input("Por Favor ingrese su nombre: ").title().strip()
print(f"{nombre_usuario}, Bienvenido al sistema de control de inventario!📦 \n")

lista_productos = []

# Creacion de funciones para cada opcion del menu
# Agregar Productos
def agregar_Productos():
    print("-" * 30 + "\n")
    while True:
        nombre_producto = input("Ingrese el nombre del producto a agregar: ").title().strip()
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))
        precio_unitario = int(input("Ingrese el precio unitario del producto: "))
        lista_productos.append({
            "nombre": nombre_producto,
            "cantidad": cantidad_producto,
            "precio_unitario": precio_unitario
        })
        print(f"Producto {nombre_producto} agregado exitosamente!✅ \n")
        print("-" * 30)
        continuar = input(f"{nombre_usuario} ¿Desea agregar otro producto? (s/n): ").title()
        if continuar == 'S':
            continue
        else:
            break

# Eliminar productos
def eliminar_Productos():
    producto_eliminar = input("Por favor ingrese el nombre del producto a eliminar: ").title().strip()
    encontrado = False
    for producto in lista_productos:
        if producto["nombre"] == producto_eliminar:
            lista_productos.remove(producto)
            encontrado = True
            print("✅ El producto fue eliminado correctamente!")
            break
    if not encontrado:
        print("⚠️ El producto no se encuentra en el inventario!")

# Consultar Inventario
def consulta_Inventario():
    print(f"{nombre_usuario} El inventario actual es el siguiente: \n")
    for i in lista_productos:
        print(f"\n Nombre: {i['nombre']} \n Cantidad: {i['cantidad']} \n Precio Unitario: ${i['precio_unitario']} \n Precio Total: ${i['cantidad'] * i['precio_unitario']} \n ")
        print("-" * 30 + "-")

# Calcular el total del inventario
def calculo_Total_Inventario():
    total_inventario = 0
    for i in lista_productos:
        total_inventario += i['cantidad'] * i['precio_unitario']
    print(f"💵 El precio total del inventario es: ${total_inventario} \n")

# Menu principal
while True:
    print("1-Agregar Productos")
    print("2-Eliminar Productos")
    print("3-Consultar Inventario")
    print("4-Ver el precio total del inventario")
    print("5-Generar Reporte")
    print("6-Salir Del Sistema \n")
    opc = int(input("Por favor ingrese una opcion del menu: "))
    print("-" * 30 + "\n")

    # Opciones del menu
    if opc == 1:
        agregar_Productos()
    elif opc == 2:
        eliminar_Productos()
    elif opc == 3:
        consulta_Inventario()
    elif opc == 4:
        calculo_Total_Inventario()
    elif opc == 5:
        print("Este modulo todavia no esta disponible.")
    elif opc == 6:
        print(f"{nombre_usuario}, Gracias por usar el sistema de control de inventario hasta luego!👋")
        break
    else:
        print("⚠️ Opcion no valida, por favor intente de nuevo.")