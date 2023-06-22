#Desafio tocar musica no python - MP3.

#Importamos a biblioteca do pygame.
import pygame

#Iniciar o pygame
pygame.mixer.init()

#Mixando uma música.
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()

#Deu erro no começo pois o curso é um pouco antigo então a solução para mixar múscas ficou obsoleta.
#Da linha 18 até o final peguei essa solução de um usuario do linkedin:
#https://www.linkedin.com/in/michael-cardoso-84a9a0b2?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BF23BT8GmQrKMhZdGGI7ruw%3D%3D

#Ultilizei esse while para verificação do canal de música ver se está em uso ou não.
while pygame.mixer.music.get_busy():
    continue

pygame.quit()