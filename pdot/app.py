import tkinter as tk

__version__ = "0.0.1"

class DrawPane(tk.Canvas):
    def __init__(self, master, relief=tk.RIDGE):
        super().__init__(master)
        self.config(width=320, height=320, bg="white")

        def callback(event):
            x = event.x // 10
            y = event.y // 10
            self.render_cell(x, y, "#ff0000")

        self.bind("<1>", callback)
        self.canvas = [[[255, 255, 255] for _ in range(32)] for _ in range(32)] 
        self.render()
        self.show_grid()

    def render(self):
        for x in range(32):
            for y in range(32):
                r, g, b = self.canvas[x][y]
                code = f"#{r:02x}{g:02x}{b:02x}"
                self.render_cell(x, y, code)

    def show_grid(self):
        for i in range(32):
            i *= 10
            self.create_line(i, 0, i, 320, fill="#cccccc")
            self.create_line(0, i, 320, i, fill="#cccccc")

    def render_cell(self, x, y, code):
        x *= 10
        y *= 10
        self.create_rectangle(x, y, x + 10, y + 10, fill=code, width=0)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.config(width=500, height=320)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        draw_pane = DrawPane(self)
        draw_pane.place(relx=0.36)

def new_app(title=f"pdot {__version__}"):
    root = tk.Tk()
    root.title(title)
    root.resizable(width=False, height=False)
    app = Application(master=root)
    return app
