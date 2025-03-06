import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def on_resize(event):
    print(f"Fenstergröße geändert: {event.width}x{event.height}")


class ViewOne:
    def __init__(self, tab: ctk.CTkTabview, app: ctk.CTk):
        self.app = app
        self.graph_canvas = None
        self.tab = tab

        self.graph_frame = ctk.CTkFrame(self.tab, fg_color="transparent")
        self.graph_frame.pack(side="left", padx=0, pady=(10,0), fill="both", expand=True)
        self.side_bar = ctk.CTkFrame(self.tab, fg_color=self.app.color_config["light_background"], width=150)
        self.side_bar.pack( side="right", fill="y", padx=(10,0), pady=(30,0))

        x_values = [d["name"] for d in app.data_config if d["x"]==True]

        self.cb_label = ctk.CTkLabel(self.graph_frame, text="X-Achse", text_color="white")
        self.cb_label.pack(anchor="nw", padx=5, pady=(0,0))
        self.combo_box = ctk.CTkComboBox(self.graph_frame, command=self.plot, values=x_values)
        self.combo_box.pack(anchor="nw", padx=5, pady=(0,0))
        self.graph = ctk.CTkFrame(self.graph_frame, fg_color="transparent")
        self.graph.pack(padx=0, pady=(10,0), fill="both", expand=True)

        self.x_slides = {}
        for y_name in [d["name"] for d in app.data_config if d["y"]==True]:
            self.x_slides[y_name] = ctk.CTkSwitch(self.side_bar, fg_color="purple", text=y_name, variable=ctk.BooleanVar(value=True), command=self.plot)

            self.x_slides[y_name].pack(anchor="nw", padx=5, pady=5)


    def update_data(self):
        self.plot()


    def plot(self, choice=None):
        if self.app.data is None:
            return

        # #x = self.app.data.columns[0]
        # x = self.combo_box.get()
        # y = self.combo_box.get()

        fig, ax = plt.subplots()
        fig.set_facecolor(self.app.color_config["background"])
        ax.set_facecolor(self.app.color_config["background"])
        ax.tick_params(axis='both', colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white') 
        for spine in ax.spines.values(): spine.set_color("white")

        
        ax.tick_params(axis='both', colors='white')

        for col_name in [d["name"] for d in self.app.data_config if d["y"]==True and d["name"]!=self.combo_box.get() and self.x_slides[d["name"]].get()]:
            ax.plot(self.app.data[self.combo_box.get()], self.app.data[col_name] /self.app.data[col_name].max(), label=col_name)

        ax.legend()
        

        if self.graph_canvas:
            self.graph_canvas.get_tk_widget().destroy()
        self.graph_canvas = FigureCanvasTkAgg(fig, master=self.graph)
        self.graph_canvas.get_tk_widget().config(bg=self.app.color_config["background"])
        self.graph_canvas.get_tk_widget().pack(fill="both", expand=True)
        self.graph_canvas.draw()
        
        