from tareas import Tarea
from datetime import datetime

class TareaRecurrente(Tarea):
    def __init__(self, descripcion, fecha_tope, frecuencia, estado="pendiente"):
        super().__init__(descripcion, estado)
        self.__fecha_tope = fecha_tope
        self.__frecuencia = frecuencia

    @property
    def frecuencia(self):
        return self.__frecuencia
    
    @frecuencia.setter
    def frecuencia(self, nueva_frecuencia):
        self.__frecuencia = nueva_frecuencia

    @property
    def fecha_tope(self):
        return self.__fecha_tope
    
    @fecha_tope.setter
    def fecha_tope(self, nueva_fecha_tope):
        self.__fecha_tope = nueva_fecha_tope

    def __str__(self):
        return f"Descripción: {self.descripcion}\nFecha Tope: {self.fecha_tope}\nFrecuencia: {self.frecuencia}\nEstado: {self.estado}\n"

    def to_dict(self):
        super_dict = super().to_dict()
        super_dict['fecha_tope'] = self.fecha_tope
        super_dict['frecuencia'] = self.frecuencia
        return super_dict
