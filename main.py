import tkinter as tk
from archivoConcurso import Concurso

class ConcursoBandasApp:
    def __init__(self):
        self.concurso = Concurso()
        self.ventana = tk.Tk()
        self.ventana.title("CONCURSO DE BANDAS")
        self.ventana.geometry("500x300")
        self.info = tk.Label(self.ventana, text = "")
        self.info.pack()

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Calificación de candidatas a Reinas\nSeptiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Registrar candidata", command=self.registrar_candidata)
        opciones.add_command(label="Registrar jurado", command=self.registrar_jurado)
        opciones.add_command(label="Registrar calificacion", command=self.registrar_calificacion)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def registrar_candidata(self):
        self.info.config(text="")
        ventana_inscripcion = tk.Toplevel(self.ventana)
        ventana_inscripcion.title("Registrar candidata")

        tk.Label(ventana_inscripcion, text="Codigo").pack()
        entrada_codigo = tk.Entry(ventana_inscripcion)
        entrada_codigo.pack()

        tk.Label(ventana_inscripcion, text="Nombre").pack()
        entrada_nombre = tk.Entry(ventana_inscripcion)
        entrada_nombre.pack()

        tk.Label(ventana_inscripcion, text="Edad").pack()
        entrada_edad = tk.Entry(ventana_inscripcion)
        entrada_edad.pack()

        tk.Label(ventana_inscripcion, text="Institución Educativa").pack()
        entrada_institucion = tk.Entry(ventana_inscripcion)
        entrada_institucion.pack()

        tk.Label(ventana_inscripcion, text="Municipio").pack()
        entrada_municipio = tk.Entry(ventana_inscripcion)
        entrada_municipio.pack()

        def guardar():
            try:
                candidata = Candidata(
                    entrada_codigo.get(),
                    entrada_nombre.get(),
                    int(entrada_edad.get()),
                    entrada_institucion.get(),
                    entrada_municipio.get()
                )
                self.concurso.agregar_candidata(candidata)
                self.info.config(text="Exito, Inscripcion de candidata realizada!")
                ventana_inscripcion.destroy()
            except Exception as e:
                self.info.config(text=f"Error {e}")

        tk.Button(ventana_inscripcion, text="Guardar", command=guardar).pack(pady=10)

    def registrar_jurado(self):
        self.info.config(text="")
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title("Registrar Jurado")

        tk.Label(ventana_registro, text="Nombre").pack()
        entrada_nombre = tk.Entry(ventana_registro)
        entrada_nombre.pack()

        tk.Label(ventana_registro, text="Especialidad").pack()
        entrada_especialidad = tk.Entry(ventana_registro)
        entrada_especialidad.pack()

        tk.Label(ventana_registro, text="Método para evaluar").pack()
        entrada_metodo = tk.Entry(ventana_registro)
        entrada_metodo.pack()

        def guardar():
            try:
                jurado = Jurado(
                    entrada_nombre.get(),
                    entrada_especialidad.get(),
                    entrada_metodo.get()
                )
                self.concurso.agregar_jurado(jurado)
                self.info.config(text="Exito, Registro de jurado realizada!")
                ventana_registro.destroy()
            except Exception as e:
                self.info.config(text=f"Error {e}")

        tk.Button(ventana_registro, text="Guardar", command=guardar).pack(pady=10)

    def registrar_calificacion(self):
        self.info.config(text="")
        ventana_cal = tk.Toplevel(self.ventana)
        ventana_cal.title("Registrar Calificacion")

        tk.Label(ventana_cal, text="Nombre").pack()
        entrada_jurado = tk.Entry(ventana_cal)
        entrada_jurado.pack()

        tk.Label(ventana_cal, text="Codigo Candidata").pack()
        entrada_cod = tk.Entry(ventana_cal)
        entrada_cod.pack()

        tk.Label(ventana_cal, text="Cultura (0-10").pack()
        entrada_cultura = tk.Entry(ventana_cal)
        entrada_cultura.pack()

        tk.Label(ventana_cal, text="Proyeccion (1-10").pack()
        entrada_proy = tk.Entry(ventana_cal)
        entrada_proy.pack()

        tk.Label(ventana_cal, text="Entrevista (1-10)").pack()
        entrada_ent = tk.Entry(ventana_cal)
        entrada_ent.pack()

        def guardar():
            try:
                calif = Calificacion(
                    entrada_jurado.get(),
                    entrada_cod.get(),
                    entrada_cultura.get(),
                    entrada_proy.get(),
                    entrada_ent.get()
                )
                self.concurso.registrar_calificacion(calif)
                self.info.config(text="Exito, Calificacion realizada!")
                ventana_cal.destroy()
            except Exception as e:
                self.info.config(text=f"Error {e}")

        tk.Button(ventana_cal, text="Guardar", command=guardar).pack(pady=10)

    def ver_ranking(self):
        self.info.config(text="")
        ventana_ranking = tk.Toplevel(self.ventana)
        ventana_ranking.title("Ranking final")

        texto = tk.Text(ventana_ranking, width=80, height=20)
        texto.pack()

        ranking = self.concurso.mostrar_ranking()
        if not ranking:
            texto.insert(tk.END, "No hay candidatas calificadas aún.\n")
        else:
            texto.insert(tk.END, "RANKING DE CANDIDATAS:\n\n")
            for candidata in enumerate(ranking, start=1):
                texto.insert(tk.END, f"{candidata}\n")

if __name__ == "__main__":
    ConcursoBandasApp()
