from SpritesClass import Sprite
from JogadorClass import Jogador

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Tela:
    def __init__(self,j,t0):
        self.telas = ["jogo","game over"] #telas existentes
        self.estagio = "jogo"
        self.j = j

        #sprites
        self.v0 = Sprite(40,40,30,30,t0)
        self.v1 = Sprite(40,80,30,30,t0)
        self.v2 = Sprite(40,120,30,30,t0)
        self.sprites = [self.v0,self.v1,self.v2]


    def getEstagio(self):
        return self.estagio

    def setEstagio(self,temp):
        if temp in self.telas:
            self.estagio=temp
        else:
            print("Tela não existe, erro de digitação no código")

    def getSprites(self):
        return self.sprites

    def atualizarSprites(self):
        if self.j.getVidas() == 2:
            self.sprites.remove(self.v2)
        if self.j.getVidas() == 1:
            self.sprites.remove(self.v1)
        if self.j.getVidas() == 0:
            self.sprites.remove(self.v0)