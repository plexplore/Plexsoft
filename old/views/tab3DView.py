import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def update_plot(ax, x, y, z, temperatur, luftfeuchtigkeit, sauerstoffgehalt, feinstaub, show_temp, show_humidity, show_oxygen, show_pm, canvas):
    # Löscht die aktuellen Punkte im Plot
    ax.cla()

    ax.plot(x, y, z, color='cyan', linewidth=2, label="Flugbahn")

    if show_temp:
        ax.scatter(x, y, z + 0.1, c=temperatur, cmap='Greens', vmin=min(temperatur), vmax=max(temperatur), label="Temperatur", marker='o')

    if show_humidity:
        ax.scatter(x, y, z + 0.2, c=luftfeuchtigkeit, cmap='Blues', vmin=min(luftfeuchtigkeit), vmax=max(luftfeuchtigkeit), label="Luftfeuchtigkeit", marker='^')

    if show_oxygen:
        ax.scatter(x, y, z + 0.3, c=sauerstoffgehalt, cmap='Reds', vmin=min(sauerstoffgehalt), vmax=max(sauerstoffgehalt), label="Sauerstoffgehalt", marker='s')

    if show_pm:
        ax.scatter(x, y, z + 0.4, c=feinstaub, cmap='YlOrBr', vmin=min(feinstaub), vmax=max(feinstaub), label="Feinstaub", marker='D')

    ax.set_zlabel("Höhe (km)")
    ax.legend()

    # Achsenfarbe anpassen
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.zaxis.label.set_color('white')
    ax.title.set_color('white')
    ax.tick_params(colors='white')

    # X- und Y-Achsen ausblenden
    ax.set_xticks([])  # Keine X-Achsen-Markierungen
    ax.set_yticks([])  # Keine Y-Achsen-Markierungen

    # Canvas für den Plot erstellen
    canvas.draw()  # Canvas nach Plot-Aktualisierung neu zeichnen
    return ax

def tab3dView(tab: ctk.CTkFrame, colors:dict):
    fig = plt.Figure(figsize=(6, 6), dpi=100, facecolor=colors["background"])
    ax = fig.add_subplot(111, projection='3d', facecolor=colors["background"])
    
    # Simulierte Flugbahn-Daten
    t = np.linspace(0, 10, 100)
    x = np.sin(t)
    y = np.cos(t)
    z = 1 - t / 10
    
    # Messwerte
    temperatur = np.linspace(20, -50, 100)
    luftfeuchtigkeit = np.linspace(50, 10, 100)
    sauerstoffgehalt = np.linspace(21, 10, 100)
    feinstaub = np.linspace(30, 5, 100)

    # Sidebar mit Checkboxes
    sidebar = ctk.CTkFrame(tab, corner_radius=10)  # Sidebar breiter gemacht
    sidebar.pack(anchor="nw", side="right",  padx=20, pady=20)  # Padding hinzugefügt, damit der Abstand zur Seite vergrößert wird

    # Status der Checkboxen (True oder False)
    show_temp = ctk.BooleanVar(value=True)
    show_humidity = ctk.BooleanVar(value=True)
    show_oxygen = ctk.BooleanVar(value=True)
    show_pm = ctk.BooleanVar(value=True)

    # Erstellen der Checkboxen und deren Funktionen
    show_temp_cb = ctk.CTkCheckBox(sidebar, text="Temperatur", variable=show_temp, command=lambda: update_plot(ax, x, y, z, temperatur, luftfeuchtigkeit, sauerstoffgehalt, feinstaub, show_temp.get(), show_humidity.get(), show_oxygen.get(), show_pm.get(), canvas))
    show_temp_cb.pack(anchor="w", padx=10, pady=10)  # Padding für Abstand zwischen Checkboxen

    show_humidity_cb = ctk.CTkCheckBox(sidebar, text="Luftfeuchtigkeit", variable=show_humidity, command=lambda: update_plot(ax, x, y, z, temperatur, luftfeuchtigkeit, sauerstoffgehalt, feinstaub, show_temp.get(), show_humidity.get(), show_oxygen.get(), show_pm.get(), canvas))
    show_humidity_cb.pack(anchor="w", padx=10, pady=10)

    show_oxygen_cb = ctk.CTkCheckBox(sidebar, text="Sauerstoffgehalt", variable=show_oxygen, command=lambda: update_plot(ax, x, y, z, temperatur, luftfeuchtigkeit, sauerstoffgehalt, feinstaub, show_temp.get(), show_humidity.get(), show_oxygen.get(), show_pm.get(), canvas))
    show_oxygen_cb.pack(anchor="w", padx=10, pady=10)

    show_pm_cb = ctk.CTkCheckBox(sidebar, text="Feinstaub", variable=show_pm, command=lambda: update_plot(ax, x, y, z, temperatur, luftfeuchtigkeit, sauerstoffgehalt, feinstaub, show_temp.get(), show_humidity.get(), show_oxygen.get(), show_pm.get(), canvas))
    show_pm_cb.pack(anchor="w", padx=10, pady=10)

    # Initialen Plot erstellen
    canvas = FigureCanvasTkAgg(fig, master=tab)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    update_plot(ax, x, y, z, temperatur, luftfeuchtigkeit, sauerstoffgehalt, feinstaub, show_temp.get(), show_humidity.get(), show_oxygen.get(), show_pm.get(), canvas)
