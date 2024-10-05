import tkinter as tk
from tkinter import messagebox, font

class TodoApp:
    def __init__(self, root):
        """Inicializa la ventana principal y los elementos gráficos."""
        self.root = root
        self.configurar_ventana()

        # Crear subtítulo para explicar los atajos de teclado
        self.crear_subtitulo()

        # Crear el área de entrada y la lista de tareas
        self.crear_area_entrada()
        self.crear_lista_tareas()

        # Crear botones y atajos
        self.crear_botones()
        self.crear_atajos_teclado()

    def configurar_ventana(self):
        """Parámetros generales de la ventana."""
        self.root.title("UEA_Registro de tareas")  # Título
        self.root.geometry("500x550")
        self.root.configure(bg="#2E8B57")  # Fondo verde
        self.root.resizable(False, False)  

    def crear_subtitulo(self):
        """Crea un subtítulo que explique los atajos de teclado."""
        texto_subtitulo = (
            "Atajos de teclado:\n"
            "* Enter o I: Añadir tarea\n"
            "* C: Completar tarea\n"
            "* D: Eliminar tarea\n"
            "* Escape: Cerrar aplicación"
        )
        subtitulo_label = tk.Label(
            self.root, text=texto_subtitulo, bg="#2E8B57", fg="white", font=("Arial", 10, "italic")
        )
        subtitulo_label.pack(pady=10)

    def crear_area_entrada(self):
        """Crea el área de entrada para las nuevas tareas."""
        fuente_personalizada = font.Font(family="Helvetica", size=12, weight="bold")
        self.entrada_tarea = tk.Entry(self.root, width=45, font=fuente_personalizada, bg="#F0FFF0", fg="#333333")
        self.entrada_tarea.pack(pady=15)

    def crear_lista_tareas(self):
        """Crea la lista donde se mostrarán las tareas."""
        self.lista_tareas = tk.Listbox(self.root, height=10, width=45, font=("Courier", 12), bg="#D3E4CD", fg="#333333")
        self.lista_tareas.pack(pady=10)

    def crear_botones(self):
        """Crea los botones con funcionalidades avanzadas."""
        marco_botones = tk.Frame(self.root, bg="#2E8B57")
        marco_botones.pack(pady=10)

        self.boton_añadir = self.crear_boton(marco_botones, "Añadir Tarea", self.añadir_tarea, "#66CDAA", "#000000")
        self.boton_completar = self.crear_boton(marco_botones, "Completar Tarea", self.completar_tarea, "#66CDAA", "#000000")
        self.boton_eliminar = self.crear_boton(marco_botones, "Eliminar Tarea", self.eliminar_tarea, "#66CDAA", "#000000")

    def crear_boton(self, parent, text, command, bg, fg):
        """Función para crear botones con un estilo común."""
        boton = tk.Button(parent, text=text, command=command, width=15, bg=bg, fg=fg, font=("Arial", 10, "bold"))
        boton.pack(side=tk.LEFT, padx=5)
        return boton

    def crear_atajos_teclado(self):
        """Asigna atajos de teclado para acciones comunes."""
        self.root.bind("<Return>", lambda event: self.añadir_tarea())  # Añadir tarea con Enter
        self.root.bind("<i>", lambda event: self.añadir_tarea())       # Atajo personalizado "I" para añadir
        self.root.bind("<c>", lambda event: self.completar_tarea())  # Completar tarea con "C"
        self.root.bind("<d>", lambda event: self.eliminar_tarea())    # Eliminar tarea con "D"
        self.root.bind("<Escape>", lambda event: self.cerrar_aplicacion())  # Cerrar con Escape

    def añadir_tarea(self):
        """Añade una tarea a la lista si el campo de entrada no está vacío."""
        tarea = self.entrada_tarea.get().strip()  # Limpia espacios innecesarios
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)  # Borra el campo de entrada después de añadir
        else:
            self.mostrar_mensaje("Campo vacío", "¡Por favor, ingresa una tarea!")

    def completar_tarea(self):
        """Marca la tarea seleccionada como completada."""
        try:
            tarea_seleccionada = self.lista_tareas.curselection()[0]
            tarea = self.lista_tareas.get(tarea_seleccionada)
            self.lista_tareas.delete(tarea_seleccionada)
            self.lista_tareas.insert(tk.END, f"[COMPLETADA] {tarea}")
        except IndexError:
            self.mostrar_mensaje("Sin selección", "¡Por favor, selecciona una tarea para completar!")

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada."""
        try:
            tarea_seleccionada = self.lista_tareas.curselection()[0]
            self.lista_tareas.delete(tarea_seleccionada)
        except IndexError:
            self.mostrar_mensaje("Sin selección", "¡Por favor, selecciona una tarea para eliminar!")

    def cerrar_aplicacion(self):
        """Cierra la aplicación."""
        self.root.quit()

    def mostrar_mensaje(self, titulo, mensaje):
        """Muestra un mensaje de advertencia."""
        messagebox.showwarning(titulo, mensaje)

# Crear la ventana principal y lanzar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
