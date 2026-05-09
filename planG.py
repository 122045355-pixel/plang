import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()


def abrir_ventanatroll():

    ventanatroll = ctk.CTkToplevel(app)
    ventanatroll.geometry("400x400")
    ventanatroll.title("te dije que no hicieras click")

    texto = ctk.CTkLabel(
        ventanatroll,
        text="te dije continuar, tomate el tiempo de leer",
        font=("Arial", 20)
    )
    texto.pack(pady=20)

    imagen = ctk.CTkImage(
        light_image=Image.open("homero.jpg"),
        size=(200, 200)
    )

    label_imagen = ctk.CTkLabel(
        ventanatroll,
        text="",
        image=imagen
    )
    label_imagen.pack(pady=20)

    boton = ctk.CTkButton(
    ventanatroll,
    text="Aceptar",
    command=ventanatroll.destroy
    )
    boton.pack(pady=20)




def abrir_ventana2():

    ventana3 = ctk.CTkToplevel(app)
    ventana3.geometry("400x200")
    ventana3.title("Nueva ventana")

    texto = ctk.CTkLabel(
        ventana3,
        text="Bienvenido a la siguiente parte 😎",
        font=("Arial", 20)
    )

    texto.pack(pady=40)
    app.withdraw()

frame = ctk.CTkFrame(
    app,
    corner_radius=20
)

frame.pack(
    padx=40,
    pady=40,
    fill="both",
    expand=True
)

titulo = ctk.CTkLabel(
    frame,
    text=" Guía de Supervivencia para \nAplicaciones Web",
    font=("Arial", 32, "bold")
)
titulo.pack(pady=(30,20))

texto = ctk.CTkLabel(
    frame,
    text="Bienvenido a la guía de supervivencia de la materia de aplicaciones web sin morir en el intento :DDDD"
)
texto.pack()

texto1 = ctk.CTkLabel(
    frame,
    text="en esta aventura te presentaremos el reglamento, los valores de evaluación , objetivos y fechas importantes,\n despues pondremos a prueba tus conocimientos con un pequeño quiz "
)
texto1.pack()

texto = ctk.CTkLabel(
    frame,
    text="si entendiste todo lo anterior, haz click en continuar para continuar con la aventura"
)
texto.pack()

boton = ctk.CTkButton(
    frame,
    text="Aceptar",
    command=abrir_ventanatroll
)
boton.pack(pady=20)

boton1 = ctk.CTkButton(
    frame,
    text="Continuar",
    command=abrir_ventana2
)
boton1.pack(pady=20)

app.mainloop()