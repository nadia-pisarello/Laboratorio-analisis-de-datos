import json
from datetime import datetime
from tareas_simples import TareaSimple
from tareas_recurrentes import TareaRecurrente

class GestorTareas:
    def __init__(self, archivo):
        self.archivo = archivo
        self.tareas = self.leer_archivo()

    def leer_archivo(self):
        try:
            with open(self.archivo, 'r') as file:
                contenido = file.read()
                datos = json.loads(contenido)
                return {key: self.dict_to_tarea(value) for key, value in datos.items()}
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará un nuevo archivo.")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")
            return {}
        except Exception as error:
            print(f"Error al leer el archivo: {error}")
            return {}

    def guardar_tarea(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump({key: value.to_dict() for key, value in datos.items()}, file, indent=4)
                print(f"Tareas guardadas en {self.archivo}")
        except IOError as error:
            print(f"Error al intentar guardar el archivo {self.archivo}: {error}")
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")

    def crear_tarea(self, tarea):
        try:
            datos = self.leer_archivo()
            descripcion = tarea.descripcion
            if descripcion not in datos.keys():
                datos[descripcion] = tarea
                self.guardar_tarea(datos)
                print("Se creó una nueva tarea")
            else:
                print("Ya existe esa tarea")
        except Exception as error:
            print(f"No se pudo crear una nueva tarea: {error}")

    def editar_tarea(self, id, nuevos_datos):
        try:
            datos = self.leer_archivo()
            if id in datos:
                if 'descripcion' in nuevos_datos:
                    datos[id].descripcion = nuevos_datos['descripcion']
                if 'fecha_tope' in nuevos_datos:
                    datos[id].fecha_tope = nuevos_datos['fecha_tope']
                if 'estado' in nuevos_datos:
                    datos[id].estado = nuevos_datos['estado']
                if 'frecuencia' in nuevos_datos:
                    datos[id].frecuencia = nuevos_datos['frecuencia']
                self.guardar_tarea(datos)
                print(f"Tarea '{id}' modificada")
            else:
                print("Tarea no encontrada")
        except Exception as error:
            print(f"Error al editar la tarea: {error}")

    def eliminar_tarea(self, descripcion):
        try:
            datos = self.leer_archivo()
            if descripcion in datos:
                del datos[descripcion]
                self.guardar_tarea(datos)
                print(f"Tarea '{descripcion}' eliminada")
            else:
                print("Tarea no encontrada")
        except Exception as error:
            print(f"Error al eliminar la tarea: {error}")

    def dict_to_tarea(self, datos):
        if 'frecuencia' in datos:
            fecha_tope = datetime.strptime(datos['fecha_tope'], '%d/%m/%Y').strftime('%d/%m/%Y')
            return TareaRecurrente(datos['descripcion'], fecha_tope, datos['frecuencia'], datos['estado'])
        else:
            fecha_creacion = datetime.strptime(datos['fecha_creacion'], '%d/%m/%Y').strftime('%d/%m/%Y')
            return TareaSimple(datos['descripcion'], fecha_creacion, datos['estado'])

    def validar_fecha(self, fecha):
        if not fecha:
            return datetime.today()
        try:
             return datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError as e:
             print(f"Error: - Formato de fecha no válido: dd/mm/aaaa {e}")
        return datetime.today()
