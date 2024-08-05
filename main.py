import platform
import os
from tareas import Tarea
from tareas_simples import TareaSimple
from tareas_recurrentes import TareaRecurrente
from gestor_tareas import GestorTareas
from datetime import datetime

# def limpiar_pantalla():
#     ''' Limpiar la pantalla según el sistema operativo'''
#     if platform.system() == 'Windows':
#         os.system('cls')
#     else:
#         os.system('clear') # Para Linux/Unix/MacOs

def show_menu():   
    print(f"--------- Sistema de Gestión de Tareas ---------")
    print("1. Agregar Tarea")
    print("2. Mostrar una Tarea")
    print("3. Modificar Tarea")
    print("4. Eliminar Tarea")
    print("5. Mostrar todas las Tareas")
    print("0. Salir")

# agregar tarea
def agregar_tarea(gestor):
    try:
        print("Elige el tipo de tarea a crear:")
        print("1. Tarea Simple")
        print("2. Tarea Recurrente")
        tipo_tarea = int(input("Ingrese tipo de tarea: "))
        if tipo_tarea == 1 or tipo_tarea == 2:
            descripcion = input("Ingrese nomnre de la tarea: ").lower()
            if tipo_tarea == 1:
                tarea = TareaSimple(descripcion)
            elif tipo_tarea == 2:
                fecha_vencimiento = input("Ingrese fecha de vencimiento/tope (DD/MM/YYYY): ")
                fecha_vencimiento = gestor.validar_fecha(fecha_vencimiento)
                frecuencia = input("Ingrese frecuencia (diaria, semanal, mensual): ")
                tarea = TareaRecurrente(descripcion, fecha_vencimiento.strftime("%d/%m/%Y"), frecuencia)
            gestor.crear_tarea(tarea)
        else:
            print("Tipo de tarea no válido.")
            return
        input('Presione enter para continuar...')
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')

# mostrar una tarea
def buscar_tarea(gestor):
    try:
        descripcion = input("Ingrese nombre de la tarea a mostrar: ").lower()
        tareas = gestor.leer_archivo()
        if descripcion in tareas:
            tarea = tareas[descripcion]

            print(f"\nTarea: {descripcion} {tarea}")
        else:
            print(f"Tarea no encontrada.")
        input('Presione enter para continuar...')
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')

# modificar tarea
def modificar_tarea(gestor):
    try:
        descripcion = input("Nombre de la tarea a modificar: ")
        datos = gestor.leer_archivo()

        if descripcion in datos:
            tarea = datos[descripcion]
            nuevos_datos = {}
            print("Ingrese nuevos datos (deje en blanco para no cambiar):")

            nuevo_nombre = input("Nombre: ").lower()
            if nuevo_nombre and nuevo_nombre != descripcion:
                if nuevo_nombre in datos:
                    print(f"Ya existe una tarea con el nombre '{nuevo_nombre}'.")
                else:
                    datos[nuevo_nombre] = datos.pop(descripcion)  # Cambiar clave en el diccionario
                    descripcion = nuevo_nombre  # Actualizar la variable descripcion para referencia futura

            nueva_descripcion = input("Descripción: ")
            if nueva_descripcion:
                nuevos_datos['descripcion'] = nueva_descripcion

            nuevo_estado = input("Estado (pendiente, en progreso, completada): ")
            if nuevo_estado:
                nuevos_datos['estado'] = nuevo_estado

            if isinstance(tarea, TareaRecurrente):
                nueva_fecha_vencimiento = input("Fecha de vencimiento (DD/MM/YYYY): ")
                if nueva_fecha_vencimiento:
                    nuevos_datos['fecha_tope'] = nueva_fecha_vencimiento            
                nueva_frecuencia = input("Nueva frecuencia (diaria, semanal, mensual): ")
                if nueva_frecuencia:
                    nuevos_datos['frecuencia'] = nueva_frecuencia

            tarea_actualizada = datos[descripcion]
            for clave, valor in nuevos_datos.items():
                setattr(tarea_actualizada, clave, valor)

            gestor.guardar_tarea(datos)
            print(f"Tarea '{descripcion}' modificada")
        else:
            print(f"Tarea '{descripcion}' no encontrada")
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')

# eliminar tarea
def eliminar_tarea(gestor):
    try:
        descripcion = input("Nombre de la tarea a eliminar: ")
        gestor.eliminar_tarea(descripcion)
    except Exception as e:
        print(f'Error inesperado: {e}')

# mostrar todas las tareas
def mostrar_todas_las_tareas(gestor):
    tareas = gestor.leer_archivo()
    if tareas:  
        for descripcion, tarea in tareas.items():
            print(f"\nTarea: {descripcion}\n{tarea}")
    else:
        print("No hay tareas disponibles.")
    input('Presione enter para continuar...')

if __name__ == "__main__":
    file_tarea = 'tareas.json'
    gestor = GestorTareas(file_tarea)
    while True:
        # limpiar_pantalla()
        show_menu()
        opcion = input("Elige una opción: ")
        if opcion == '1':
            agregar_tarea(gestor)
        elif opcion == '2':
            buscar_tarea(gestor)
        elif opcion == '3':
            modificar_tarea(gestor)
        elif opcion == '4':
            eliminar_tarea(gestor)
        elif opcion == '5':
            mostrar_todas_las_tareas(gestor)
        elif opcion == '0':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, elige nuevamente.")
