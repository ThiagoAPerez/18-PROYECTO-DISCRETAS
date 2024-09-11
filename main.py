from tkinter import *
from tkinter import font


window = Tk()            # CREO LA VENTANA
# LE ASIGNO UN TITULO
window.title(
    "                                                                   MATEMATICAS DISCRETAS")
window.geometry("600x220+560+300")  # LE ASIGNO UN TAMAÑO
window.resizable(False, False)  # DEFINO QUE VA TENER EL TAMAÑO FIJO
window.iconbitmap("./imagenes./icono.ico")  # LE PONEMOS UN ICONO A LA VENTANA
window.configure(bg="#2E4053")


# --------------------------------------------------------------------------------------------------
# ALGORITMO EUCLIDES


def gcd():
    """
    Calcula el maiximo comun divisor GCD de dos numeros enteros
    utilizando el algoritmo de euclidess
    """
    a = int(valora.get())
    b = int(valorb.get())
    r = 0
    q = 0
    flag = True

    while flag is True:
        q = a // b
        r = a % b

        if r == 0:
            result.delete(0, "end")
            result.insert(0, b)
            break

        elif r != 0:
            a = b
            b = r


# Agrego unas fuentes lindas :)
title_font = font.Font(family="Comic Sans MS", size=15, weight="bold")
subtitles_font = font.Font(family="Times New Roman", size=18, weight="bold")
buttons_font = font.Font(family="Times New Roman", size=12, weight="bold")
info_font = font.Font(family="Comic Sans MS", size=12, weight="bold")
warning_font = font.Font(family="Comic Sans MS", size=8,
                         weight="bold", slant="italic")


# TEXTO TITULO
lbl = Label(
    window, text="ALGORITMO DE EUCLIDES", font=title_font, fg="#F39C12", bg="#2E4053")
lbl.place(x=165, y=15)

# TEXTO GCD
lblone = Label(window, text="GCD (", font=subtitles_font,
               bg="#2E4053", fg="#ECF0F1")
lblone.place(x=70, y=70)

# TEXTO PARA SEPARAR LOS ENTRY
lbltwo = Label(window, text=",", font=subtitles_font,
               bg="#2E4053", fg="#ECF0F1")
lbltwo.place(x=210, y=80)

# TEXTO PARA DESPUES DEL ENTRY
lblthree = Label(window, text=") = ", font=subtitles_font,
                 bg="#2E4053", fg="#ECF0F1")
lblthree.place(x=290, y=70)

# ENTRY PARA TOMAR VALOR A
valora = Entry(window, bg="#D5DBDB", font=buttons_font, fg="#17202A")
valora.place(x=150, y=75, width=60, height=25)

# ENTRY PARA TOMAR VALOR B
valorb = Entry(window, bg="#D5DBDB", font=buttons_font, fg="#17202A")
valorb.place(x=225, y=75, width=60, height=25)

# ENTRY PARA MOSTRAR RESULTADO
result = Entry(window, bg="#D5DBDB", font=buttons_font, fg="#17202A")
result.place(x=330, y=75, width=70, height=25)

# BOTON PARA CALCULAR EL GCD
calculate = Button(window, text="CALCULAR",
                   font=buttons_font, command=gcd, bg="#A9CCE3", fg="#17202A")
calculate.place(x=450, y=70, width=130, height=30)


# AGREGO EL PROFESORA, APARTE PARA ASIGNARLE UN COLOR DISTINTO
teacher = Label(
    window, text="PROFESORA =", font=info_font, fg="#F39C12", bg="#2E4053")
teacher.place(x=70, y=110, height=50)

# NOMBRE DE LA PROFESORA MAS LINDA DE LA U
teacher_name = Label(
    window, text="CLARA INES VASQUEZ ECHAVARRIA", font=info_font, fg="#ECF0F1", bg="#2E4053")
teacher_name.place(x=190, y=110, height=50)

# AGREGO EL PRESENTADO POR, APARTE PARA ASIGNARLE UN COLOR DISTINTO
student = Label(
    window, text="PRESENTADO POR =", font=info_font,  fg="#F39C12", bg="#2E4053")
student.place(x=70, y=150, height=50)

# NONMBRE DEL ESTUDIANTE MAS LINDO DE LA U
student_name = Label(
    window, text="SANTIAGO ARBELÁEZ PÉREZ", font=info_font, fg="#ECF0F1", bg="#2E4053")
student_name.place(x=240, y=150, height=50)

# AGREGO UNA ADVERTENCIA QUE NO TUVE EN CUENTA A LA HORA DE REALIZAR EL CODIGO
warning = Label(
    window, text="SOLO SE ACEPTAN VALORES ENTEROS", fg="#ECF0F1", bg="#2E4053", font=warning_font)
warning.place(x=350, y=200)

# SE UTILIZA PARA MANTENER LA VENTANA ABIERTA
window.mainloop()
# --------------------------------------------------------------------------------------------------
