import random

#libreria echga sopbretodo para los contactos y puntos 

seguidores = ["mxuspldu", "adua_viles", "elcolumpiooficial",
             "joel_serebin", "_maxiivc", "michaell_morraz",
             "popmillpye", "lorrain_1", "moha.gmt_15",
             "david.siqueiros.56884", "filip_samuel14",
             "herr_oktopus", "davidponce1522", "buty0606",
             "jonnierdev", "ferrodriguxz", "spillwayallay",
             "cesarsanchez", "er.en_data", "danielmendoza847",
             "andres.jimenez.3705157", "eduarholguin", 
             "sr.kitsune_", "nickoloko456", "joshu_alop",]

# esta es la lista de los primeros seguidores, seguire añadiendo

class Jugador :
    def __init__(self, nombre, puntos, lista):
        self.nombre = nombre
        self.puntos = puntos
        self.contactos = contactar(self.nombre, lista)
        #ni sabia que podia meter funciones como definiciones en clases

#clase para definir a las propiedades de cada usuario
        
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

#con esta funcion guaradamos todos los datos, tanto en el nuevo fichero
#como en el diccionario que hace el return( menos contactos)
    

def contactar(nombre, lista):
    lista_contactos = []
    numero_contactos = random.randint(0, 5)
    for contacto_nuevo in range(0,numero_contactos):
        numero_jugadores = len(lista) - 1
        jugador_aleatorio = random.randint(0, numero_jugadores)
        if lista[jugador_aleatorio] != nombre:
            lista_contactos.append(lista[jugador_aleatorio])
    return lista_contactos

#funcion echa no solo para tener los contactos aleatorios sino para que el numero de estos tb lo sea

def donar_puntos(de_quien, a_quien, diccionario):
    puntos = int(input("cuantos puntos?: "))
    diccionario[de_quien] -= puntos
    diccionario[a_quien] += puntos

#funcion echa para pasar puntos de un jugador a otro

if __name__ == "__main__":
    almacen = almacenar_datos(seguidores, "puntos.csv")
    quieres_donar = "si"
    while quieres_donar == "si":
        quieres_donar = input("quieres que se donen puntos?")
        if quieres_donar == "si":
            de_quien = input("de quien? ")
            a_quien = input("a quien? ")
            print(donar_puntos(de_quien, a_quien, almacen, ))
    print("operaciones terminadas")




