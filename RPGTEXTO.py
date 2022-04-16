#archivos importados
from personajes import Enemigo, Personaje
from Controles import combate, recompensa
from random import randint

#Propiedades del Jugador
jugador = Personaje("", 15, 100, 100, 10, 30)
#propiedades del enemigo sala 10
OrcoGuerrero = Enemigo ("Orco Guerrero", 60, 5)
OrcoArquero = Enemigo ("Orco Arquero", 40, 8)
OrcoGladeador = Enemigo("Orco Gladeador", 60, 8)

#inicio de Juego
print("Bienvenido a la Isla de los orcos...")
jugador.nombre = input("Como te llamas jugador: " )
print("!Encantado de conocerte! " + jugador.nombre)

#Enemigos pimera etapa
nivel1 = [OrcoGuerrero,OrcoArquero,OrcoGladeador]

for Enemigo in nivel1 :
    combate(jugador, Enemigo)
    recompensa(jugador)
    jugador.comprobarNivel()

print("Has conseguido Avanzar de sala ")

 #prueba de git
















