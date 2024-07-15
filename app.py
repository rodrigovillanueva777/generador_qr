import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import qrcode
from PIL import Image, ImageTk
import pyperclip

def generate_qr():
    url = url_entry.get()
    if url:
        # Obtener colores seleccionados
        fill_color = fill_color_var.get()
        back_color = back_color_var.get()

        # Generar código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Crear imagen del QR con colores personalizados
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # Convertir a formato que Tkinter pueda mostrar
        img_tk = ImageTk.PhotoImage(img)

        # Mostrar la imagen
        qr_label.config(image=img_tk)
        qr_label.image = img_tk

        # Guardar imagen en variable de instancia
        global saved_img
        saved_img = img
    else:
        messagebox.showwarning("Input Error", "Please enter a URL.")

def paste_from_clipboard():
    try:
        url = pyperclip.paste()
        url_entry.delete(0, tk.END)
        url_entry.insert(0, url)
    except Exception as e:
        messagebox.showerror("Paste Error", str(e))

def save_image():
    if saved_img:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            saved_img.save(file_path)
    else:
        messagebox.showwarning("Save Error", "No QR code to save.")

def choose_fill_color():
    color = colorchooser.askcolor(title="Choose QR Code Color")[1]
    if color:
        fill_color_var.set(color)
        fill_color_display.config(bg=color)

def choose_back_color():
    color = colorchooser.askcolor(title="Choose Background Color")[1]
    if color:
        back_color_var.set(color)
        back_color_display.config(bg=color)

# Crear ventana principal
root = tk.Tk()
root.title("Generador de Códigos QR")

# Crear marco para entrada y botones
frame = tk.Frame(root)
frame.pack(pady=10)

# Crear campo de entrada
url_entry = tk.Entry(frame, width=40)
url_entry.pack(side=tk.LEFT, padx=5)

# Crear botón de pegado
paste_button = tk.Button(frame, text="Pegar", command=paste_from_clipboard)
paste_button.pack(side=tk.LEFT, padx=5)

# Crear marco para botones de color
color_frame = tk.Frame(root)
color_frame.pack(pady=10)

# Crear botones para seleccionar colores
fill_color_var = tk.StringVar(value="#000000")  # Color por defecto negro
back_color_var = tk.StringVar(value="#FFFFFF")  # Color por defecto blanco

fill_color_button = tk.Button(color_frame, text="Elegir Color QR", command=choose_fill_color)
fill_color_button.grid(row=0, column=0, padx=5)

fill_color_display = tk.Label(color_frame, bg=fill_color_var.get(), width=10, height=1, relief=tk.SOLID)
fill_color_display.grid(row=0, column=1, padx=5)

back_color_button = tk.Button(color_frame, text="Elegir Color Fondo", command=choose_back_color)
back_color_button.grid(row=0, column=2, padx=5)

back_color_display = tk.Label(color_frame, bg=back_color_var.get(), width=10, height=1, relief=tk.SOLID)
back_color_display.grid(row=0, column=3, padx=5)

# Crear botón para generar el QR
generate_button = tk.Button(root, text="Generar QR", command=generate_qr)
generate_button.pack(pady=10)

# Crear botón para guardar la imagen
save_button = tk.Button(root, text="Guardar Imagen", command=save_image)
save_button.pack(pady=10)

# Crear etiqueta para mostrar el QR
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Variable para almacenar la imagen generada
saved_img = None

# Ejecutar la aplicación
root.mainloop()
