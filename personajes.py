class Enemigo:
    def __init__(self,nombre,vida,ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.vivo = True

    #Metodo Para perder vida
    def quitarVida(self,cantidad):
     if self.vivo == True:
        self.vida -= cantidad
        if self.vida <= 0:
            self.vivo = False
        
class Personaje:
    def __init__(self,nombre,ataque,vida,energia,curacion,costeCuracion):        
        self.nombre = nombre
        self.ataque = ataque
        self.vida = vida
        self.energia = energia
        self.curacion = curacion
        self.costeCuracion = costeCuracion
        self.vivo = True
        self.experiencia = 0
        self.nivel = 1
        self.oro = 50
        self.xpSiguienteNivel= 150

    #Metodo Para perder vida
    def quitarVida(self,cantidad):
     if self.vivo == True:
        self.vida -= cantidad
        if self.vida <= 0:
            self.vivo = False

    def Curar(self):
        self.vida += self.curacion
        self.energia -= self.costeCuracion

    def comprobarNivel(self):
        if self.experiencia >= self.xpSiguienteNivel:
            self.nivel += 1
            self.xpSiguienteNivel = 550
            self.vida   += int (1.5)
            self.ataque  += int(1.5)
            self.energia  += int(1.5)
            print("Has subido al nivel: " + str(self.nivel))
            print("Tu vida actual es: " + str(self.vida))
            print("Tu ataque actual es: " + str(self.ataque))
            print("Tu energia actual es: " + str(self.energia))
            
            


