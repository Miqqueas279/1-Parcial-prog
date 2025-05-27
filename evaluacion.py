pacientes = []

def cargar_pacientes():
    n = int(input("Ingrese cantidad de pacientes a registrar: "))
    for _ in range(n):
        historia = int(input("Número de historia clínica: "))
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad del paciente: "))
        diagnostico = input("Diagnóstico: ")
        dias = int(input("Cantidad de días de internación: "))
        pacientes.append([historia, nombre, edad, diagnostico, dias])
    print("Pacientes cargados exitosamente.")

def mostrar_pacientes():
        """Imprime todos los pacientes registrados."""
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        for paciente in pacientes:
            print(f"Historia: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Días: {paciente[4]}")
    
    input("\nPresiona ENTER para volver al menú...")

def buscar_paciente(num_historia):
    """Busca un paciente por número de historia clínica."""
    encontrado = False
    for paciente in pacientes:
        if paciente[0] == num_historia:
            print(f"Paciente encontrado: {paciente}")
            encontrado = True
            break
    if not encontrado:
        print("Paciente no encontrado.")

def ordenar_pacientes():
     """Ordena los pacientes por número de historia clínica usando el método de burbuja."""
    if not pacientes:
        print(" No hay pacientes registrados.")
        return

    n = len(pacientes)
    i = 0

    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if pacientes[j][0] > pacientes[j + 1][0]:
                pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]
            j += 1
        i += 1

    print("\n Pacientes ordenados por historia clínica:")
    for p in pacientes:
        print(f"Historia Clínica: {p[0]} - Nombre: {p[1]} - Edad: {p[2]} - Diagnóstico: {p[3]} - Días internados: {p[4]}")

def paciente_con_mas_dias():
    """Encuentra el paciente con más días de internación."""
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    paciente_max = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > paciente_max[4]:
            paciente_max = paciente
    print(f"Paciente con más días de internación: {paciente_max}")

def paciente_con_menos_dias():
    """Encuentra el paciente con menos días de internación."""
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    paciente_min = pacientes[0]
    for paciente in pacientes:
        if paciente[4] < paciente_min[4]:
            paciente_min = paciente
    print(f"Paciente con menos días de internación: {paciente_min}")

def cantidad_pacientes_mas_de_5_dias():
        """Cuenta los pacientes con más de 5 días de internación."""
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    cantidad = 0
    for paciente in pacientes:
        if paciente[4] > 5:
            cantidad += 1
    print(f"Cantidad de pacientes con más de 5 días de internación: {cantidad}")

def promedio_dias_internacion():
        """Calcula el promedio de días de internación."""
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    total_dias = 0
    for paciente in pacientes:
        total_dias += paciente[4]
    promedio = total_dias / len(pacientes)
    print(f"Promedio de días de internación: {promedio:.2f}")

def menu():
"""Menú interactivo del sistema de gestión de clínica."""
    while True:
        print("\nSistema de Gestión de Clínica")
        print("1. Cargar pacientes")
        print("2. Mostrar todos los pacientes")
        print("3. Buscar paciente por número de historia clínica")
        print("4. Ordenar pacientes por número de historia clínica")
        print("5. Mostrar paciente con más días de internación")
        print("6. Mostrar paciente con menos días de internación")
        print("7. Cantidad de pacientes con más de 5 días de internación")
        print("8. Promedio de días de internación de todos los pacientes")
        print("9. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_pacientes()
        elif opcion == 2:
            mostrar_pacientes() 
        elif opcion == 3:
            num_historia = int(input("Ingrese número de historia clínica: "))
            buscar_paciente(num_historia)
        elif opcion == 4:
            ordenar_pacientes()
        elif opcion == 5:
            paciente_con_mas_dias()
        elif opcion == 6:
            paciente_con_menos_dias()
        elif opcion == 7:
            cantidad_pacientes_mas_de_5_dias()
        elif opcion == 8:
            promedio_dias_internacion()
        elif opcion == 9:
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")
menu()
