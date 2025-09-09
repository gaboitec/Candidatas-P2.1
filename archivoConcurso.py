from archivoCandidatas import Candidata
from tkinter import messagebox


class Concurso:
    def __init__(self):
        self.candidatas = {}
        self.jurados = {}
        self.calificaciones = []
        self.cargar_datos()

    def agregar_candidata(self, candidata):
        self.candidatas[candidata.codigo] = candidata
        self.guardar_datos()

    def agregar_jurado(self, jurado):
        self.jurados[jurado.nombre] = jurado




    def registrar_calificacion(self, nombre_jurado, codigo_candidata, cultura, proyeccion, entrevista):
        if nombre_jurado not in self.jurados or codigo_candidata not in self.candidatas:
            return False

        jurado = self.jurados[nombre_jurado]
        candidata = self.candidatas[codigo_candidata]
        calificacion = jurado.calificar(candidata, cultura, proyeccion, entrevista)
        candidata.agregar_calificacion(calificacion)
        self.calificaciones.append(calificacion)
        return True



    def ranking(self):
        lista_candidatas = list(self.candidatas.values())

        n = len(lista_candidatas)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista_candidatas[j].puntaje_final() < lista_candidatas[j + 1].puntaje_final():
                    lista_candidatas[j], lista_candidatas[j + 1] = lista_candidatas[j + 1], lista_candidatas[j]

        return lista_candidatas


    def mostrar_ranking(self):
        ranking = self.ranking()
        resultado = "RANKING FINAL DE CANDIDATAS:\n\n"
        for i, candidata in enumerate(ranking, start=1):
            resultado += f"{i}. {candidata.nombre} - {candidata.puntaje_final():.2f}\n"
        if ranking:
            resultado += f"\nGanadora: {ranking[0].nombre}"
        return resultado

    def guardar_datos(self, archivo="concurso.txt"):
        with open(archivo, "w", encoding="utf-8") as f:
            for candidata in self.candidatas.values():
                f.write(f"{candidata.codigo}:{candidata.nombre}:{candidata.edad}:"
                        f"{candidata.institucion}:{candidata.municipio}:{candidata.puntaje_final():.2f}\n")




    def cargar_datos(self, archivo="concurso.txt"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    codigo, nombre, edad, institucion, municipio, puntaje = linea.strip().split(":")
                    candidata = Candidata(codigo, nombre, int(edad), institucion, municipio)
                    self.candidatas[codigo] = candidata
        except FileNotFoundError:
            messagebox.showwarning("NO se enctro el archivo")