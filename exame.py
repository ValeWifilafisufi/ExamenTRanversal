
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'] 
    }
stock = {'8475HD': [387990,10], 
    '2175HD': [327990,4],
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21],
    '123FHD': [290890,32],
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1],
    'FS1230HD': [249990,0], 
    }

marcas = ["HP", "LENOVO", "ASUS", "DELL"]

def stock_marca(productos, stock):
    marca = input("Ingrese la marca que desea buscar: ").upper().strip() #pedimos la marca
    if marca in marcas: #validamos que la carca exista 
        stockxmarca = 0
        codigosparabuscar = []
        codigosxmarca = []

        for codigo, datos in productos.items():
            if datos[0].upper() == marca: #valido que la marca que quiero buscar si este en la lista
                codigosxmarca.append(codigo)
        for i in codigosxmarca:
            codigosparabuscar.append(i) #lo agrego a la lista
        for codigos, datos in stock.items(): #verifico si el codigo esta en el stock
            if codigos in codigosparabuscar:  
                if codigos in codigosxmarca:
                    stockxmarca += datos[1] #supuestamente lo sumo
                    
        print(f"El stock para {marca} es {stockxmarca}")
    else:
        print("la marca no esta registrada")

def busquedaxprecio(productos,stock):
    try:
        #pedimos rngo de precios
        preciominimo = int(input("Ingrese el precio minimo a buscar: "))
        preciomaximo = int(input("Ingrese el precio maximo a buscar: "))
        codigos = {}
        marca_modelo = []
    except ValueError:
        print("solo se pueden ingresar numeros enteros.")
    else:
        for codigo, datos in stock.items(): #verificamos que este
            codigos[codigo]
            precioproducto = datos[0] #pasamos el precio a una variable para poder validarla
            if precioproducto >= preciominimo: #validamos que sea mayor que el minimo
                    if precioproducto <= preciomaximo: #validamos que sea menor que el maximo
                        codigos[codigo] #lo agregamos a la lista para verificar
                        codigos[codigo] = [precioproducto]
                        for clave, valor in productos.items(): 
                            if codigos in productos:
                                codigos.sort()
                                print(f"{codigos}")
                            else:
                                print("idk que poner aca ")
                    else:
                        print("No hay productos que cumplan con el rango")

def actualizar(productos,stock):
    for clave, datos in productos.items():
        print(f"codigo: {clave} - Modelo: {datos[0]}")
    modelo = input("ingrese el modelo que desea actualizar el precio: ").upper()
    for clave, valor in stock.items():
        if modelo in stock:
            precio_nuevo = float(input(f"Ingrese el nuevo precio de {modelo}"))
            stock[valor[0]] = precio_nuevo
            print("Precio actualizado con exito.")
            break
        else:
            print("el modelo que buscas no esta disponible")

def main():
    while True:
        try:
            print("1. Stock marca.")
            print("2. Búsqueda por precio.")
            print("3. Actualizar precio.")
            print("4. Salir.")

            opc = int(input("Igrese una opcion: "))
        except ValueError:
            print("Error: Solo se pueden ingresar números. Vuelva a intentarlo.")
        else:
            if opc == 1:
                stock_marca(productos,stock)
            elif opc == 2:
                busquedaxprecio(productos,stock)
            elif opc == 3:
                actualizar(productos,stock)
            elif opc == 4:
                print("Saliendo del programa.")
                break
            else:
                print("Debe seleccionar una opción válida!!")


if __name__ == "__main__":
    main()
        


