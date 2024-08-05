class Tarea:
    def __init__(self, descripcion, estado="pendiente"):        
        self.descripcion = descripcion
        self.estado = estado

    def to_dict(self):
        return {
            "descripcion": self.descripcion,
            "estado": self.estado
        }

    def __str__(self):
        return f"\nDescripción: {self.descripcion}\nEstado: {self.estado}"

