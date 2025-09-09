class Candidata:
    def __init__(self, codigo, nombre, edad, institucion, municipio):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.institucion = institucion
        self.municipio = municipio
        self.calificaciones = []


    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)



    def puntaje_final(self):
        if not self.calificaciones:
            return 0
        return sum(c.promedio() for c in self.calificaciones) / len(self.calificaciones)