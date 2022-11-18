# Importing library
# need intall Pillow
import qrcode
import unicodedata
from pytube import Playlist, YouTube
import re
import os


def removerAcentosECaracteresEspeciais(palavra):
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)


def gera_qrs(link):
    urls = []

    #Verifica se existe a pasta
    if os.path.isdir("QR"):
        pass
    else:
        #Se nao existe, cria
        os.mkdir("QR")

    if 'list=' in link:
        urls = Playlist(link)
        img = qrcode.make(link)
        img.save('playlist.png')
    else:
        urls.append(link)

    for i in urls:  # Salva separadamente cada link
        limpo = removerAcentosECaracteresEspeciais(YouTube(i).title)
        img = qrcode.make(i)
        img.save('.\\QR\\' + limpo + '.png')
        print('QR criado: ' + limpo)



