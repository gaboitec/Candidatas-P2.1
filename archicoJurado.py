from archivoCalificacion import Calificacion

class Jurado:
    def __init__(self, nombre, especialidad,metodo):
        self.nombre = nombre
        self.especialidad = especialidad
        self.metodo = metodo


    def calificar(self, candidata, cultura, proyeccion, entrevista):
        return Calificacion(self, candidata, cultura, proyeccion, entrevista)
