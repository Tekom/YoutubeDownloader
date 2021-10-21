import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import requests
import json
import os


client_id = 'db349b155880460ca7c9dda829271539'
client_secret = 'abe52e2a3a6049149127e977678edbbe'

def get_album_name(artista, cancion, path):
    os.chdir(path)
    artistas = []
    artistas_cancion = ""
    artist = cancion + " " + artista
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret))
    result = sp.search(artist)
    #pprint.pprint(result)
    id_album = result['tracks']['items'][0]['album']['id']
    nombre_cancion = sp.search(q='artist:' + artista + ' track:' + cancion, type='track')
    #pprint.pprint(result['tracks']['items'][-1])
    r = requests.get("https://open.spotify.com/oembed?url=spotify:album:{}".format(id_album))
    res = json.loads(r.text)

    for i in range(len(result['tracks']['items'][0]['artists'])):
        artistas.append(result['tracks']['items'][0]['artists'][i]['name'])
        
        if i != len(result['tracks']['items'][0]['artists']) - 1:
            artistas.append(", ")

    for i in range(len(artistas)):
        artistas_cancion = artistas_cancion + artistas[i]

    nombre = result['tracks']['items'][-1]['name']
       
    album = result['tracks']['items'][0]['album']['name']

    imagen = res['thumbnail_url']
    codigo_imagen = requests.get(imagen)
    file = open("cover.png", 'wb')
    file.write(codigo_imagen.content)

    #print(nombre, artistas_cancion, album)

    return(nombre,artistas_cancion,album)


 
    

#get_album_name('bad bunny', 'cancion con yandel')





















