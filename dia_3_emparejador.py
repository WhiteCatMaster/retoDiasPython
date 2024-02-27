import dia_2
def tinder(lista, fichero):
    fichero3 = open(fichero, "w")
    lista_sin_nombrar = lista
    lista_parejas = []
    for seguidor in  lista:
        if seguidor in lista_sin_nombrar:
            diccionario_parejas = {}
            diccionario_parejas["user1"] = seguidor
            lista_sin_nombrar.remove(seguidor)
            seguidor = dia_2.seguidor_aleatorio(1, lista_sin_nombrar)
            diccionario_parejas["user2"] = seguidor
            lista_sin_nombrar.remove(seguidor)
            lista_parejas.append(diccionario_parejas)
    for diccionario in lista_parejas:
        fichero3.write(f"{str((diccionario))}\n")
    fichero3.close()
