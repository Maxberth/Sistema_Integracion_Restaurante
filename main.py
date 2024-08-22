import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import pymysql
import subprocess
import os

conexion = pymysql.connect(
    host="localhost",
    user="root",
    password="contra2023",
    database="MIMANUELA"
)

class VentanaInicioSesion:
    def __init__(self, rol):
        self.rol = rol
        self.ventana = tk.Toplevel()
        self.ventana.title(f"Inicio de Sesión - {rol.capitalize()}")
        self.ventana.geometry("400x200")

        etiqueta_usuario = tk.Label(self.ventana, text="Usuario:", font=("Arial", 12))
        etiqueta_usuario.pack(pady=10)
        self.entrada_usuario = tk.Entry(self.ventana, font=("Arial", 12))
        self.entrada_usuario.pack(pady=5)

        etiqueta_contrasena = tk.Label(self.ventana, text="Contraseña:", font=("Arial", 12))
        etiqueta_contrasena.pack(pady=10)
        self.entrada_contrasena = tk.Entry(self.ventana, show="*", font=("Arial", 12))
        self.entrada_contrasena.pack(pady=5)

        boton_iniciar_sesion = tk.Button(self.ventana, text="Iniciar Sesión", font=("Arial", 12), command=self.iniciar_sesion)
        boton_iniciar_sesion.pack(pady=10)

    def iniciar_sesion(self):
        usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()
        cursor = conexion.cursor()
        consulta = f"SELECT * FROM {self.rol} WHERE Usuario = %s AND Contraseña = %s"
        cursor.execute(consulta, (usuario, contrasena))
        resultado = cursor.fetchone()
        if resultado:
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
            self.ventana.withdraw()
            if self.rol == 'cocinero':
                root.deiconify()  # Mostrar la ventana principal
                script_dir = os.path.dirname(os.path.abspath(__file__))
                script_path = os.path.join(script_dir, "cocinerogui.py")
                subprocess.Popen(["python", script_path], shell=True)

            if self.rol == 'administrador':
                root.deiconify()  # Mostrar la ventana principal
                script_dir = os.path.dirname(os.path.abspath(__file__))
                script_path = os.path.join(script_dir, "admingui.py")
                subprocess.Popen(["python", script_path], shell=True)

            if self.rol == 'mesero':
                root.deiconify()  # Mostrar la ventana principal
                script_dir = os.path.dirname(os.path.abspath(__file__))
                script_path = os.path.join(script_dir, "meserogui.py")
                subprocess.Popen(["python", script_path], shell=True)
            return True
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            return False

# Crear la ventana principal
root = tk.Tk()
root.title("Iniciar Sesión")
root.geometry("810x500")
root.configure(bg="white")

# Cargar imagen de fondo usando ruta relativa
script_dir = os.path.dirname(os.path.abspath(__file__))
restaurante_path = os.path.join(script_dir, "fondo.png")
restaurante_image = Image.open(restaurante_path)
restaurante_photo = ImageTk.PhotoImage(restaurante_image)

# Panel de contenido
content_frame = tk.Frame(root, bg="white")
content_frame.pack(expand=True, fill=tk.BOTH)

# Etiqueta de fondo
restaurante_label = tk.Label(content_frame, image=restaurante_photo, bg="white")
restaurante_label.place(x=450, y=0)

# Etiqueta del título
inicio_sesion_label = tk.Label(content_frame, text="Iniciar Sesión", font=("Roboto Black", 24), bg="white", fg="black")
inicio_sesion_label.place(x=135, y=80)

# Botones de roles
def mostrar_ventana_inicio_sesion(rol):
    VentanaInicioSesion(rol)

boton_admin = tk.Button(content_frame, text="Administrador", font=("Roboto Medium", 14), bg="#333333", fg="white", cursor="hand2", command=lambda: mostrar_ventana_inicio_sesion('administrador'))
boton_admin.place(x=170, y=140, width=150, height=40)

boton_cocinero = tk.Button(content_frame, text="Cocinero", font=("Roboto Medium", 14), bg="#333333", fg="white", cursor="hand2", command=lambda: mostrar_ventana_inicio_sesion('cocinero'))
boton_cocinero.place(x=170, y=190, width=150, height=40)

boton_mesero = tk.Button(content_frame, text="Mesero", font=("Roboto Medium", 14), bg="#333333", fg="white", cursor="hand2", command=lambda: mostrar_ventana_inicio_sesion('mesero'))
boton_mesero.place(x=170, y=240, width=150, height=40)

# Mantener la ventana abierta
root.mainloop()
