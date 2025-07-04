productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0],
}

def obtener_stock_marca(marca):
    marca = marca.lower()
    for modelo, info in productos.items():
        if info[0].lower() == marca:
            print(f'Modelo: {modelo} | Stock: {stock[modelo][1]}')

def busqueda_precio(p_min, p_max):
    modelos_en_rango = []
    for modelo, info in productos.items():
        precio = stock[modelo][0]
        if p_min <= precio <= p_max and stock[modelo][1] > 0:
            modelos_en_rango.append(f'{info[0]}--{modelo}')
    
    if modelos_en_rango:
        modelos_en_rango.sort()  # Ordenamos alfabéticamente
        for modelo in modelos_en_rango:
            print(modelo)
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    return False

def obtener_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Debe ingresar un valor entero!!")

def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            marca = input("Ingrese la marca: ")
            obtener_stock_marca(marca)
        
        elif opcion == '2':
            p_min = obtener_int("Ingrese el precio mínimo: ")
            p_max = obtener_int("Ingrese el precio máximo: ")
            busqueda_precio(p_min, p_max)
        
        elif opcion == '3':
            modelo = input("Ingrese el modelo a actualizar: ")
            precio_nuevo = obtener_int("Ingrese el nuevo precio: ")
            if actualizar_precio(modelo, precio_nuevo):
                print("Precio actualizado!!")
            else:
                print("El modelo no existe!!")
            
            actualizar_otro = input("¿Desea actualizar otro precio? (si/no): ").lower()
            if actualizar_otro != 'si':
                continue
        
        elif opcion == '4':
            print("Programa finalizado.")
            break
        
        else:
            print("Debe seleccionar una opción válida!!")

menu()
