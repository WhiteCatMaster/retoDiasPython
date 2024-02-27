import random

def seguidor_aleatorio(rango, lista_seguidores):
    for _ in range (0, rango) :
        seguidor_random = lista_seguidores[random.randint(0, len(lista_seguidores) - 1)]
        return seguidor_random
# si lees esto te daras cuenta que son 5 y no 7 lineas, ya que 
# tome la decision de ejecutar las cosas a parte una vez ya echo el programa
        
