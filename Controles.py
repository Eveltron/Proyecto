
from random import randint
def combate(j,e):
    print("***Ha empezado el combate ****")
    #Presentacion del primer enemigo
    print("Ha aparecido un " + e.nombre)
    
    while j.vivo == True and e.vivo == True:
    #Inicio de combate/ Info de los personajes
        print("*********")
        print("Tu vida es de:"  + str(j.vida))
        print("Tu energia actual es de :" + str(j.energia))
        print("Vida del enemigo:" + str(e.vida))

        #Jugabilidad
        respuesta=""
        respuesta= input("¿ Que deberiamos hacer? a-Atacar ("+str(j.ataque)+")/ c-Curar(coste="+str(j.costeCuracion)+"),(cantidad="+str(j.curacion)+"):")

        if respuesta == "a":
            print("!Has decidido atacar¡")
            e.quitarVida(j.ataque)
            if e.vivo == False:
                break
            
        elif respuesta == "c" and j.energia >= j.costeCuracion and j.vida <100:
            print("!Has decidido Curarte¡")
            j.Curar()

        print("El " + e.nombre + " te hace un daño de " + str(e.ataque) + " Puntos de vida ")
        j.quitarVida(e.ataque)
        
    print("Has derrotado al: " + e.nombre + " Felicidades puedes continuar avanzando ")
   
print("************")
def recompensa (Personaje):
    #recompensas posibles: Recuperar energia, Recuperar vida, aumento del ataque maximo
    print("Recibes algo de xp por este combate")
    Personaje.experiencia += 100
    print("recibes algo de oro")
    Personaje.oro += 50
    print("Tu enemigo ha dejado caer un botin")
    p = randint(1, 4)
    if p == 1:
        print("Te has regenerado 25 puntos de vida")
        Personaje.vida += 25
    elif p == 2:
        print("Has regenerado 25 puntos de energia")
        Personaje.energia += 25
    elif p == 3:
        print("Has conseguido un anillo de fortificacion menor +5 en ataque")
        Personaje.ataque += 5
    elif p == 4:
        print("Has conseguido oro adicional")
        Personaje.oro += 50
    







     
    




