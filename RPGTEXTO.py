#archivos importados
from personajes import Enemigo, Personaje, OrcoGuerrero, OrcoArquero, OrcoGladeador
from Controles import combate, recompensa
from random import randint

#Propiedades del Jugador
jugador = Personaje("", 15, 100, 100, 10, 30)
#propiedades del enemigo sala 10


#inicio de Juego
print("Bienvenido a la Isla de los orcos...")
jugador.nombre = input("Como te llamas jugador: " )
print("!Encantado de conocerte! " + jugador.nombre)

#Enemigos pimera etapa
nivel1 = [OrcoGuerrero(randint(0,2)), OrcoArquero(randint(0,2)),OrcoGuerrero(randint(0,2)),OrcoGladeador(randint(0,2))]

for Enemigo in nivel1 :
    combate(jugador, Enemigo)
    recompensa(jugador)
    jugador.comprobarNivel()

print("Has conseguido Avanzar de sala enorabuena")

















