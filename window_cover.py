from tkinter import *
from youtube import * 
from tkinter.font import Font
from PIL import ImageTk, Image

def resource_path2(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
 
    return os.path.join(base_path, relative_path)

def cerrar_info():
    window_cover.destroy()

def buscar():
    artista = entry0.get()
    cancion = entry1.get()

    YoutubeDownloder.obtenerDatosCaratula(artista, cancion)

    im = Image.open(YoutubeDownloder.path_image)
    im = im.resize((100,100), Image.ANTIALIAS)
    ph = ImageTk.PhotoImage(im)
    label = Label(canvas, image=ph)
    label.image=ph 
    label.place(x=460,y=5) 

    song,artists,album = YoutubeDownloder.datos

    if 'remix' in cancion.lower():
        pass
    else:
        song = song.replace('-','')
        song = song.replace('Remix','')


    cancion_name.config(text='Artista: {}'.format(artists))
    artista_nombres.config(text='Cancion: {}'.format(song))
    album_name.config(text='Album: {}'.format(album))
 
def cover_window(window):
    global window_cover, entry0, entry1, canvas, cancion_name,artista_nombres,album_name
    window_cover = Toplevel(window)
    window_cover.title('Album Art')
    window_cover.geometry("622x211")
    window_cover.configure(bg = "#ffffff")
    canvas = Canvas(
        window_cover,
        bg = "#ffffff",
        height = 211,
        width = 622,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    path5 = resource_path2("im0g_textBox0.png")
    entry0_img = PhotoImage(file = path5)
    entry0_bg = canvas.create_image(
        369.0, 139.0,
        image = entry0_img)

    entry0 = Entry(window_cover,
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry0.place(
        x = 306.0, y = 129,
        width = 126.0,
        height = 18)

    path6 = resource_path2("im1g_textBox.png")
    entry1_img = PhotoImage(file = path6)
    entry1_bg = canvas.create_image(
        369.0, 58.0,
        image = entry1_img)

    entry1 = Entry(window_cover,
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry1.place(
        x = 306.0, y = 48,
        width = 126.0,
        height = 18)

    path7 = resource_path2("im0.png")
    img0 = PhotoImage(file = path7)
    b0 = Button(window_cover,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = buscar,
        relief = "flat")

    b0.place(
        x = 294, y = 171,
        width = 110,
        height = 31)

    path8 = resource_path2("im1.png")
    img1 = PhotoImage(file = path8)
    b1 = Button(window_cover,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = cerrar_info,
        relief = "flat")

    b1.place(
        x = 490, y = 173,
        width = 110,
        height = 33)

    path9 = resource_path2("background2.png")
    background_img = PhotoImage(file = path9)
    background = canvas.create_image(
        187.0, 105.5,
        image=background_img)

    cancion_name = Label(canvas,text='',background='white',font=('Probeta Light',12))
    artista_nombres = Label(canvas,text='',background='white',font=('Probeta Light',12))
    album_name = Label(canvas,text='',background='white',font=('Probeta Light',12))

    cancion_name.place(x=460,y=110)
    artista_nombres.place(x=460,y=130)
    album_name.place(x=460,y=150)

    #window.resizable(False, False)
    window.mainloop()
