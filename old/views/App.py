import customtkinter as ctk

from .tab3DView import tab3dView
from .allGraphs import allGraphs

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self, colors):
        super().__init__()

        self.title("Plexsoft")
        self.geometry("900x600")
        self.configure(fg_color=colors["background"], padx=0, pady=0)

        # Tabview erstellen
        self.tabview = ctk.CTkTabview(self, corner_radius=10, fg_color=colors["background"], segmented_button_fg_color=colors["normal"])
        self.tabview.pack(padx=0, pady=0, fill="both", expand=True)

        # Tabs hinzufügen
        self.tab1 = self.tabview.add("Großansicht")
        self.tab2 = self.tabview.add("Gridansicht")
        self.tab3 = self.tabview.add("3D-Ansicht")

        tab3dView(self.tab3, colors)#
        # allGraphs(self.tab2)


