import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    url = url_entry.get()
    if url:
        # Generar código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Crear imagen del QR
        img = qr.make_image(fill='black', back_color='white')
        
        # Convertir a formato que Tkinter pueda mostrar
        img_tk = ImageTk.PhotoImage(img)

        # Mostrar la imagen
        qr_label.config(image=img_tk)
        qr_label.image = img_tk
    else:
        messagebox.showwarning("Input Error", "Please enter a URL.")

# Crear ventana principal
root = tk.Tk()
root.title("Generador de Códigos QR")

# Crear campo de entrada
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=10)

# Crear botón para generar el QR
generate_button = tk.Button(root, text="Generar QR", command=generate_qr)
generate_button.pack(pady=10)

# Crear etiqueta para mostrar el QR
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
