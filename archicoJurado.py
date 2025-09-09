from archivoCalificacion import Calificacion

class Jurado:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def calificar(self, candidata, cultura, proyeccion, entrevista):
        return Calificacion(self, candidata, cultura, proyeccion, entrevista)
