from tkinter import *
from tkinter import ttk
import sys, os
from tkinter import filedialog
from youtube import *
from window_cover import * 

def resource_path0(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
 
 
def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )
 
    return os.path.join(base_path, relative_path)
 
def resource_path2(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)

def btn_clicked():
    downloader.descargarVideo(entry0.get())

def folder(): 
    YoutubeDownloder.path_actual = os.getcwd()
    YoutubeDownloder.folder_selected = filedialog.askdirectory()
    downloader.activador = True
    YoutubeDownloder.path_image = os.path.join(YoutubeDownloder.path_actual, "cover.png")
    os.chdir(YoutubeDownloder.folder_selected)

def cover():
    if downloader.activador:
        os.chdir(YoutubeDownloder.path_actual)
        cover_window(window)
    else:
        messagebox.showwarning("Advertencia","Seleccione primero un directorio.")

if __name__ == '__main__':
    window = Tk()
    window.title('Youtube Downloader')
    window.geometry("728x398")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 398,
        width = 728,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    path0 = resource_path2("img_textBox0.png")
    entry0_img = PhotoImage(file =path0)
    entry0_bg = canvas.create_image(
        572.0, 129.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry0.place(
        x = 478.0, y = 106,
        width = 188.0,
        height = 44)

    path1 = resource_path2("background.png")
    background_img = PhotoImage(file = path1)
    background = canvas.create_image(
        308.0, 199.0,
        image=background_img)

    path2 = resource_path2("img0.png")
    img0 = PhotoImage(file = path2)
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 485, y = 213,
        width = 178,
        height = 47)

    path3 = resource_path2("img1.png")
    img1 = PhotoImage(file = path3)
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = folder,
        relief = "flat")

    b1.place(
        x = 425, y = 339,
        width = 120,
        height = 43)

    path4 = resource_path2("img2.png")
    img2 = PhotoImage(file = path4)
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = cover,
        relief = "flat")

    b2.place(
        x = 583, y = 339,
        width = 128,
        height = 43)

    downloader = YoutubeDownloder(window)

    s = ttk.Style()
    s.theme_use("alt")
    s.configure("red.Horizontal.TProgressbar", foreground='white', background='#6BFC60',fieldbackground='white')

    window.resizable(False, False)
    window.mainloop()
