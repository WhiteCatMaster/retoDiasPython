import random
import os
from pygame import mixer
from gtts import gTTS

seguidores = ["mxuspldu", "adua_viles", "elcolumpiooficial",
             "joel_serebin", "_maxiivc", "michaell_morraz",
             "popmillpye", "lorrain_1", "moha.gmt_15",
             "david.siqueiros.56884", "filip_samuel14",
             "herr_oktopus", "davidponce1522", "buty0606",
             "jonnierdev", "ferrodriguxz", "spillwayallay",
             "cesarsanchez", "er.en_data", "danielmendoza847",
             "andres.jimenez.3705157", "eduarholguin", 
             "sr.kitsune_", "nickoloko456", "joshu_alop",]

class Jugador :
    def __init__(self, nombre, puntos, lista):
        self.nombre = nombre
        self.puntos = puntos
        self.contactos = contactar(self.nombre, lista)

def crear_mover_fichero():
    if "ficherosseguidores" not in os.listdir():
        directorio = os.mkdir("ficherosseguidores")
    os.chdir("ficherosseguidores")

def almacenar_datos(lista, fichero):
    fichero_write = open(fichero, "w")
    dict_jugador = {}
    for usuario in lista:
        jugador = Jugador(usuario, random.randint(0,100), lista)
        # asi nos aseguramos que no haya numeros deorbitados
        dict_jugador[f"{jugador.nombre}"] = int(jugador.puntos)
        fichero_write.write(f"{jugador.nombre}, con {jugador.puntos} puntos y de contactos a {jugador.contactos} \n")
    return(dict_jugador)
    fichero_write.close()

def contactar(nombre, lista):
    lista_contactos = []
    numero_contactos = random.randint(0, 5)
    for contacto_nuevo in range(0,numero_contactos):
        numero_jugadores = len(lista) - 1
        jugador_aleatorio = random.randint(0, numero_jugadores)
        if lista[jugador_aleatorio] != nombre:
            lista_contactos.append(lista[jugador_aleatorio])
    return lista_contactos

def donar_puntos(de_quien, a_quien, diccionario):
    puntos = int(input("cuantos puntos?: "))
    diccionario[de_quien] -= puntos
    diccionario[a_quien] += puntos

def seguidor_aleatorio(rango, lista_seguidores):
    for _ in range (0, rango) :
        seguidor_random = lista_seguidores[random.randint(0, len(lista_seguidores) - 1)]
        return seguidor_random

def voice(txt, nombre):
    tts = gTTS(txt)
    tts.save(f'{nombre}.mp3')
    mixer.init()
    mixer.music.load('output.mp3')
    mixer.music.play()

if __name__ == "__main__":
    crear_mover_fichero()
    almacen = almacenar_datos(seguidores, "puntos.csv")
    quieres_donar = "si"
    while quieres_donar == "si":
        quieres_donar = input("quieres que se donen puntos?")
        if quieres_donar == "si":
            de_quien = input("de quien? ")
            a_quien = input("a quien? ")
            print(donar_puntos(de_quien, a_quien, almacen, ))
            voice()
    mostrar_ganador = input("quieres mostrar el ganador?: ")
    if mostrar_ganador == "si":
        ganador = seguidor_aleatorio(1, seguidores)
        print(ganador)
        voice(f"congratulaciones por ganar {ganador}", ganador)
    print("operaciones terminadas")