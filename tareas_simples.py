from tareas import Tarea
from datetime import date

class TareaSimple(Tarea):
    def __init__(self, descripcion, fecha_creacion=date.today().strftime("%d/%m/%Y"), estado="pendiente"):
        super().__init__(descripcion, estado)
        self.fecha_creacion = fecha_creacion

    def __str__(self):
        return f"Descripción: {self.descripcion}\nFecha de creación: {self.fecha_creacion}\nEstado: {self.estado}\n"

    def to_dict(self):
        super_dict = super().to_dict()
        super_dict['fecha_creacion'] = self.fecha_creacion
        return super_dict

