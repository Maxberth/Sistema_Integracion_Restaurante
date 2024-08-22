import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

conexion = pymysql.connect(
    host="localhost",
    user="root",
    password="contra2023",
    database="MIMANUELA"
)

class VentanaPrincipalCocinero:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema gestión de menús")

        # Cargar imagen de fondo
        self.bg_image = ImageTk.PhotoImage(Image.open("fondo.png"))

        # Canvas para la imagen de fondo
        self.canvas = tk.Canvas(self.root, width=self.bg_image.width(), height=self.bg_image.height())
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        # Frame principal en el Canvas con transparencia
        self.main_frame = tk.Frame(self.canvas, bg="gray", highlightthickness=0, bd=0)
        self.main_frame.place(relwidth=1, relheight=1)

        # Botones principales
        button_frame = tk.Frame(self.main_frame, bg="blue", highlightthickness=0, bd=0)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Button(button_frame, text="Nuevo", bg="gray", fg="white", command=self.add_dish).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Modificar", bg="gray", fg="white", command=self.modify_dish).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Eliminar", bg="gray", fg="white", command=self.delete_dish).pack(side=tk.LEFT, padx=5, pady=5)

        # Botón VER PEDIDO
        tk.Button(button_frame, text="VER PEDIDO", bg="red", fg="white", command=self.open_order_window).pack(side=tk.RIGHT, padx=5, pady=5)

        # Tabla de platos
        right_frame = tk.Frame(self.main_frame, bg="#42b337", highlightthickness=0, bd=0)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(right_frame, columns=("Codigo", "Platillo", "Precio"), show="headings")
        self.tree.heading("Codigo", text="Codigo")
        self.tree.heading("Platillo", text="Platillo")
        self.tree.heading("Precio", text="Precio")

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.setup_styles()

        # Botón de cerrar sesión en la parte inferior derecha
        logout_button_frame = tk.Frame(self.main_frame, bg="gray", highlightthickness=0, bd=0)
        logout_button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        tk.Button(logout_button_frame, text="Cerrar Sesión", command=self.confirm_logout).pack(side=tk.RIGHT, padx=10, pady=10)

    def setup_styles(self):
        # Configurar estilos para Treeview
        style = ttk.Style()
        style.theme_use("clam")

        # Configurar el estilo de los encabezados
        style.configure("Treeview.Heading", background="#32786e", foreground="white", font=("Arial", 10, "bold"))

        # Configurar el estilo de las filas
        style.configure("Treeview", background="#d3ffd3", foreground="black", font=("Arial", 10))

    def add_dish(self):
        self.open_dish_window("Agregar Plato")

    def modify_dish(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item, "values")
            self.open_dish_window("Modificar Plato", item_values)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un plato para modificar.")

    def delete_dish(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item, "values")
            codigo_platillo = item_values[0]  # Obtener el código del platillo seleccionado
            if messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de eliminar el platillo con código {codigo_platillo}?"):
                cursor = conexion.cursor()
                delete_query = "DELETE FROM Platillo WHERE Id_Platillo = %s"
                cursor.execute(delete_query, (codigo_platillo,))
                conexion.commit()
                cursor.close()

                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un plato para eliminar.")

    def open_dish_window(self, title, values=None):
        window = tk.Toplevel(self.root)
        window.title(title)

        tk.Label(window, text="Codigo").grid(row=0, column=0, padx=5, pady=5)
        codigo_entry = tk.Entry(window)
        codigo_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(window, text="Platillo").grid(row=1, column=0, padx=5, pady=5)
        nombre_entry = tk.Entry(window)
        nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(window, text="Precio").grid(row=2, column=0, padx=5, pady=5)
        precio_entry = tk.Entry(window)
        precio_entry.grid(row=2, column=1, padx=5, pady=5)

        if values:
            codigo_entry.insert(0, values[0])
            nombre_entry.insert(0, values[1])
            precio_entry.insert(0, values[2])

        def save_changes():
            codigo = codigo_entry.get()
            nombre = nombre_entry.get()
            precio = precio_entry.get()

            if not codigo or not nombre or not precio:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                return

            cursor = conexion.cursor()
            if values:
                update_query = "UPDATE Platillo SET Nombre=%s, Precio=%s WHERE Id_Platillo=%s"
                cursor.execute(update_query, (nombre, precio, codigo))
            else:
                insert_query = "INSERT INTO Platillo (Id_Platillo, Nombre, Precio) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (codigo, nombre, precio))

            conexion.commit()
            cursor.close()

            window.destroy()
            self.refresh_treeview()

        tk.Button(window, text="Guardar", command=save_changes).grid(row=3, column=0, columnspan=2, pady=10)

    def refresh_treeview(self):
        cursor = conexion.cursor()
        query = "SELECT Id_Platillo, Nombre, Precio FROM Platillo"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", "end", values=row)

    def confirm_logout(self):
        if messagebox.askyesno("Cerrar Sesión", "¿Está seguro que desea cerrar sesión?"):
            self.root.quit()

    def open_order_window(self):
        messagebox.showinfo("Pedido", "Funcionalidad en desarrollo.")




if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipalCocinero(root)
    root.state("zoomed")  # Maximizar ventana automáticamente
    root.mainloop()