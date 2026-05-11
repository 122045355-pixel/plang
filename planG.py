import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
def error(quiz):

    aviso = ctk.CTkToplevel(quiz)
    aviso.geometry("300x150")
    aviso.title("Error")

    texto = ctk.CTkLabel(
        aviso,
        text="Debes contestar todas las preguntas",
        font=("Arial", 18)
    )
    texto.pack(pady=30)

    boton = ctk.CTkButton(
        aviso,
        text="Aceptar",
        command=aviso.destroy
    )
    boton.pack(pady=10)
def reglametoredirect(ventana,nueva):
    ventana.destroy()
    nueva()


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
        command=lambda: reglametoredirect(reglamento, quiz1)
    )
    boton.pack(pady=15)
    
def porcentajes():

    porcentajes = ctk.CTkToplevel(app)
    porcentajes.geometry("800x600")
    porcentajes.title("Porcentajes de Evaluación")

    titulo = ctk.CTkLabel(
        porcentajes,
        text="El Oráculo de las Notas",
        font=("Arial", 30, "bold")
    )
    titulo.pack(pady=20)

    texto = ctk.CTkLabel(
        porcentajes,
        text="revisa atentamente los porcentajes de evaluación",
        font=("Arial", 20)
    )
    texto.pack(pady=20)

    imagen = ctk.CTkImage(
        light_image=Image.open("porcentajes.png"),
        size=(500, 200)
    )

    label_imagen = ctk.CTkLabel(
        porcentajes,
        text="",
        image=imagen
    )

    label_imagen.pack(pady=20)

   
    label_imagen.image = imagen

    boton = ctk.CTkButton(
        porcentajes,
        text="Continuar",
        command=lambda: reglametoredirect(porcentajes, quiz2)
    )

    boton.pack(pady=20)


def ventanaAprobado():

    ventanaAprobado = ctk.CTkToplevel(app)
    ventanaAprobado.geometry("400x400")
    ventanaAprobado.title("felicidades")

    texto = ctk.CTkLabel(
        ventanaAprobado,
        text="felicidades, aprobaste el quiz, ahora puedes continuar con la materia",
        font=("Arial", 20)
    )
    texto.pack(pady=20)

    imagen = ctk.CTkImage(
        light_image=Image.open("aprobado.jpg"),
        size=(200, 200)
    )

    label_imagen = ctk.CTkLabel(
        ventanaAprobado,
        text="",
        image=imagen
    )
    label_imagen.pack(pady=20)

    boton = ctk.CTkButton(
    ventanaAprobado,
    text="Aceptar",
    command=lambda: reglametoredirect(ventanaAprobado, abrir_ventana3)
    )
    boton.pack(pady=20)

def ventanaFracaso():

    ventanaFracaso = ctk.CTkToplevel(app)
    ventanaFracaso.geometry("400x400")
    ventanaFracaso.title("efe en el chat")

    texto = ctk.CTkLabel(
        ventanaFracaso,
        text="fracasaste el quiz, te recomiendo leer el reglamento detenidamente y volver a intentarlo",
        font=("Arial", 20)
    )
    texto.pack(pady=20)

    imagen = ctk.CTkImage(
        light_image=Image.open("Fracaso.jpg"),
        size=(200, 200)
    )

    label_imagen = ctk.CTkLabel(
        ventanaFracaso,
        text="",
        image=imagen
    )
    label_imagen.pack(pady=20)

    boton = ctk.CTkButton(
    ventanaFracaso,
    text="Aceptar",
    command=lambda:
    reglametoredirect(
        ventanaFracaso,
        inforeglamento
    )
    )
    boton.pack(pady=20)
def ventanaAprobado2():

    ventanaAprobado2 = ctk.CTkToplevel(app)
    ventanaAprobado2.geometry("400x400")
    ventanaAprobado2.title("felicidades")

    texto = ctk.CTkLabel(
        ventanaAprobado2,
        text="felicidades, aprobaste el quiz, tus padres deben sentirse orullosos :,D",
        font=("Arial", 20)
    )
    texto.pack(pady=20)

    imagen = ctk.CTkImage(
        light_image=Image.open("exito.jpg"),
        size=(200, 200)
    )

    label_imagen = ctk.CTkLabel(
        ventanaAprobado2,
        text="",
        image=imagen
    )
    label_imagen.pack(pady=20)

    boton = ctk.CTkButton(
    ventanaAprobado2,
    text="Aceptar",
    command=lambda: reglametoredirect(ventanaAprobado2, abrir_ventana4)
    )
    boton.pack(pady=20)

def ventanaFracaso2():

    ventanaFracaso2 = ctk.CTkToplevel(app)
    ventanaFracaso2.geometry("400x400")
    ventanaFracaso2.title("efe en el chat")

    texto = ctk.CTkLabel(
        ventanaFracaso2,
        text="fracasaste el quiz, llegaste mas lejos animo :DDD",
        font=("Arial", 20)
    )
    texto.pack(pady=20)

    imagen = ctk.CTkImage(
        light_image=Image.open("hulk.jpg"),
        size=(200, 200)
    )

    label_imagen = ctk.CTkLabel(
        ventanaFracaso2,
        text="",
        image=imagen
    )
    label_imagen.pack(pady=20)

    boton = ctk.CTkButton(
    ventanaFracaso2,
    text="Aceptar",
    command=lambda:
    reglametoredirect(
        ventanaFracaso2,
        porcentajes
    )
    )
    boton.pack(pady=20)
def ventanaAprobado3():

    ventanaAprobado3 = ctk.CTkToplevel(app)
    ventanaAprobado3.geometry("400x400")
    ventanaAprobado3.title("felicidades")

    texto = ctk.CTkLabel(
        ventanaAprobado3,
        text="son lagrimas de orgullo :,,D",
        font=("Arial", 20)
    )
    texto.pack(pady=20)

    imagen = ctk.CTkImage(
        light_image=Image.open("espacio.jpg"),
        size=(200, 200)
    )

    label_imagen = ctk.CTkLabel(
        ventanaAprobado3,
        text="",
        image=imagen
    )
    label_imagen.pack(pady=20)

    boton = ctk.CTkButton(
    ventanaAprobado3,
    text="Aceptar",
    command=lambda: reglametoredirect(ventanaAprobado3, abrir_ventana5)
    )
    boton.pack(pady=20)

def ventanaFracaso3():

    ventanaFracaso3 = ctk.CTkToplevel(app)
    ventanaFracaso3.geometry("400x400")
    ventanaFracaso3.title("efe en el chat")

    texto = ctk.CTkLabel(
        ventanaFracaso3,
        text="se que te quieres rendir pero tu mamá no crió a un cobarde",
        font=("Arial", 20)
    )
    texto.pack(pady=20)

    imagen = ctk.CTkImage(
        light_image=Image.open("llorando.jpg"),
        size=(200, 200)
    )

    label_imagen = ctk.CTkLabel(
        ventanaFracaso3,
        text="",
        image=imagen
    )
    label_imagen.pack(pady=20)

    boton = ctk.CTkButton(
    ventanaFracaso3,
    text="Aceptar",
    command=lambda:
    reglametoredirect(
        ventanaFracaso3,
        objetivos
    )
    )
    boton.pack(pady=20)
def ventanaFracaso4():

    ventanaFracaso4 = ctk.CTkToplevel(app)
    ventanaFracaso4.geometry("400x400")
    ventanaFracaso4.title("efe en el chat")

    texto = ctk.CTkLabel(
        ventanaFracaso4,
        text="si 3 anos de universidad no te detuvieron, este quiz tampoco lo hará (no tengo la letra que sigue de la n xd)",
        font=("Arial", 20)
    )
    texto.pack(pady=20)

    imagen = ctk.CTkImage(
        light_image=Image.open("pum.jpg"),
        size=(200, 200)
    )

    label_imagen = ctk.CTkLabel(
        ventanaFracaso4,
        text="",
        image=imagen
    )
    label_imagen.pack(pady=20)

    boton = ctk.CTkButton(
    ventanaFracaso4,
    text="Aceptar",
    command=lambda:
    reglametoredirect(
        ventanaFracaso4,
        Fechas
    )
    )
    boton.pack(pady=20)
def ventanaAprobado4():

    ventanaAprobado4 = ctk.CTkToplevel(app)
    ventanaAprobado4.geometry("400x400")
    ventanaAprobado4.title("felicidades")

    texto = ctk.CTkLabel(
        ventanaAprobado4,
        text="lo lograste, a partir de ahora eres un sobreviviente de aplicaciones web :DDD",
        font=("Arial", 20)
    )
    texto.pack(pady=20)

    imagen = ctk.CTkImage(
        light_image=Image.open("campeon.jpg"),
        size=(200, 200)
    )

    label_imagen = ctk.CTkLabel(
        ventanaAprobado4,
        text="",
        image=imagen
    )
    label_imagen.pack(pady=20)

    boton = ctk.CTkButton(
    ventanaAprobado4,
    text="Aceptar",
    command=ventanaAprobado4.destroy
    )
    boton.pack(pady=20)



    
def verificar_respuesta1(
    quiz,
    respuesta1,
    respuesta2,
    respuesta3,
    
):
    if respuesta1 == "" or respuesta2 == "" or respuesta3 == "":
        error(quiz)
        return

    correctas = 0

    if respuesta1 == "se reprobará la asignatura ":
        correctas += 1

    if respuesta2 == "1 día":
        correctas += 1

    if respuesta3 == "10 minutos":
        correctas += 1


    if correctas < 2:
        reglametoredirect(quiz, ventanaFracaso)
    else:

        reglametoredirect(quiz, ventanaAprobado)



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
    boton_verificar = ctk.CTkButton(
    quiz,
    text="Verificar Quiz",

    command=lambda:
    verificar_respuesta1(
        quiz,
        respuesta1.get(),
        respuesta2.get(),
        respuesta3.get(),
        
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
    command=lambda: reglametoredirect(ventana3,inforeglamento)
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

def abrir_ventana3():

    ventana3 = ctk.CTkToplevel(app)
    ventana3.geometry("800x400")
    ventana3.title("La Cámara de las Reglas")

    texto = ctk.CTkLabel(
        ventana3,
        text="El oraculo de las notas",
        font=("Arial", 40)
    )
    texto1 = ctk.CTkLabel(
        ventana3,
        text="Felicidads, pasaste a la siguiente prueba, \n a continuación te mostraremos los porcentajes de la evaluación \n una vez leido todo, presiona el botón y avanza al quiz",
        font=("Arial", 20)
    )

    texto.pack(pady=40)
    texto1.pack(pady=40)
    app.withdraw()
    boton = ctk.CTkButton(
    ventana3,
    text="Aceptar",
    command=lambda: reglametoredirect(ventana3,porcentajes)
    )
    boton.pack(pady=20)
def abrir_ventana4():

    ventana4 = ctk.CTkToplevel(app)
    ventana4.geometry("800x400")
    ventana4.title("La Cámara de las Reglas")

    texto = ctk.CTkLabel(
        ventana4,
        text="skills a desbloquear",
        font=("Arial", 40)
    )
    texto1 = ctk.CTkLabel(
        ventana4,
        text="increible, vamos a medio camino, \n ahora realizaremos repaso a las skills a practica \n una vez leido todo, presiona el botón y avanza al quiz",
        font=("Arial", 20)
    )

    texto.pack(pady=40)
    texto1.pack(pady=40)
    app.withdraw()
    boton = ctk.CTkButton(
    ventana4,
    text="Aceptar",
    command=lambda: reglametoredirect(ventana4,objetivos)
    )
    boton.pack(pady=20)
def abrir_ventana5():

    ventana5 = ctk.CTkToplevel(app)
    ventana5.geometry("800x400")
    ventana5.title("Skills a Desbloquear")

    texto = ctk.CTkLabel(
        ventana5,
        text="skills a desbloquear",
        font=("Arial", 40)
    )
    texto1 = ctk.CTkLabel(
        ventana5,
        text="increible, vamos a medio caminoun paso mas viejo, \n por último debemos estudiar las fechas importantes de la asignatura \n una vez leido todo, presiona el botón y avanza al quiz",
        font=("Arial", 20)
    )

    texto.pack(pady=40)
    texto1.pack(pady=40)
    app.withdraw()
    boton = ctk.CTkButton(
    ventana5,
    text="Aceptar",
    command=lambda: reglametoredirect(ventana5,Fechas)
    )
    boton.pack(pady=20)
def verificar_respuesta2(
    quiz,
    respuesta1,
    respuesta2,
    respuesta3,
):
    if respuesta1 == "" or respuesta2 == "" or respuesta3 == "":
        error(quiz)
        return
    correctas = 0

    if respuesta1 == "40%":
        correctas += 1

    if respuesta2 == "50%":
        correctas += 1

    if respuesta3 == "30%":
        correctas += 1

    if correctas < 2:
        reglametoredirect(quiz, ventanaFracaso2)
    else:
        reglametoredirect(quiz, ventanaAprobado2)


def quiz2():

    quiz = ctk.CTkToplevel(app)
    quiz.geometry("700x900")
    quiz.title("Quiz sobre porcentajes")

    titulo = ctk.CTkLabel(
        quiz,
        text="Quiz sobre porcentajes de evaluación",
        font=("Arial", 28, "bold")
    )
    titulo.pack(pady=20)

    
    pregunta1 = "¿Cuánto vale la evidencia de conocimiento en el 1P?"

    label1 = ctk.CTkLabel(
        quiz,
        text=pregunta1,
        font=("Arial", 20)
    )
    label1.pack(pady=10)

    respuesta1 = ctk.StringVar(value="")

    opciones1 = [
        "10%",
        "20%",
        "30%",
        "40%"
    ]

    for opcion in opciones1:

        radio = ctk.CTkRadioButton(
            quiz,
            text=opcion,
            variable=respuesta1,
            value=opcion
        )

        radio.pack(pady=5)

    
    pregunta2 = "¿Cuánto vale el proyecto integrador en el 3P?"

    label2 = ctk.CTkLabel(
        quiz,
        text=pregunta2,
        font=("Arial", 20)
    )
    label2.pack(pady=20)

    respuesta2 = ctk.StringVar(value="")

    opciones2 = [
        "10%",
        "20%",
        "30%",
        "50%"
    ]

    for opcion in opciones2:

        radio = ctk.CTkRadioButton(
            quiz,
            text=opcion,
            variable=respuesta2,
            value=opcion
        )

        radio.pack(pady=5)

    
    pregunta3 = "¿Cuánto vale la evidencia de producto en el 2P?"

    label3 = ctk.CTkLabel(
        quiz,
        text=pregunta3,
        font=("Arial", 20)
    )
    label3.pack(pady=20)

    respuesta3 = ctk.StringVar(value="")

    opciones3 = [
        "10%",
        "20%",
        "30%",
        "40%"
    ]

    for opcion in opciones3:

        radio = ctk.CTkRadioButton(
            quiz,
            text=opcion,
            variable=respuesta3,
            value=opcion
        )

        radio.pack(pady=5)

    verificar = ctk.CTkButton(
        quiz,
        text="Verificar Quiz",
        command=lambda:
        verificar_respuesta2(
            quiz,
            respuesta1.get(),
            respuesta2.get(),
            respuesta3.get(),
        )
    )

    verificar.pack(pady=20)

def objetivos():

    info = ctk.CTkToplevel(app)
    info.geometry("1000x800")
    info.title("objetivos generales y específicos")

    titulo = ctk.CTkLabel(
        info,
        text="Información objetivos y skills a desbloquear",
        font=("Arial", 32, "bold")
    )
    titulo.pack(pady=20)

    objetivo_titulo = ctk.CTkLabel(
        info,
        text="OBJETIVO",
        font=("Arial", 24, "bold")
    )
    objetivo_titulo.pack(pady=10)

    objetivo = ctk.CTkLabel(
        info,
        text="Desarrollará aplicaciones móviles mediante lenguajes de programación,\n"
             "entornos de desarrollo, diseño de interfaces de usuario,\n"
             "arquitecturas, patrones de diseño y herramientas de programación móvil.",
        font=("Arial", 18),
        justify="center"
    )
    objetivo.pack(pady=10)

    competencias_titulo = ctk.CTkLabel(
        info,
        text="COMPETENCIAS QUE ADQUIERE",
        font=("Arial", 24, "bold")
    )
    competencias_titulo.pack(pady=10)

    competencias = ctk.CTkLabel(
        info,
        text="Soluciones tecnológicas multiplataforma de software web y móvil\n"
             "utilizando programación orientada a objetos, frameworks,\n"
             "bases de datos, estándares de calidad y diseño.",
        font=("Arial", 18),
        justify="center"
    )
    competencias.pack(pady=10)

    temario_titulo = ctk.CTkLabel(
        info,
        text="TEMARIO DE LA ASIGNATURA",
        font=("Arial", 24, "bold")
    )
    temario_titulo.pack(pady=20)

    tabla = ctk.CTkTextbox(
        info,
        width=800,
        height=250,
        font=("Consolas", 18)
    )
    tabla.pack(pady=10)

    contenido = """
    unidad/horas teoria/horas practica

1. Introducción al desarrollo apps móviles   10  8

2. Diseño de aplicaciones móviles            10  14

3. Programación de aplicaciones móviles      12  24

4. Publicación de aplicaciones móviles        4   8
"""

    tabla.insert("1.0", contenido)
    tabla.configure(state="disabled")

    boton = ctk.CTkButton(
        info,
        text="Continuar al Quiz",
        command=lambda: reglametoredirect(info, quiz3)
    )
    boton.pack(pady=20)


def verificar_respuesta3(
    quiz,
    respuesta1,
    respuesta2,
    respuesta3,
):
    if respuesta1 == "" or respuesta2 == "" or respuesta3 == "":
        error(quiz)
        return

    correctas = 0

    if respuesta1 == "Programación orientada a objetos":
        correctas += 1

    if respuesta2 == "24":
        correctas += 1

    if respuesta3 == "Publicación de aplicaciones móviles":
        correctas += 1

    if correctas < 2:
        reglametoredirect(quiz, ventanaFracaso3)
    else:
        reglametoredirect(quiz, ventanaAprobado3)


def quiz3():

    quiz = ctk.CTkToplevel(app)
    quiz.geometry("700x900")
    quiz.title("Quiz Información General")

    titulo = ctk.CTkLabel(
        quiz,
        text="Quiz de Información General",
        font=("Arial", 28, "bold")
    )
    titulo.pack(pady=20)

   
    pregunta1 = "¿Qué tipo de programación se menciona en las competencias?"

    label1 = ctk.CTkLabel(
        quiz,
        text=pregunta1,
        font=("Arial", 20)
    )
    label1.pack(pady=10)

    respuesta1 = ctk.StringVar(value="")

    opciones1 = [
        "Programación funcional",
        "Programación orientada a objetos",
        "Programación en ensamblador",
        "Programación lineal"
    ]

    for opcion in opciones1:

        radio = ctk.CTkRadioButton(
            quiz,
            text=opcion,
            variable=respuesta1,
            value=opcion
        )

        radio.pack(pady=5)

  
    pregunta2 = "¿Cuántas horas prácticas tiene la unidad 3?"

    label2 = ctk.CTkLabel(
        quiz,
        text=pregunta2,
        font=("Arial", 20)
    )
    label2.pack(pady=20)

    respuesta2 = ctk.StringVar(value="")

    opciones2 = [
        "8",
        "10",
        "24",
        "12"
    ]

    for opcion in opciones2:

        radio = ctk.CTkRadioButton(
            quiz,
            text=opcion,
            variable=respuesta2,
            value=opcion
        )

        radio.pack(pady=5)

  
    pregunta3 = "¿Cuál es la última unidad del temario?"

    label3 = ctk.CTkLabel(
        quiz,
        text=pregunta3,
        font=("Arial", 20)
    )
    label3.pack(pady=20)

    respuesta3 = ctk.StringVar(value="")

    opciones3 = [
        "Diseño de aplicaciones móviles",
        "Programación de aplicaciones móviles",
        "Publicación de aplicaciones móviles",
        "Introducción al desarrollo apps móviles"
    ]

    for opcion in opciones3:

        radio = ctk.CTkRadioButton(
            quiz,
            text=opcion,
            variable=respuesta3,
            value=opcion
        )

        radio.pack(pady=5)

    boton_verificar = ctk.CTkButton(
        quiz,
        text="Verificar Quiz",
        command=lambda:
        verificar_respuesta3(
            quiz,
            respuesta1.get(),
            respuesta2.get(),
            respuesta3.get(),
        )
    )

    boton_verificar.pack(pady=20)
def Fechas():

    fecha = ctk.CTkToplevel(app)
    fecha.geometry("800x600")
    fecha.title("Fechas Importantes")

    titulo = ctk.CTkLabel(
        fecha,
        text="Fechas Importantes",
        font=("Arial", 30, "bold")
    )
    titulo.pack(pady=20)

    texto = ctk.CTkLabel(
        fecha,
        text="revisa atentamente las fechas importantes",
        font=("Arial", 20)
    )
    texto.pack(pady=20)

    imagen = ctk.CTkImage(
        light_image=Image.open("fechas.jpg"),
        size=(500, 200)
    )

    label_imagen = ctk.CTkLabel(
        fecha,
        text="",
        image=imagen
    )

    label_imagen.pack(pady=20)

   
    label_imagen.image = imagen

    boton = ctk.CTkButton(
        fecha,
        text="Continuar",
        command=lambda: reglametoredirect(fecha, quiz4)
    )

    boton.pack(pady=20)
def verificar_respuesta4(
    quiz,
    respuesta1,
    respuesta2,
    respuesta3,
):
    if respuesta1 == "" or respuesta2 == "" or respuesta3 == "":
        error(quiz)
        return
    correctas = 0

    if respuesta1 == "01-06-26":
        correctas += 1

    if respuesta2 == "17-08-26":
        correctas += 1

    if respuesta3 == "06-07-26":
        correctas += 1

    if correctas < 2:
        reglametoredirect(quiz, ventanaFracaso4)
    else:
        reglametoredirect(quiz, ventanaAprobado4)
def quiz4():

    quiz = ctk.CTkToplevel(app)
    quiz.geometry("700x700")
    quiz.title("Quiz Fechas Importantes")

    titulo = ctk.CTkLabel(
        quiz,
        text="Quiz de Fechas Importantes",
        font=("Arial", 28, "bold")
    )
    titulo.pack(pady=20)

    
    pregunta1 = ctk.CTkLabel(
        quiz,
        text="¿Cuándo es el 1er parcial?",
        font=("Arial", 20)
    )
    pregunta1.pack(pady=10)

    respuesta1 = ctk.StringVar(value="")

    opciones1 = [
        "01-06-26",
        "06-07-26",
        "10-08-26",
        "17-08-26"
    ]

    for opcion in opciones1:

        radio = ctk.CTkRadioButton(
            quiz,
            text=opcion,
            variable=respuesta1,
            value=opcion
        )

        radio.pack()

    
    pregunta2 = ctk.CTkLabel(
        quiz,
        text="¿Cuándo es el examen final?",
        font=("Arial", 20)
    )
    pregunta2.pack(pady=20)

    respuesta2 = ctk.StringVar(value="")

    opciones2 = [
        "01-06-26",
        "17-08-26",
        "06-07-26",
        "10-08-26"
    ]

    for opcion in opciones2:

        radio = ctk.CTkRadioButton(
            quiz,
            text=opcion,
            variable=respuesta2,
            value=opcion
        )

        radio.pack()

    
    pregunta3 = ctk.CTkLabel(
        quiz,
        text="¿Cuándo es el 2do parcial?",
        font=("Arial", 20)
    )
    pregunta3.pack(pady=20)

    respuesta3 = ctk.StringVar(value="")

    opciones3 = [
        "17-08-26",
        "10-08-26",
        "06-07-26",
        "01-06-26"
    ]

    for opcion in opciones3:

        radio = ctk.CTkRadioButton(
            quiz,
            text=opcion,
            variable=respuesta3,
            value=opcion
        )

        radio.pack()

    boton = ctk.CTkButton(
        quiz,
        text="Verificar Quiz",
        command=lambda:
        verificar_respuesta4(
            quiz,
            respuesta1.get(),
            respuesta2.get(),
            respuesta3.get()
        )
    )

    boton.pack(pady=30)


app.mainloop()