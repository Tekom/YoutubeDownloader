import youtube_dl
from tkinter import *
from tkinter import ttk
import eyed3
import subprocess
from PIL import ImageTk, Image
from mutagen.id3 import ID3, APIC, error
import os
from prueba import get_album_name
from tkinter import filedialog
from tkinter import messagebox
from tkinter.font import Font


class YoutubeDownloder():
    def __init__(self, window):
        self.ventana = window
        self.path_actual = os.getcwd()
        self.activador = False

        self.progress_bar = ttk.Progressbar(self.ventana, style='red.Horizontal.TProgressbar',orient="horizontal", length=230, mode='determinate')
        self.progress_bar.place(x=455,y=185)

        self.porcentaje_valor = Label(self.ventana,text='',background='white', foreground='gray')
        self.porcentaje_valor.place(x=550,y=158)

        self.mp3_state = True
        self.mp4_state = False

        self.folder_selected = ''
        self.path_actual = ''

    @classmethod
    def obtenerDatosCaratula(cls, artista, cancion):
        cls.datos = get_album_name(artista, cancion, cls.path_actual)
        os.chdir(cls.folder_selected)


    def descargarVideo(self,link):
        self.link = f'{link}'

        if self.mp3_state and not self.mp4_state:
            ydl_opts = {
                        'progress_hooks': [self.my_hook],
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                                            'key': 'FFmpegExtractAudio',
                                            'preferredcodec': 'webm',
                                            'preferredquality': '192',
                                        }]
                    }

        elif self.mp4_state and not self.mp3_state.get:
             ydl_opts = {
                        'progress_hooks': [self.my_hook],
                    }

        elif self.mp4_state.get() and self.mp3_state:
            print('Error, tiene las dos opciones seleccionadas.')

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    self.info = ydl.extract_info(self.link, download=False)
                    ydl.download([self.link])
        except Exception as e:
            print(e)

    @classmethod
    def agregarCover(cls, audio, name):
        audiofile = eyed3.load(audio)

        if not audiofile.tag:
          audiofile.initTag()


        audiofile.tag.images.set(eyed3.id3.frames.ImageFrame.FRONT_COVER, open(cls.path_image,'rb').read(), 'image/jpeg')
        audiofile.tag.artist = u"{}".format(cls.datos[1])
        audiofile.tag.album = u"{}".format(cls.datos[2])
        audiofile.tag.title = u"{}".format(cls.datos[0])

        audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

        try:
            os.remove(os.path.join(cls.folder_selected, name))
        except:
            pass
        
        os.rename(audio, cls.datos[0] + '.mp3')

    def my_hook(self, d):
        if d['status'] == 'downloading':
           self.estado_descarga = Label(self.ventana,text='Descargando...',background='white',font=('Probeta Light',12), foreground='gray')
           self.estado_descarga.place(x=455,y=158)
           porcentaje = float(d['_percent_str'].replace('%',""))
           self.progress_bar['value'] = porcentaje
           self.porcentaje_valor.config(text=str(porcentaje) + '%')
           self.ventana.update()


        if d['status'] == 'finished':
            self.estado_descarga.config(text='Convirtiendo...')
            filename=d['filename']
            total_porcentaje = float(d['_total_bytes_str'].replace('MiB','')) * 1000
            name = filename[0:5]

            if '.' in name or ' ' in name:
                name = name.replace(' ','-')
                name = name.replace('.','')
                name = name + '.webm'
            else:
                name = filename[0:5] + '.webm'

            name_output = filename.replace('.webm','')
            name_output = name_output.replace("'",'')
            name_output = name_output.replace(' ','-')
            print(name_output)
            os.rename(filename, name)

            cmd = f'ffmpeg -i {name} -acodec mp3 {name_output}.mp3'

            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
            for line in process.stdout:
                if 'kB' in line:
                    try:
                        conv = int(line.split()[1].replace('kB',''))
                        valor = (100*conv)/total_porcentaje
                        print(conv, valor)
                        self.progress_bar['value'] = valor
                        self.porcentaje_valor.config(text="{0:.1f}".format(valor) + '%')
                        self.ventana.update()
                    except:
                        pass
                else:
                    pass

            self.progress_bar['value'] = 100
            self.porcentaje_valor.config(text="100" + '%')
            self.ventana.update()


            self.agregarCover(name_output + '.mp3', name)

#if __name__ == '__main__':
    #downloader.ventana.mainloop()

