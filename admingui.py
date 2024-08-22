import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

# Database connection
conexion = pymysql.connect(
    host="localhost",
    user="root",
    password="contra2023",
    database="Base_Datos"
)

class VentanaPrincipalAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Gestión de Empleados")

        # Cargar imagen de fondo
        self.bg_image = ImageTk.PhotoImage(Image.open("fondo.png"))

        # Canvas para la imagen de fondo
        self.canvas = tk.Canvas(self.root, width=self.bg_image.width(), height=self.bg_image.height())
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        # Frame principal en el Canvas
        self.main_frame = tk.Frame(self.canvas, bg="gray", highlightthickness=0, bd=0)
        self.main_frame.place(relwidth=1, relheight=1)

        # Botones principales
        button_frame = tk.Frame(self.main_frame, bg="blue", highlightthickness=0, bd=0)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Button(button_frame, text="Nuevo Cocinero", bg="gray", fg="white", command=lambda: self.add_employee("Cocinero")).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Nuevo Mesero", bg="gray", fg="white", command=lambda: self.add_employee("Mesero")).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Modificar Cocinero", bg="gray", fg="white", command=lambda: self.modify_employee("Cocinero")).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Modificar Mesero", bg="gray", fg="white", command=lambda: self.modify_employee("Mesero")).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Eliminar Cocinero", bg="gray", fg="white", command=lambda: self.delete_employee("Cocinero")).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Eliminar Mesero", bg="gray", fg="white", command=lambda: self.delete_employee("Mesero")).pack(side=tk.LEFT, padx=5, pady=5)

        # Tabla de empleados
        right_frame = tk.Frame(self.main_frame, bg="#42b337", highlightthickness=0, bd=0)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(right_frame, columns=("ID", "Nombre", "Papellido", "Sapellido", "Usuario", "Contraseña", "Rol"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Papellido", text="P. Apellido")
        self.tree.heading("Sapellido", text="S. Apellido")
        self.tree.heading("Usuario", text="Usuario")
        self.tree.heading("Contraseña", text="Contraseña")
        self.tree.heading("Rol", text="Rol")

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.setup_styles()

        # Botón de cerrar sesión
        logout_button_frame = tk.Frame(self.main_frame, bg="gray", highlightthickness=0, bd=0)
        logout_button_frame.pack(side=tk.BOTTOM, fill=tk.X)
        tk.Button(logout_button_frame, text="Cerrar Sesión", command=self.confirm_logout).pack(side=tk.RIGHT, padx=10, pady=10)

        # Iniciar la actualización automática
        self.update_treeview()

    def setup_styles(self):
        # Configurar estilos para Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="#32786e", foreground="white", font=("Arial", 10, "bold"))
        style.configure("Treeview", background="#d3ffd3", foreground="black", font=("Arial", 10))

    def add_employee(self, role):
        self.open_employee_window(f"Agregar {role}", role)

    def modify_employee(self, role):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item, "values")
            self.open_employee_window(f"Modificar {role}", role, item_values)
        else:
            messagebox.showwarning("Advertencia", f"Por favor, seleccione un {role.lower()} para modificar.")

    def delete_employee(self, role):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item, "values")
            employee_id = item_values[0]
            if messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de eliminar el {role.lower()} con ID {employee_id}?"):
                cursor = conexion.cursor()
                if role == "Cocinero":
                    delete_query = "DELETE FROM cocinero WHERE Id_cocinero = %s"
                else:
                    delete_query = "DELETE FROM mesero WHERE Id_mesero = %s"
                cursor.execute(delete_query, (employee_id,))
                conexion.commit()
                cursor.close()
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", f"Por favor, seleccione un {role.lower()} para eliminar.")

    def open_employee_window(self, title, role, values=None):
        window = tk.Toplevel(self.root)
        window.title(title)

        tk.Label(window, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
        nombre_entry = tk.Entry(window)
        nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(window, text="P. Apellido").grid(row=1, column=0, padx=5, pady=5)
        papellido_entry = tk.Entry(window)
        papellido_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(window, text="M. Apellido").grid(row=2, column=0, padx=5, pady=5)
        sapellido_entry = tk.Entry(window)
        sapellido_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(window, text="Usuario").grid(row=3, column=0, padx=5, pady=5)
        usuario_entry = tk.Entry(window)
        usuario_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(window, text="Contraseña").grid(row=4, column=0, padx=5, pady=5)
        contraseña_entry = tk.Entry(window, show="*")
        contraseña_entry.grid(row=4, column=1, padx=5, pady=5)

        if values:
            nombre_entry.insert(0, values[1])
            papellido_entry.insert(0, values[2])
            sapellido_entry.insert(0, values[3])
            usuario_entry.insert(0, values[4])
            contraseña_entry.insert(0, values[5])

        def save_changes():
            nombre = nombre_entry.get()
            papellido = papellido_entry.get()
            sapellido = sapellido_entry.get()
            usuario = usuario_entry.get()
            contraseña = contraseña_entry.get()

            if not nombre or not papellido or not sapellido or not usuario or not contraseña:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                return

            cursor = conexion.cursor()
            if values:
                if role == "Cocinero":
                    update_query = "UPDATE cocinero SET Nombre=%s, Papellido=%s, Sapellido=%s, Usuario=%s, Contraseña=%s WHERE Id_cocinero=%s"
                else:
                    update_query = "UPDATE mesero SET Nombre=%s, Papellido=%s, Sapellido=%s, Usuario=%s, Contraseña=%s WHERE Id_mesero=%s"
                cursor.execute(update_query, (nombre, papellido, sapellido, usuario, contraseña, values[0]))
            else:
                if role == "Cocinero":
                    insert_query = "INSERT INTO cocinero (Nombre, Papellido, Sapellido, Usuario, Contraseña, Id_administrador) VALUES (%s, %s, %s, %s, %s, 2)"  # the actual Id_administrador
                else:
                    insert_query = "INSERT INTO mesero (Nombre, Papellido, Sapellido, Usuario, Contraseña, Id_administrador) VALUES (%s, %s, %s, %s, %s, 2)"  # the actual Id_administrador
                cursor.execute(insert_query, (nombre, papellido, sapellido, usuario, contraseña))

            conexion.commit()
            cursor.close()

            window.destroy()
            self.refresh_treeview()

        tk.Button(window, text="Guardar", command=save_changes).grid(row=5, column=0, columnspan=2, pady=10)

    def refresh_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cocinero")
        cocineros = cursor.fetchall()
        cursor.execute("SELECT * FROM mesero")
        meseros = cursor.fetchall()
        cursor.close()

        for row in cocineros:
            self.tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], "Cocinero"))

        for row in meseros:
            self.tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], "Mesero"))

    def update_treeview(self):
        self.refresh_treeview()
        self.root.after(500000, self.update_treeview)  # Repetir cada 500ms

    def confirm_logout(self):
        if messagebox.askyesno("Cerrar Sesión", "¿Está seguro de que desea cerrar sesión?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipalAdmin(root)
    root.state("zoomed")  # Maximizar ventana automáticamente
    root.mainloop()
