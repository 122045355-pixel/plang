import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
def reglametoredirect(ventana):
    ventana.destroy()
    inforeglamento()
def quiz1redirect(ventana):
    ventana.destroy()
    quiz1()

def inforeglamento():
    reglamento = ctk.CTkToplevel(app)
    reglamento.geometry("800x900")
    reglamento.title("Reglamento")

    titulo = ctk.CTkLabel(
        reglamento,
        text="Reglamento de la materia",
        font=("Arial", 30, "bold")
    )
    titulo.pack(pady=20)

    caja_texto = ctk.CTkTextbox(
        reglamento,
        width=700,
        height=450,
        font=("Arial", 16),
        wrap="word"
    )
    caja_texto.pack(padx=20, pady=20, fill="both", expand=True)

    reglamento_texto = """
1. Se requiere 80% de asistencia para tener derecho a evaluación parcial y 80% de trabajos en clase.

2. Se permiten 10 minutos de tolerancia y si el alumno llega después de este tiempo puede permanecer en la clase, pero no se tomará la asistencia.

3. Las faltas deberán estar justificadas mediante el correo institucional con un plazo máximo de 24 horas.

4. Las tareas y trabajos deberán subirlas al Classroom de forma individual y no se recibirán de manera extemporánea.

5. Las tareas y trabajos deben presentarse en tiempo y forma.

6. Utilizar el correo institucional para trabajar bajo la plataforma Google Classroom.

7. El plagio o copia de trabajos y/o exámenes será condicionado a reprobar la asignatura.

8. Cualquier deshonestidad académica será sancionada reprobando el parcial.

9. En caso de indisciplina o falta de respeto se aplicarán sanciones.

10. Uso de laptops y dispositivos móviles limitado únicamente a actividades académicas.

11. Prohibido el uso de audífonos durante la clase.

12. Prohibido comer y/o tomar líquidos en el salón.

13. Prohibido sentarse encima de las mesas o columpiarse en las sillas.

14. Todo tema académico debe revisarse primero con el docente.

15. Cualquier situación no prevista deberá tratarse con la dirección del programa educativo.

16. El día de entrega de calificaciones todos los estudiantes deben estar presentes.

17. Este reglamento entra en vigor después de ser aceptado por la mayoría de los estudiantes.
"""

    caja_texto.insert("1.0", reglamento_texto)

    caja_texto.configure(state="disabled")

    boton = ctk.CTkButton(
        reglamento,
        text="continuar al quiz",
        command=lambda: quiz1redirect(reglamento)
    )
    boton.pack(pady=15)


    
def verificar_respuesta1(
    respuesta1,
    respuesta2,
    respuesta3,
    resultado_label
):

    correctas = 0

    if respuesta1 == "se reprobará la asignatura ":
        correctas += 1

    if respuesta2 == "1 día":
        correctas += 1

    if respuesta3 == "10 minutos":
        correctas += 1

    resultado_label.configure(
        text=f"Obtuviste {correctas} de 3 respuestas correctas"
    )


def quiz1():

    quiz = ctk.CTkToplevel(app)
    quiz.geometry("700x900")
    quiz.title("Quiz")

    titulo = ctk.CTkLabel(
        quiz,
        text="Quiz sobre el reglamento",
        font=("Arial", 28, "bold")
    )
    titulo.pack(pady=20)

    pregunta1 = "¿cual es el castigo por plagio y/o copia de trabajos?"

    label1 = ctk.CTkLabel(
        quiz,
        text=pregunta1,
        font=("Arial", 20)
    )
    label1.pack(pady=10)

    respuesta1 = ctk.StringVar(value="")

    opciones1 = [
        "se cancela la actividad",
        "se pierde el derecho a exámen",
        "se prohibirá la entrada a esa clase",
        "se reprobará la asignatura "
    ]

    for opcion in opciones1:

        radio = ctk.CTkRadioButton(
            quiz,
            text=opcion,
            variable=respuesta1,
            value=opcion
        )

        radio.pack(pady=5)

    pregunta2 = "¿cuanto es el plazo de tiempo para justificar faltas?"

    label2 = ctk.CTkLabel(
        quiz,
        text=pregunta2,
        font=("Arial", 20)
    )
    label2.pack(pady=20)

    respuesta2 = ctk.StringVar(value="")

    opciones2 = [
        "1 semana",
        "1 día",
        "al final del parcial",
        "ese mismo día"
    ]

    for opcion in opciones2:

        radio = ctk.CTkRadioButton(
            quiz,
            text=opcion,
            variable=respuesta2,
            value=opcion
        )

        radio.pack(pady=5)

    pregunta3 = "¿Cuál es el tiempo de toleracia para entrar a clase sin falta?"

    label3 = ctk.CTkLabel(
        quiz,
        text=pregunta3,
        font=("Arial", 20)
    )
    label3.pack(pady=20)

    respuesta3 = ctk.StringVar(value="")

    opciones3 = [
        "5 minutos",
        "10 minutos",
        "15 minutos",
        "no hay tolerancia"
    ]

    for opcion in opciones3:

        radio = ctk.CTkRadioButton(
            quiz,
            text=opcion,
            variable=respuesta3,
            value=opcion
        )

        radio.pack(pady=5)
    resultado_label = ctk.CTkLabel(
    quiz,
    text="",
    font=("Arial", 18)
    )

    resultado_label.pack(pady=20)
    boton_verificar = ctk.CTkButton(
    quiz,
    text="Verificar Quiz",

    command=lambda:
    verificar_respuesta1(
        respuesta1.get(),
        respuesta2.get(),
        respuesta3.get(),
        resultado_label
    )
)

    boton_verificar.pack(pady=20)

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
        text="homero chino",
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
    ventana3.geometry("800x400")
    ventana3.title("La Cámara de las Reglas")

    texto = ctk.CTkLabel(
        ventana3,
        text="La Cámara de las Reglas",
        font=("Arial", 40)
    )
    texto1 = ctk.CTkLabel(
        ventana3,
        text="a continiación presentaremos el reglamento de la materia, \n es importante que lo leas detenidamente para el siguiente cuestionario \n una vez leido todo, presiona el botón y avanza al quiz",
        font=("Arial", 20)
    )

    texto.pack(pady=40)
    texto1.pack(pady=40)
    app.withdraw()
    boton = ctk.CTkButton(
    ventana3,
    text="Aceptar",
    command=lambda: reglametoredirect(ventana3)
    )
    boton.pack(pady=20)

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

boton2 = ctk.CTkButton(
    frame,
    text="Continuar",
    command=abrir_ventana2
)
boton2.pack(pady=20)

app.mainloop()