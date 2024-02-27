import requests
from bs4 import BeautifulSoup
from pygame import mixer
from gtts import gTTS
file = "index.html"

def voice(txt, nombre):
    tts = gTTS(txt)
    tts.save(f'{nombre}.mp3')
    mixer.init()
    mixer.music.load('output.mp3')
    mixer.music.play()

def write_web(texto):
    r = requests.get(texto)
    soup = BeautifulSoup(r.text, 'lxml')
    use_file = open(file, "w")
    for line in str(soup):
        use_file.write(line)
    print(soup.title)
    use_file.close()

def search(fichero, el_impu):
    files = open(fichero, "r")
    cosa_buscada = el_impu
    for cosa in files:
        if cosa_buscada in cosa:
            print(cosa)

def main(carga, texto, name):
    if carga == 1:
        write_web(texto)
        search(file, name)
    else:
        voice(texto, name)

if __name__ == "__main__":
    main(1, "https://www.youtube.com/", "bottom")