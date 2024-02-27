from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("ha ocurrido problemita")
    print("videito pa ti hermano")

def Download_pa_retrasaos(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_lowest_resolution()
    try:
        youtubeObject.download()
    except:
        print("ha ocurrido problemita")
    print("videito pa ti hermano")

def inputs(lista):   
    pasa = "no"
    while pasa == "no":
        link = input("metale aqui el video hermano (si acabaste dale al enter): ")
        if link == "":
            pasa = "si"
        elif link == "rola":
            lista.append("https://youtu.be/NDX4u3Z38WY?si=rX-Ub03OPAkflmzr")
        elif link == "secreto":
            lista.append("https://youtu.be/dQw4w9WgXcQ?si=9GflmSAovsLFEb2B")
        else:
            lista.append(link)

def ejecutar():
    lista_espera = []  
    inputs(lista_espera)
    for link in lista_espera:
        Download(link)
    print("fin del trayo, gracias loquito")

ejecutar()
