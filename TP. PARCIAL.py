 # Listado de nombres de usuarios
usuarios = [
    "lunatico_pixel", "sombra_cristal", "ecoerrante", "navefantasma", "bytesdelabahia",
    "tintaenelviento", "relojoxidado", "miradacodificada", "circuitoazul", "fuego_niebla",
    "teclaerrante", "nebulosa_urbana", "sueño_binario", "saltofantasma", "claveoculta"
]

# Listado de nombres de empresas disponibles para invertir
acciones = ["APPLE", "TESLA", "NVIDIA"]

# Precio por acción para cada empresa (en dólares)
precios = [10.41, 7.71, 8.50]

# Matriz 15x3 que guarda la cantidad de acciones que cada usuario compró de cada empresa
matriz = []
for i in range(15):
    fila = [0, 0, 0]
    matriz += fila

# Normaliza el nombre de usuario: primera letra en mayúscula, resto en minúsculas
def normalizar_usuario(nombre):
    resultado = ""
    for i in range(len(nombre)):
        letra = nombre[i]
        if i == 0:
            if letra >= "a" and letra <= "z":
                letra = chr(ord(letra) - 32)
        else:
            if letra >= "A" and letra <= "Z":
                letra = chr(ord(letra) + 32)
        resultado += letra
    return resultado

# Convierte todo el nombre de acción a mayúsculas
def normalizar_accion(nombre):
    resultado = ""
    for i in range(len(nombre)):
        letra = nombre[i]
        if letra >= "a" and letra <= "z":
            letra = chr(ord(letra) - 32)
        resultado += letra
    return resultado

# Busca el índice del usuario en la lista
def obtener_indice_usuario(nombre, usuarios):
    i = 0
    indice = -1
    while i < 15:
        if nombre == normalizar_usuario(usuarios[i]):
            indice = i
            i = 15  # cortar el bucle
        else:
            i += 1
    return indice

# Busca el índice de la acción en la lista
def obtener_indice_accion(nombre, acciones):
    i = 0
    indice = -1
    while i < 3:
        if nombre == acciones[i]:
            indice = i
            i = 3
        else:
            i += 1
    return indice

# Intercambia dos elementos en una lista
def swap(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

# Función para registrar la compra de acciones
def registrar_transaccion(usuarios, acciones, precios, matriz):
    nombre_usuario = input("Ingrese el nombre del usuario: ")
    nombre_usuario = normalizar_usuario(nombre_usuario)
    indice_usuario = obtener_indice_usuario(nombre_usuario, usuarios)

    if indice_usuario == -1:
        print("Usuario no válido.")
    else:
        nombre_accion = input("Ingrese el nombre de la acción (Apple, Tesla, Nvidia): ")
        nombre_accion = normalizar_accion(nombre_accion)
        indice_accion = obtener_indice_accion(nombre_accion, acciones)

        if indice_accion == -1:
            print("Acción no válida.")
        else:
            cantidad = int(input("Ingrese la cantidad de acciones (0 a 500): "))
            if cantidad < 0 or cantidad > 500:
                print("Cantidad fuera de rango.")
            else:
                # Actualizamos la matriz cantidades
                actual = matriz[indice_usuario][indice_accion]
                nuevo = actual + cantidad
                matriz[indice_usuario][indice_accion] = nuevo
                total = cantidad * precios[indice_accion]
                print("Transacción registrada. Total invertido: $", total)

# Muestra los datos completos de cada usuario y acción
def visualizar_datos(usuarios, acciones, precios, matriz):
    for i in range(15):
        for j in range(3):
            print("Usuario:", usuarios[i])
            print("Acción:", acciones[j])
            print("Precio por unidad:", precios[j])
            print("Cantidad:", matriz[i][j])
            total = matriz[i][j] * precios[j]
            print("Total invertido: $", total)
            print("--------------------------")

# Módulo de consultas 
def consultas(usuarios, acciones, precios, matriz):
    while True:
        print("Consultas:")
        print("1. Cantidad total de acciones por usuario")
        print("2. Promedio de acciones por empresa")
        print("3. Usuarios de Z-A con total invertido")
        print("4. Inversión total acumulada")
        print("5. Empresa con más acciones por usuario")
        print("6. Acción con mayor inversión total")
        print("7. Porcentaje de inversión por usuario")
        print("8. Usuarios con inversión mayor al promedio")
        print("9. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        # 1. Total de acciones por usuario
        if opcion == "1":
            for i in range(15):
                total = 0
                for j in range(3):
                    total = total + matriz[i][j]
                print(usuarios[i], "adquirió", total, "acciones")

        # 2. Promedio de acciones por empresa
        elif opcion == "2":
            for j in range(3):
                total = 0
                for i in range(15):
                    total = total + matriz[i][j]
                promedio = total / 15
                print("Promedio de", acciones[j], "=", promedio)

        # 3. Ordenar usuarios de Z a A por nombre y mostrar total invertido
        elif opcion == "3":
            i = 0
            while i < 14:
                j = i + 1
                while j < 15:
                    if usuarios[i] < usuarios[j]:
                        swap(usuarios, i, j)
                        swap(matriz, i, j)
                    j += 1
                i += 1
            for i in range(15):
                total = 0
                for j in range(3):
                    total = total + (matriz[i][j] * precios[j])
                print(usuarios[i], "Total invertido: $", total)

        # 4. Inversión total entre todos los usuarios
        elif opcion == "4":
            total = 0
            for i in range(15):
                for j in range(3):
                    total = total + (matriz[i][j] * precios[j])
            print("Inversión total de todos los usuarios: $", total)

        # 5. Empresa con más acciones compradas por cada usuario
        elif opcion == "5":
            for i in range(15):
                mayor = matriz[i][0]
                indice = 0
                for j in range(1, 3):
                    if matriz[i][j] > mayor:
                        mayor = matriz[i][j]
                        indice = j
                print(usuarios[i], "compró más acciones de", acciones[indice])

        # 6. Acción con mayor inversión total entre todos
        elif opcion == "6":
            total_accion = [0, 0, 0]
            for j in range(3):
                for i in range(15):
                    total_accion[j] = total_accion[j] + (matriz[i][j] * precios[j])
            mayor = total_accion[0]
            indice = 0
            for j in range(1, 3):
                if total_accion[j] > mayor:
                    mayor = total_accion[j]
                    indice = j
            print("La acción con mayor inversión total es:", acciones[indice], "con $", mayor)

        # 7. Porcentaje de inversión individual respecto al total
        elif opcion == "7":
            total_general = 0
            totales = []
            for i in range(15):
                total = 0
                for j in range(3):
                    total = total + (matriz[i][j] * precios[j])
                totales += [total]
                total_general = total_general + total
            for i in range(15):
                porcentaje = (totales[i] * 100) / total_general
                print(usuarios[i], "-->", porcentaje, "%")

        # 8. Mostrar usuarios cuya inversión es mayor al promedio
        elif opcion == "8":
            suma = 0
            totales = []
            for i in range(15):
                total = 0
                for j in range(3):
                    total = total + (matriz[i][j] * precios[j])
                totales += [total]
                suma = suma + total
            promedio = suma / 15
            for i in range(15):
                if totales[i] > promedio:
                    print(usuarios[i], "→ $", totales[i])

        # 9. Salir de consultas
        elif opcion == "9":
            break

# MENÚ PRINCIPAL 
while True:
    print("--- MENÚ PRINCIPAL ---")
    print("1. Registrar una transacción")
    print("2. Visualizar todos los datos")
    print("3. Consultas")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_transaccion(usuarios, acciones, precios, matriz)
    elif opcion == "2":
        visualizar_datos(usuarios, acciones, precios, matriz)
    elif opcion == "3":
        consultas(usuarios, acciones, precios, matriz)
    elif opcion == "4":
        break
    else:
        print("Opción incorrecta.")