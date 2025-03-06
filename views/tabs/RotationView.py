# import customtkinter as ctk
# import tkinter as tk
# import vtk
# from vtkmodules.vtkRenderingCore import vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor, vtkActor, vtkPolyDataMapper
# from vtkmodules.vtkIOGeometry import vtkSTLReader
# from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
# from vtkmodules.vtkRenderingOpenGL2 import vtkOpenGLRenderWindow


# class RotationView:
#     def __init__(self, tab:ctk.CTkFrame, app:ctk.CTk):
#         self.tab = tab
#         self.app = app

#         self.vtk_frame = tk.Frame(tab, width=800, height=600, background=self.app.color_config["background"])
#         self.vtk_frame.pack(fill=tk.BOTH, expand=True, pady=(20,0))
#         self.tab.after(100, self.init_vtk)


#     def init_vtk(self):
#         # Renderer und Render Window erstellen
#         self.renderer = vtkRenderer()
#         self.renderWindow = vtkOpenGLRenderWindow()
#         self.renderWindow.AddRenderer(self.renderer)

#         # Interactor für das Render Window
#         self.renderWindowInteractor = vtkRenderWindowInteractor()
#         self.renderWindowInteractor.SetRenderWindow(self.renderWindow)

#         # STL-Datei laden
#         reader = vtkSTLReader()
#         reader.SetFileName("assets/canmodel.stl")

#         # Mapper und Actor erstellen
#         self.mapper = vtkPolyDataMapper()
#         self.mapper.SetInputConnection(reader.GetOutputPort())

#         self.actor = vtkActor()
#         self.actor.SetMapper(self.mapper)
#         self.actor.GetProperty().SetColor(1,0,0)

#         # Berechnung des Mittelpunkts des Modells
#         self.center = self.calculate_center(reader)

#         # Setze den Mittelpunkt des Modells als Ursprung für die Rotation
#         self.actor.SetOrigin(self.center)

#         # Renderer konfigurieren
#         self.renderer.AddActor(self.actor)

    
#         self.renderer.SetBackground(0.01,0.01,0.1)  # Blau: RGB(0, 0, 1)

#         # Interaktionsstil setzen
#         style = vtkInteractorStyleTrackballCamera()
#         self.renderWindowInteractor.SetInteractorStyle(style)

#         # VTK Render Window mit tkinter verbinden
#         self.vtk_frame.update_idletasks()
#         win_id = self.vtk_frame.winfo_id()
#         self.renderWindow.SetWindowInfo(str(win_id))

#         # Rendern starten
#         self.renderWindow.Render()
#         self.renderWindowInteractor.Initialize()

#         # Start Rotation
#         self.rotate_model()

#     def calculate_center(self, reader):
#         # Berechne den Mittelpunkt des Modells
#         reader.Update()  # Stelle sicher, dass das Modell geladen ist
#         bounds = reader.GetOutput().GetBounds()
#         # Berechne den Mittelpunkt
#         center = [(bounds[0] + bounds[1]) / 2,
#                   (bounds[2] + bounds[3]) / 2,
#                   (bounds[4] + bounds[5]) / 2]
#         return center

#     def rotate_model(self):
#         # Modell um 1° um die Y-Achse drehen
#         self.actor.RotateY(1)
#         self.renderWindow.Render()
#         # Alle 20ms erneut rotieren
#         self.tab.after(20, self.rotate_model)