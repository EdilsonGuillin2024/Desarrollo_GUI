import tkinter as tk
from tkinter import messagebox

# Funciones para manejar las tareas
def add_task(event=None):
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")

def complete_task(event=None):
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"[COMPLETADA] {task}")
    except IndexError:
        messagebox.showwarning("Ninguna tarea seleccionada", "Por favor, selecciona una tarea para completar.")

def delete_task(event=None):
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Ninguna tarea seleccionada", "Por favor, selecciona una tarea para eliminar.")

# Función para cerrar la aplicación
def close_app(event=None):
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas Pendientes")
root.geometry("400x300")
root.configure(bg="#008000")  # Fondo de la ventana en verde

# Campo de entrada para nuevas tareas
task_entry = tk.Entry(root, width=35, bg="#d0f0c0", fg="black")
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)  # Atajo para añadir tarea con Enter

# Lista de tareas
tasks_listbox = tk.Listbox(root, width=50, height=10, bg="#d0f0c0", fg="black")
tasks_listbox.pack(pady=10)

# Botones para añadir, completar y eliminar tareas
buttons_frame = tk.Frame(root, bg="#008000")  # Fondo del frame en verde
buttons_frame.pack(pady=10)

add_button = tk.Button(buttons_frame, text="Añadir tarea", command=add_task, bg="#32CD32", fg="white")
add_button.pack(side=tk.LEFT, padx=10)

complete_button = tk.Button(buttons_frame, text="Marcar como completada", command=complete_task, bg="#32CD32", fg="white")
complete_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(buttons_frame, text="Eliminar tarea", command=delete_task, bg="#32CD32", fg="white")
delete_button.pack(side=tk.LEFT, padx=10)

# Atajos de teclado
root.bind("<Escape>", close_app)          # Atajo para cerrar la aplicación con Escape
root.bind("<c>", complete_task)           # Atajo para marcar como completada con "C"
root.bind("<d>", delete_task)             # Atajo para eliminar con "D"
root.bind("<Control-n>", add_task)        # Atajo para añadir una tarea con Ctrl + N

# Ejecutar la aplicación
root.mainloop()
