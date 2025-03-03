import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)  # Erste Funktion
y2 = np.exp(x / 3)  # Zweite Funktion mit größerer Skalierung
y3 = np.log(x + 1)  # Dritte Funktion mit kleiner Skalierung

fig, ax1 = plt.subplots()

# Erste y-Achse
ax1.plot(x, y1, 'g-', label="sin(x)")
ax1.set_ylabel("sin(x)", color="g")

# Zweite y-Achse
ax2 = ax1.twinx()
ax2.plot(x, y2, 'b-', label="exp(x/3)")
ax2.set_ylabel("exp(x/3)", color="b")

# Dritte y-Achse
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("outward", 60))  # Abstand zur zweiten Achse
ax3.plot(x, y3, 'r-', label="log(x+1)")
ax3.set_ylabel("log(x+1)", color="r")

# Achsenfarben anpassen für bessere Sichtbarkeit
ax1.tick_params(axis='y', colors='g')
ax2.tick_params(axis='y', colors='b')
ax3.tick_params(axis='y', colors='r')

plt.show()
