class Calificacion:
    def __init__(self, jurado, candidata, cultura, proyeccion, entrevista):
        self.jurado = jurado
        self.candidata = candidata
        self.cultura = cultura
        self.proyeccion = proyeccion
        self.entrevista = entrevista

    def promedio(self):
        return (self.cultura + self.proyeccion + self.entrevista) / 3


