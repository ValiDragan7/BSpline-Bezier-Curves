import random
import time
import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import Menu
from tkinter import messagebox

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.rcParams['animation.ffmpeg_path'] = 'C:/Users/Vali/Desktop/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe'


def generare_automata():
    for entry_x, entry_y, entry_z in zip(entry_x_list, entry_y_list, entry_z_list):
        entry_x.delete(0, tk.END)
        entry_x.insert(0, str(random.randint(-100, 100)))
        entry_y.delete(0, tk.END)
        entry_y.insert(0, str(random.randint(-100, 100)))
        entry_z.delete(0, tk.END)
        entry_z.insert(0, str(random.randint(-100, 100)))


def salvare_grafic():
    plt.savefig("grafic.jpg")


def buton_save_grafic():
    salvare_grafic()
    image = Image.open("grafic.jpg")
    messagebox.showinfo("Salvat!", "Graficul a fost salvat sub forma de .jpg in folderul proiectului.")
    image.show()


# def validare_continut(content):
#     if not content.isdigit():
#         messagebox.showerror("Eroare","Continutul trebuie sa fie un numar.")
#         return False
#     return True


def plot3d_bezier():
    # input-urile
    for entry_x, entry_y, entry_z in zip(entry_x_list, entry_y_list, entry_z_list):
        x_val = entry_x.get()
        y_val = entry_y.get()
        z_val = entry_z.get()

        if not x_val:
            display_error_message("Coordonata x")
            return
        if not y_val:
            display_error_message("Coordonata y")
            return
        if not z_val:
            display_error_message("Coordonata z")
            return
        # if not validare_continut(x_val):
        #     return
        # if not validare_continut(y_val):
        #     return
        # if not validare_continut(z_val):
        #     return
    start_time_meth = time.time()

    #  input - float
    x = [float(entry_x.get()) for entry_x in entry_x_list]
    y = [float(entry_y.get()) for entry_y in entry_y_list]
    z = [float(entry_z.get()) for entry_z in entry_z_list]

    cells = 100
    nr_puncte = np.size(x, 0)
    n = nr_puncte - 1
    i = 0
    t = np.linspace(0, 1, cells)
    b = []

    iteration = 0
    approx_value = np.zeros((3, cells))
    abs_error = np.inf
    elapsed_time_meth = 0.0
    elapsed_time_bezier = 0.0
    start_time_bezier = time.time()

    xBezier = np.zeros((1, cells))
    yBezier = np.zeros((1, cells))
    zBezier = np.zeros((1, cells))

    def Ni(n, i):  # coeficientii binomiali
        return np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i))

    def basisFunction(n, i, t):
        J = np.array(Ni(n, i) * (t ** i) * (1 - t) ** (n - 1))
        return J

    for k in range(0, nr_puncte):
        b.append(basisFunction(n, i, t))

        xBezier = basisFunction(n, i, t) * x[k] + xBezier
        yBezier = basisFunction(n, i, t) * y[k] + yBezier
        zBezier = basisFunction(n, i, t) * z[k] + zBezier
        i += 1
        iteration += 1

    # end_time_bezier = time.time()
    # elapsed_time_bezier = end_time_bezier - start_time_bezier

    # approx_value = np.vstack((xBezier, yBezier, zBezier))
    # abs_error = np.linalg.norm(approx_value - np.vstack((xBezier, yBezier, zBezier)), axis=0)

    # end_time_meth = time.time()
    # elapsed_time_meth = end_time_meth - start_time_meth
    # info_text = f"Iteration: {iteration}\n"
    # info_text += f"Approximated value:\n{xBezier}\n{yBezier}\n{zBezier}\n"
    # info_text += f"Absolute Error: {abs_error}\n"
    # info_text += f"Elapsed time method: {elapsed_time_meth} sec\n"
    # info_text += f"Elapsed time bezier: {elapsed_time_bezier} sec\n"

    for line in b:
        plt.plot(t, line)

    fig1 = plt.figure(figsize=(4, 4))
    ax1 = fig1.add_subplot(111, projection="3d")
    ax1.scatter(x, y, z, c="black")
    ax1.plot(xBezier[0], yBezier[0], zBezier[0], c="blue")

    # new window  3D plot
    window = tk.Toplevel(root)
    window.title("Bezier 3D ")
    canvas = FigureCanvasTkAgg(fig1, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    # info_label=tk.Label(window,text=info_text,font=("Arial",10))
    # info_label.pack()


def plot2d_bezier():
    # Validare
    for entry_x, entry_y in zip(entry_x_list, entry_y_list):
        x_val = entry_x.get()
        y_val = entry_y.get()

        if not x_val:
            display_error_message("Coordonata x")
            return
        if not y_val:
            display_error_message("Coordonata y")
            return
        # if not validare_continut(x_val):
        #     return
        # if not validare_continut(y_val):
        #     return

    # input-float
    x = [float(entry_x.get()) for entry_x in entry_x_list]
    y = [float(entry_y.get()) for entry_y in entry_y_list]

    cells = 100
    nr_puncte = np.size(x, 0)
    n = nr_puncte - 1
    i = 0
    t = np.linspace(0, 1, cells)
    b = []

    xBezier = np.zeros((1, cells))
    yBezier = np.zeros((1, cells))

    def Ni(n, i):
        return np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i))

    def basisFunction(n, i, t):
        J = np.array(Ni(n, i) * (t ** i) * (1 - t) ** (n - 1))
        return J

    for k in range(0, nr_puncte):
        b.append(basisFunction(n, i, t))

        xBezier = basisFunction(n, i, t) * x[k] + xBezier
        yBezier = basisFunction(n, i, t) * y[k] + yBezier
        i += 1

    for line in b:
        plt.plot(t, line)

    fig2 = plt.figure(figsize=(4, 4))
    plt.scatter(x, y, c="black")
    plt.plot(xBezier[0], yBezier[0], c="blue")
    plt.plot(x, y, linestyle="dashed", c="gray")

    # fereastra noua pt grafic 2d
    window = tk.Toplevel(root)
    window.title("Bezier 2D ")
    canvas = FigureCanvasTkAgg(fig2, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def display_error_message(field_description):
    error_message = f"In casuta {field_description} trebuie sa fie o valoare"
    error_label.config(text=error_message)


def citire_fisier():
    filepath = filedialog.askopenfilename(title="Selecteaza fisierul de intrare")

    if filepath:
        try:
            with open(filepath, "r") as file:
                lines = file.readlines()

                lines = [line.strip() for line in lines if line.strip()]

                if len(lines) < len(entry_x_list):
                    display_error_message("Insuficiente date de intrare")
                    return

                for i, line in enumerate(lines[:len(entry_x_list)]):
                    values = line.split()
                    if len(values) == 3:
                        entry_x_list[i].delete(0, tk.END)
                        entry_x_list[i].insert(0, values[0])
                        entry_y_list[i].delete(0, tk.END)
                        entry_y_list[i].insert(0, values[1])
                        entry_z_list[i].delete(0, tk.END)
                        entry_z_list[i].insert(0, values[2])

        except Exception as e:
            display_error_message(str(e))


root = tk.Tk()
root.title("Curbe Bezier")

entry_x_list = []
entry_y_list = []
entry_z_list = []

tk.Label(root, text="Coordonata x").grid(row=0, column=1)
tk.Label(root, text="Coordonata y").grid(row=0, column=2)
tk.Label(root, text="Coordonata z").grid(row=0, column=3)

for i in range(4):
    tk.Label(root, text=f"Point {i + 1}").grid(row=i + 1, column=0)
    entry_x = tk.Entry(root)
    entry_x.grid(row=i + 1, column=1)
    entry_x_list.append(entry_x)

    entry_y = tk.Entry(root)
    entry_y.grid(row=i + 1, column=2)
    entry_y_list.append(entry_y)

    entry_z = tk.Entry(root)
    entry_z.grid(row=i + 1, column=3)
    entry_z_list.append(entry_z)


def resetare_valori():
    for entry_x, entry_y, entry_z in zip(entry_x_list, entry_y_list, entry_z_list):
        entry_x.delete(0, tk.END)
        entry_y.delete(0, tk.END)
        entry_z.delete(0, tk.END)
        error_label.config(text="")


def movie_2d():
    for entry_x, entry_y, entry_z in zip(entry_x_list, entry_y_list, entry_z_list):
        x_val = entry_x.get()
        y_val = entry_y.get()
        z_val = entry_z.get()

        if not x_val:
            display_error_message("Coordonata x")
            return
        if not y_val:
            display_error_message("Coordonata y")
            return
        if not z_val:
            display_error_message("Coordonata z")
            return

    # Generare coordonate x, y, z
    x = [float(entry_x.get()) for entry_x in entry_x_list]
    y = [float(entry_y.get()) for entry_y in entry_y_list]
    z = [float(entry_z.get()) for entry_z in entry_z_list]

    fig = plt.figure()

    # Graficul 2D
    ax = fig.add_subplot(111)

    def update_frame(frame):
        ax.cla()
        ax.scatter(x, y, c="black")

        t = np.linspace(0, 1, cells)
        b = []
        xBezier = np.zeros((1, cells))
        yBezier = np.zeros((1, cells))

        def Ni(n, i):
            return np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i))

        def basisFunction(n, i, t):
            J = np.array(Ni(n, i) * (t ** i) * (1 - t) ** (n - 1))
            return J

        i = 0
        for k in range(0, nr_puncte):
            b.append(basisFunction(n, i, t))

            xBezier = basisFunction(n, i, t) * x[k] + xBezier
            yBezier = basisFunction(n, i, t) * y[k] + yBezier
            i += 1

        ax.plot(xBezier[0][:frame + 1], yBezier[0][:frame + 1], c="blue")

    cells = 100
    nr_puncte = np.size(x, 0)
    n = nr_puncte - 1

    frames = cells  # Numărul de cadre este egal cu cells
    anim = animation.FuncAnimation(fig, update_frame, frames=frames, interval=200, repeat=False)

    # Salvare ca fișier video
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=3, metadata=dict(artist='Me'), bitrate=1800)
    anim.save('bezier_movie.mp4', writer=writer)

    plt.show()


def movie_3d():
    for entry_x, entry_y, entry_z in zip(entry_x_list, entry_y_list, entry_z_list):
        x_val = entry_x.get()
        y_val = entry_y.get()
        z_val = entry_z.get()

        if not x_val:
            display_error_message("Coordonata x")
            return
        if not y_val:
            display_error_message("Coordonata y")
            return
        if not z_val:
            display_error_message("Coordonata z")
            return

    # Generare coordonate x, y, z
    x = [float(entry_x.get()) for entry_x in entry_x_list]
    y = [float(entry_y.get()) for entry_y in entry_y_list]
    z = [float(entry_z.get()) for entry_z in entry_z_list]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    def update_frame(frame):
        ax.cla()
        ax.scatter(x, y, z, c="black")

        t = np.linspace(0, 1, cells)
        b = []
        xBezier = np.zeros((1, cells))
        yBezier = np.zeros((1, cells))
        zBezier = np.zeros((1, cells))

        def Ni(n, i):
            return np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i))

        def basisFunction(n, i, t):
            J = np.array(Ni(n, i) * (t ** i) * (1 - t) ** (n - 1))
            return J

        i = 0
        for k in range(0, nr_puncte):
            b.append(basisFunction(n, i, t))

            xBezier = basisFunction(n, i, t) * x[k] + xBezier
            yBezier = basisFunction(n, i, t) * y[k] + yBezier
            zBezier = basisFunction(n, i, t) * z[k] + zBezier
            i += 1

        ax.plot(xBezier[0][:frame + 1], yBezier[0][:frame + 1], zBezier[0][:frame + 1], c="blue")

    cells = 100
    nr_puncte = np.size(x, 0)
    n = nr_puncte - 1

    frames = cells  # Numărul de cadre este egal cu cells
    anim = animation.FuncAnimation(fig, update_frame, frames=frames, interval=200, repeat=False)

    # Salvare ca fișier video
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)
    anim.save('bezier_movie.mp4', writer=writer)

    plt.show()


def buton_movie_2d():
    movie_2d()
    messagebox.showinfo("Informare", "Movie-ul a fost creat in folderul curent!")


def buton_movie_3d():
    movie_3d()
    messagebox.showinfo("Informare", "Movie-ul a fost creat in folderul curent!")


def descriere_program():
    messagebox.showinfo("Descriere program",
                        "Acest program creeaza pe baza coordonatelor x,y,z ale punctelor introduse graficul 2D si 3D.")


def adaug_puncte():
    messagebox.showinfo("Cum adaug mai multe puncte?",
                        "Pentru a modifica numarul de puncte, modificati in cod pe linia 239  numarul dintre paranteze.")


def salvare_grafic_movie():
    messagebox.showinfo("Salvare grafic / Movie",
                        "Butonul ""Salvare grafic"" salveaza in format jpg ultimul grafic generat. Si movie-urile si jpg-urile sunt salvate in folderul programului.")


menu_bar = Menu(root)
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ajutor", menu=help_menu)
help_menu.add_command(label="Descriere program", command=descriere_program)
help_menu.add_command(label="Cum adaug mai multe puncte?", command=adaug_puncte)
help_menu.add_command(label="Salvare grafic / Movie", command=salvare_grafic_movie)

root.config(menu=menu_bar)

error_label = tk.Label(root, fg="red")
error_label.grid(row=5, column=0, columnspan=4)

plot3d_button = tk.Button(root, text="Grafic 3D", command=plot3d_bezier)
plot3d_button.grid(row=6, column=0, columnspan=2)

plot2d_button = tk.Button(root, text="Grafic 2D", command=plot2d_bezier)
plot2d_button.grid(row=6, column=2, columnspan=2)

citirefisier_buton = tk.Button(root, text="Citire date din fisier", command=citire_fisier)
citirefisier_buton.grid(row=7, column=0, columnspan=2)

generare_automata_button = tk.Button(root, text="Generare Automată Valori", command=generare_automata)
generare_automata_button.grid(row=7, column=2, columnspan=2)

resetare_button = tk.Button(root, text="Resetare valori", command=resetare_valori)
resetare_button.grid(row=8, column=0, columnspan=2)

movie_button = tk.Button(root, text="Creează film 2D", command=buton_movie_2d)
movie_button.grid(row=8, column=2, columnspan=2)

movie_button2 = tk.Button(root, text="Creează film 3D", command=buton_movie_3d)
movie_button2.grid(row=10, column=0, columnspan=2)

butons = tk.Button(root, text="Salvare Grafic", command=buton_save_grafic)
butons.grid(row=10, column=2, columnspan=2)

root.mainloop()