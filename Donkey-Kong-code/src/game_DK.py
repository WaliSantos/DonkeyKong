from tupy import *


from game_Base.fundo import Fundo
from game_Base.timer import Timer
from game_Base.estruturas.escadas import Escadas
from game_Base.estruturas.plataforma import Plataforma
from game_Base.estruturas.stackBarril import StackBarril
import time
import random
from random import randint
from random import choice
from game_Base.globais import Max_direita, Max_esquerda

Fundo()


escadas = [
    Escadas(254, 464),
    Escadas(254, 390),
    Escadas(254, 399),
    Escadas(457, 449),
    Escadas(457, 431),
    Escadas(457, 413),
    Escadas(162, 368),
    Escadas(162, 350),
    Escadas(162, 332),
    Escadas(290, 380),
    Escadas(290, 362),
    Escadas(290, 344),
    Escadas(290, 326),
    Escadas(290, 318),
    Escadas(226, 310),
    Escadas(226, 241),
    Escadas(226, 248),
    Escadas(336, 301),
    Escadas(336, 283),
    Escadas(336, 265),
    Escadas(336, 246),
    Escadas(464, 289),
    Escadas(464, 271),
    Escadas(464, 253),
    Escadas(162, 222),
    Escadas(162, 204),
    Escadas(162, 186),
    Escadas(240, 226),
    Escadas(240, 208),
    Escadas(240, 190),
    Escadas(240, 181),
    Escadas(418, 236),
    Escadas(418, 178),
    Escadas(464, 159),
    Escadas(464, 141),
    Escadas(464, 123),
    Escadas(380, 105),
    Escadas(380, 95),
    Escadas(380, 85),
]


# 10
platforms = [
    Plataforma(100, 480),
    Plataforma(132, 480),
    Plataforma(164, 480),
    Plataforma(196, 480),
    Plataforma(228, 480),
    Plataforma(260, 480),
    Plataforma(292, 480),
    Plataforma(324, 477),
    Plataforma(356, 474),
    Plataforma(388, 471),
    Plataforma(420, 468),
    Plataforma(452, 465),
    Plataforma(484, 462),
    Plataforma(516, 459),
    Plataforma(489, 416, True, True),
    Plataforma(457, 413, True, True),
    Plataforma(425, 410, True, True),
    Plataforma(393, 407),
    Plataforma(361, 404),
    Plataforma(329, 401),
    Plataforma(297, 398),
    Plataforma(265, 395, False, True),
    Plataforma(233, 392, False, True),
    Plataforma(201, 389),
    Plataforma(169, 386),
    Plataforma(137, 383),
    Plataforma(105, 380),
    Plataforma(137, 335, True, True),
    Plataforma(169, 332, True, True),
    Plataforma(201, 329),
    Plataforma(233, 326),
    Plataforma(265, 323, True, True),
    Plataforma(297, 320, True, True),
    Plataforma(329, 317),
    Plataforma(361, 314),
    Plataforma(393, 311),
    Plataforma(425, 308),
    Plataforma(457, 305),
    Plataforma(489, 302),
    Plataforma(521, 299),
    Plataforma(489, 257, True, True),
    Plataforma(457, 256, True, True),
    Plataforma(425, 254),
    Plataforma(393, 252),
    Plataforma(361, 250, True, True),
    Plataforma(329, 248, True, True),
    Plataforma(297, 246, True),
    Plataforma(265, 244),
    Plataforma(233, 242, False, True),
    Plataforma(201, 240, False, True),
    Plataforma(169, 238),
    Plataforma(137, 236),
    Plataforma(105, 234),
    Plataforma(137, 187, True, True),
    Plataforma(169, 186, True, True),
    Plataforma(201, 185, True),
    Plataforma(233, 184, True, True),
    Plataforma(265, 183, True, True),
    Plataforma(297, 182),
    Plataforma(329, 181),
    Plataforma(361, 180),
    Plataforma(393, 179, False, True),
    Plataforma(425, 178, False, True),
    Plataforma(457, 177),
    Plataforma(489, 176),
    Plataforma(521, 175),
    Plataforma(489, 124, True, True),
    Plataforma(457, 123, True, True),
    Plataforma(425, 122, True),
    Plataforma(393, 121),
    Plataforma(361, 120),
    Plataforma(329, 120),
    Plataforma(297, 120),
    Plataforma(265, 120),
    Plataforma(233, 120),
    Plataforma(201, 120),
    Plataforma(169, 120),
    Plataforma(137, 120),
    Plataforma(105, 120),
    Plataforma(380, 80),
    Plataforma(350, 80),
    Plataforma(320, 80),
]

StackBarril(110, 70)

############################## Entidades


class Entidades(BaseImage):
    def __init__(self, imagem, x: float, y: float, nome: str = "entidade"):
        super().__init__(imagem, x, y)
        self._nome = nome
        self._count = 0
        self._countX = 0
        self._countY = 0
        self._countJump = 0
        self._pulando = False

    def __str__(self):
        return f'A entidade é "{self._nome}" e está em x: {self._x} e y: {self._y}'

    def __repr__(self):
        return f'A entidade é "{self._nome}" e está em x: {self._x} e y: {self._y}'

    def movimentoX(self, animacaolist: list[str], velocidade: int = 3):
        self._file = animacaolist[self._countX]
        self._x += velocidade
        if not ((self._countX + 1) % len(animacaolist)):
            self._countX = 0
            return
        self._countX += 1

    def movimentoY_escada(self, animacaolist: list[str], velocidade: int = 2):
        self._file = animacaolist[self._countY]
        self._y -= velocidade
        if not ((self._countY + 1) % len(animacaolist)):
            self._countY = 0
            return
        self._countY += 1

    def pulo(self, animacaolist: list[str], velocidade: int = 2):
        self._file = animacaolist[self._countJump]
        self._y -= velocidade
        if not ((self._countJump + 1) % len(animacaolist)):
            self._countJump = 0
            return
        self._countJump += 1

    def colisao_com_escadas(self):
        for i in range(Escadas._num_escadas):
            if self._collides_with(escadas[i]):
                if self._x + 5 >= escadas[i]._x and self._x - 5 <= escadas[i]._x:
                    return True
        return False


class Mario(Entidades):
    animacoes_direita_list = [
        "Mario_Run2.png",
        "Mario_Run2.png",
        "Mario_Run3.png",
        "Mario_Run3.png",
        "Mario_Run1.png",
        "Mario_Run1.png",
    ]
    animacoes_esquerda_list = [
        "Mario_Run2esq.png",
        "Mario_Run2esq.png",
        "Mario_Run3esq.png",
        "Mario_Run3esq.png",
        "Mario_Run1esq.png",
        "Mario_Run1esq.png",
    ]
    animacoes_subindo_list = [
        "Mario_Climb.png",
        "Mario_Climb.png",
        "Mario_Climb2.png",
        "Mario_Climb2.png",
    ]
    animacoes_pulo_list = ["Mario_Jump.png"]
    animacoes_puloesq_list = ["Mario_Jumpesq.png"]
    animacoes_hammer_esq_list = [ 
        "Mario_destroy_left.png","Mario_Run2esq.png"
                                 ]
    animacoes_hammer_dir_list = ["Mario_destroy.png","Mario_Run2.png"]

    def __init__(self) -> None:
        super().__init__("Mario_Run1.png", 100, 458, "Mario")
        self._direita = True
        self._atacando = False
        self._vivo = True
        self._vida = 300
        self._win = False
        self._suspiro = 0
        self._colidiu_com_martelo = False
        self._temporizador = None
        self.timer = Timer(3)
        self.filesEsq = Mario.animacoes_hammer_esq_list
        self.filesDir = Mario.animacoes_hammer_dir_list


    def colisao_com_plataformas(self) -> bool:
        for i in range(Plataforma._num_plataformas):
            if self._collides_with(platforms[i]):
                if (
                    self._file == "Mario_Climb.png" or self._file == "Mario_Climb2.png"
                ) and platforms[i]._transparente_mario:
                    return False
                if self._y + 14 < platforms[i]._y:
                    self._y = platforms[i]._posterior
                    return True
        if self.colisao_com_escadas() and (
            self._file == "Mario_Climb.png" or self._file == "Mario_Climb2.png"
        ):
            return False
        self._y += 4
        return False
    
    def colisao_com_barril(self) ->bool:
       for barrel in barril:
            if barrel._collides_with(self) and (
                self._file == "Mario_destroy.png" or
                self._file == "Mario_destroy_left.png"):
                    barril.remove(barrel)
                    barrel.destroy()
                    time.sleep(1)
                    return True
            elif barrel._collides_with(self):
                return True
    
    def win(self) -> None:
        if  self._y <= 60:
            self._win = True
            
    def colisao_com_hammer(self):
        for i in hammers:
            if self._collides_with(i):
                hammers.remove(i)
                i.destroy()
                return True
        return False
    
    def update(self) -> None:
        self.colisao_com_barril()
        self.colisao_com_plataformas()
        self.colisao_com_hammer()
        self.win()

        if self._vivo and not self.win():
            if keyboard.is_key_just_down("space") and self.colisao_com_plataformas() and not self._colidiu_com_martelo:
                self._pulando = True
            if self._pulando:
                if self._direita:
                    self.pulo(Mario.animacoes_pulo_list, 9)
                else:
                    self.pulo(Mario.animacoes_puloesq_list, 9)
                self._count += 1
                if self._count == 6:
                    self._pulando = False
                    self._count = 0
                    
            if keyboard.is_key_down("Left"):
                if self._x <= Max_esquerda:
                    self.movimentoX(Mario.animacoes_esquerda_list, 0)
                else:
                    self.movimentoX(Mario.animacoes_esquerda_list, -3)
                self._direita = False
            if keyboard.is_key_down("Right"):
                if self._x >= Max_direita:
                    self.movimentoX(Mario.animacoes_direita_list, 0)
                else:
                    self.movimentoX(Mario.animacoes_direita_list)
                self._direita = True
            if keyboard.is_key_down("Up") and not self._pulando:
                if self.colisao_com_escadas():
                    self.movimentoY_escada(Mario.animacoes_subindo_list)
            if keyboard.is_key_down("Down") and not self._pulando:
                if self.colisao_com_escadas():
                    self.movimentoY_escada(Mario.animacoes_subindo_list, -2)
            if (
                keyboard.is_key_up("Up")
                and keyboard.is_key_up("Down")
                and keyboard.is_key_up("Right")
                and keyboard.is_key_up("Left")
                and not self._pulando
            ):
                if self._file == "Mario_Climb.png" or self._file == "Mario_Climb2.png":
                    self._file = "Mario_Climb.png"
                elif self._direita:
                    self._file = "Mario_Run1.png"
                else:
                    self._file = "Mario_Run1esq.png"
                    
            if self.colisao_com_hammer():
                self._colidiu_com_martelo = True
                self._atacando = True
                self._temporizador = time.time() + 9
            
            if self._colidiu_com_martelo:
                if self._temporizador and time.time() < self._temporizador:
                    self.timer.update()
                    if self._direita:
                        self._file = self.filesDir[self.timer.ticks % len(self.filesDir)]
                    else:    
                        self._file = self.filesEsq[self.timer.ticks % len(self.filesEsq)]
                else:
                    self._colidiu_com_martelo = False
                
            if self._atacando:
                if self.colisao_com_barril():      
                    Barril._num_barril += -1

            self._suspiro +=1
            
            if self._vivo and self._suspiro == 12:
                if self.colisao_com_barril():
                    self._vida += -100
                    
                    time.sleep(1)

                    for i in barril:
                        i.destroy()
                    barril.clear()
                    Barril._num_barril = 0
                    
                    for j in hammers:
                        j.destroy()
                    hammers.clear()
                
                    hammer1 = Hammer(425, 360)
                    hammer2 = Hammer(137, 147)

                    hammers.append(hammer1)
                    hammers.append(hammer2)
                    
                    self._colidiu_com_martelo = False
                    self._x, self._y, self._direita = 100, 458, True

                    if self._vida >= 0:
                        sistema.perde_vida()
                    if self._vida == 0:
                        self._file = "dead.png"
                        self._vivo = False
                        Label("You Loser", 500, 200, 'Arial 80', anchor = 'center', color = "Green")
                self._suspiro = 0
            elif self._vivo == False:
                self._file = "dead.png"
    
        if self._win: 
            Label("You Win", 500, 200, 'Arial 80', anchor='center', color="Green")
            Image('full-heart.png', 350, 50)
            pauline._file, pauline._x = "pauline-still.png", 310
            mario._file, mario._x, mario._y = "Mario_Run1esq.png", 385, 60
            for i in barril:
                i.destroy()
            barril.clear()
            
    @property
    def x(self) -> str:
        return f"{self._x}"

    @x.setter
    def x(self, int: int):
        print(
            f"Preguiçoso... toma seu {int} de volta. Nada de teletransportes por aqui"
        )

    @property
    def y(self) -> str:
        return f"{self._y}"

    @y.setter
    def y(self, int: int):
        print(
            f"Preguiçoso... toma seu {int} de volta. Nada de teletransportes por aqui"
        )

class DonkeyKong(Entidades):
    animacoes_esquerda_direita_list = [
        "dkForward.png",
        "dkLeft.png",
        "dkForward.png",
        "dkRight.png",
    ]
    animacoes_subindo_list = (["dkClimbEmpty1.png", "dkClimbEmpty2.png"],)
    animacao_length = len(animacoes_esquerda_direita_list)

    def __init__(
        self,intervalo: int,
        ):
        super().__init__("dkForward.png", 190, 65, "DonkeyKong")
        self.wait = 0
        self.count = 0

    def update(self) -> None:
        self._file = "dkForward.png"
        if not mario._win and mario._vivo:
            if not self.wait:
                    self._file = DonkeyKong.animacoes_esquerda_direita_list[(self.count // 7)]
                    self.count += 1
                    if self.count // DonkeyKong.animacao_length == 7:
                        barril.append(Barril())
                        self.count = 0
                        self.wait = random.randint(50, 100)
            else:
                    self.wait += -1

class Hammer(Entidades):
    def __init__ (self, x, y) -> None:
       super().__init__ ("hammer.png", x, y, "Hammer")
       self._x = x
       self._y = y
       self._file = "hammer.png"
       
    
class Pauline(Entidades):
    animacoes_pauline = [
        "pauline-still.png",
        "pauline-help.png"

    ]
    def __init__(self) -> None:
        super().__init__("pauline-still.png", 350, 45, "Pauline")
        self.timer = Timer(10)
        self.files = Pauline.animacoes_pauline
        
    def update(self) -> None:
        self.timer.update()
        self._file = self.files[self.timer.ticks % len(self.files)]
            

class Barril(Entidades):
    animacoes_run = ["barrel1.png", "barrel2.png", "barrel3.png", "barrel4.png"]
    animacoes_escada = ["barrel-down.png"]
    _num_barril = 0

    def __init__(self) -> None:
        super().__init__("barrel1.png", 250, 102, "Barril")
        self._movimenta_para = 5
        self._x_da_escada = 999
        self._count = 0
        self._decisao_de_descida = random.randint(0, 1)
        Barril._num_barril += 1

    def colisao_com_escadas(self):
        for i in range(Escadas._num_escadas):
            if self._collides_with(escadas[i]):
                self._x_da_escada = escadas[i]._x
                self.movimentoY_escada(Barril.animacoes_escada, 0)
                return True
        self._x_da_escada = 999
        return False

    def colisao_com_plataformas(self) -> bool:
        for i in range(Plataforma._num_plataformas):
            if self._collides_with(platforms[i]):
                if (self._y + 11 < platforms[i]._y) and not platforms[
                    i
                ]._transparente_barril:
                    self._y = platforms[i]._posterior + 5
                    return True
        if self.colisao_com_escadas():
            if (
                self._x > self._x_da_escada - 2 and self._x < self._x_da_escada + 2
            ) and self._decisao_de_descida:
                self._movimenta_para = random.choice([-5, 5])
                self._y += 6
                return False
            return True
        for i in range(Plataforma._num_plataformas):
            if self._collides_with(platforms[i]) and platforms[i]._transparente_barril:
                return True
        self._y += 6
        return False

    def update(self) -> None:
        if not (self._count % 50):
            self._decisao_de_descida = random.randint(0, 1)
        if self._x >= 530:
            self._movimenta_para = -5
        if self._x <= 90:
            self._movimenta_para = 5
        if self._x <= 532 and self._x >= 88 and self.colisao_com_plataformas():
            self.movimentoX(Barril.animacoes_run, self._movimenta_para)
        self._count += 1
        
        for barrel in barril:
            if barrel._x >= 110 and barrel._y >= 463:
                    barril.remove(barrel)
                    barrel.destroy()
                    Barril._num_barril -= 1

class SistemaVida(BaseGroup):
    def __init__(self) -> None:
        super().__init__(0, 0)
        _rectangle = Rectangle(600, 100, 140, 50, fill = 'black', outline = 'pink')
        _label_vida1 = Image('full-heart.png', 630, 125) 
        _label_vida2 = Image('full-heart.png', 670, 125) 
        _label_vida3 = Image('full-heart.png',710, 125) 
        self._add(_rectangle)
        self._add(_label_vida1)
        self._add(_label_vida2)
        self._add(_label_vida3)
    
    def perde_vida(self) -> None:
        coracao = self._objects[-1]
        self._remove(coracao)
        coracao._destroy()
    

sistema = SistemaVida()
pauline = Pauline()
barril = []
donkeyKong = DonkeyKong(25)
mario = Mario()
hammers = []
hammer1 = Hammer(425, 360)
hammer2 = Hammer(137, 147)

hammers.append(hammer1)
hammers.append(hammer2)

ponto = Entidades(
    "ponto.png", 100, platforms[0]._y - 1, "a"
)  # PARTE DE CIMA DA PLATAFORMA
ponto = Entidades("ponto2.png", mario._x, mario._y, "a")  # PÉ DO MARIO
print(f"pé do mário: {mario._y + 14}")
print(f"plataforma: {platforms[0]._y - 1}")
run(globals())