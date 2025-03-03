import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Funktion zum Erstellen von Plots
def create_plot(title: str, data_x, data_y):
    fig, ax = plt.subplots(figsize=(6, 4.5))  # Plotgröße angepasst
    ax.plot(data_x, data_y)
    ax.set_title(title)
    ax.set_xlabel("Zeit")
    ax.set_ylabel("Wert")

    # Hintergrundfarbe der Grafik auf Rot setzen
    fig.patch.set_facecolor('red')

    return fig

# Funktion zum Hinzufügen der Diagramme in den Tab
def allGraphs(tab: ctk.CTkFrame):
    # Testdaten für jedes Diagramm
    time = np.linspace(0, 10, 100)  # Beispielzeitreihe
    humidity = np.random.rand(100) * 100
    temperature = np.random.rand(100) * 30
    oxygen = np.random.rand(100) * 21
    particulate_matter = np.random.rand(100) * 100
    pressure = np.random.rand(100) * 1000
    speed = np.random.rand(100) * 20
    nox = np.random.rand(100) * 50

    # Layout für die GridView
    labels = ["Luftfeuchtigkeit", "Temperatur", "Sauerstoff", "Feinstaub", "Luftdruck", "Geschwindigkeit", "Stickoxide"]
    data = [humidity, temperature, oxygen, particulate_matter, pressure, speed, nox]

    # Canvas und Scrollbar für den Tab hinzufügen
    canvas_frame = ctk.CTkFrame(tab)
    canvas_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    canvas = ctk.CTkCanvas(canvas_frame, bg="red")  # Hintergrundfarbe des Canvas auf Rot setzen
    canvas.grid(row=0, column=0, sticky="nsew")

    # Scrollbar hinzufügen, falls der Inhalt größer ist als der sichtbare Bereich
    scrollbar = ctk.CTkScrollbar(canvas_frame, orientation="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Inneres Frame für die Plots, das skaliert wird
    plot_frame = ctk.CTkFrame(canvas, fg_color="red")
    canvas.create_window((0, 0), window=plot_frame, anchor="nw")

    # 7 Plots in einer GridView anordnen
    for i, label in enumerate(labels):
        row = i // 3  # Bestimmt die Zeile
        col = i % 3   # Bestimmt die Spalte
        fig = create_plot(label, time, data[i])

        # Matplotlib Plot in Tkinter integrieren
        canvas_plot = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas_plot.get_tk_widget().grid(row=row, column=col, sticky="nsew", padx=10, pady=10)
        canvas_plot.draw()

    # Update der Größe des Inneren Frames, um das Scrollen zu aktivieren
    plot_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Dynamisches Skalieren für Canvas
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(0, weight=1)
    canvas_frame.grid_rowconfigure(0, weight=1)
    canvas_frame.grid_columnconfigure(0, weight=1)
    plot_frame.grid_rowconfigure(0, weight=1)
    plot_frame.grid_columnconfigure(0, weight=1)

    # Mausrad Scrollen aktivieren
    def on_mouse_wheel(event):
        if event.delta > 0:
            canvas.yview_scroll(-1, "units")  # Nach oben scrollen
        else:
            canvas.yview_scroll(1, "units")  # Nach unten scrollen

    # Eventbindung für das Mausrad-Scrolling
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)
