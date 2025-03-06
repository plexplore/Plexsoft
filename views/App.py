import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import pandas as pd

from  views.tabs.ViewOne import ViewOne
from views.tabs.View3D import View3D
from views.tabs.ViewAll import ViewAll
# from views.tabs.RotationView import RotationView

class App(ctk.CTk):
    def __init__(self, data_config:dict, color_config:dict):
        super().__init__()
        self.data_config = data_config
        self.color_config = color_config
        self.data = None
        self.recording= False

        self.title("Plexsoft")
        self.geometry("1100x800")
        self.minsize(1100,450)
        self.iconbitmap("assets/logo.ico")
        self.configure(fg_color=color_config["background"])

        self.tabview = ctk.CTkTabview(self, fg_color="transparent")
        self.tabview.place(relwidth=1, relheight=1)

        self.tab_one = ViewOne(self.tabview.add("Einzelansicht"), self)
        self.tab_all = ViewAll(self.tabview.add("Mehrfachansicht"), self)
        self.tab_3d = View3D(self.tabview.add("3D-Ansicht"), self)
        # self.tab_rot = RotationView(self.tabview.add("Rotationsansicht"), self)


        self.open_button = ctk.CTkButton(self, text="Öffnen", width=20, command=self.open_csv)
        self.open_button.pack(pady=10, padx=(13,10), anchor="nw", side="left")

        self.save_button = ctk.CTkButton(self, text="Speichern", width=20, command=self.save_csv)
        self.save_button.pack(pady=10, padx=0, anchor="nw", side="left")

        self.record_button = ctk.CTkButton(self, text="Aufnehmen", width=150, command=self.record)
        self.record_button.pack(pady=10, padx=5, anchor="nw", side="left")

        logo = ctk.CTkImage(dark_image=Image.open("assets/logo.png"),
                                  light_image=Image.open("assets/logo.png"),
                                  size=(50,50))
        self.logo = ctk.CTkLabel(self, image=logo, text="")
        self.logo.pack(pady=10, padx=20, anchor="ne")

        

    def open_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Dateien", "*.csv")])
        data = None
        try:
            data = pd.read_csv(path, sep=";", header=0)
            print(data)
        except:
            messagebox.showerror("Fehler", "Die Datei konnte nicht geöffnet werden")
            return
        
        if set([d["name"] for d in self.data_config]) - set(data.columns):
            print(set([d["name"] for d in self.data_config]) - set(data.columns))
            messagebox.showerror("Fehler", "Die zu landende Datei enthält nicht alle benötigten Spalten")
            return

        self.data = data
        self.update_data()

    def save_csv(self):
        if self.data is None:
            messagebox.showerror("Fehler", "Es gibt keine Daten zum speichern")
            return

        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Dateien", "*.csv")])
        self.data.to_csv(path, sep=";")
        print("hier2")

    def record(self):
        if self.recording:
            self.recording = False
            self.record_button.configure(text="Aufnehmen")
        else:
            self.record_button.configure(text="Aufnahme stoppen")
            self.recording = True
            self.get_data()

    def get_data(self):
        print("hier")
        if self.recording: self.after(100, self.get_data)


    def update_data(self):
        self.tab_one.update_data()
        self.tab_all.update_data()
        self.tab_3d.update_data()