from tupy import *


from game_Base.fundo import Fundo
from game_Base.timer import Timer
from game_Base.estruturas.escadas import Escadas
from game_Base.estruturas.plataforma import Plataforma
from game_Base.estruturas.stackBarril import StackBarril

from game_Base.globais import Max_direita,Max_esquerda


Fundo()


escadas = [
    Escadas(254, 464),
    Escadas(254, 390),
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
    Escadas(380, 85)
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
    Plataforma(489, 416, True),
    Plataforma(457, 413, True),
    Plataforma(425, 410, True),
    Plataforma(393, 407),
    Plataforma(361, 404),
    Plataforma(329, 401),
    Plataforma(297, 398),
    Plataforma(265, 395),
    Plataforma(233, 392),
    Plataforma(201, 389),
    Plataforma(169, 386),
    Plataforma(137, 383),
    Plataforma(105, 380),
    Plataforma(137, 335, True),
    Plataforma(169, 332, True),
    Plataforma(201, 329),
    Plataforma(233, 326),
    Plataforma(265, 323, True),
    Plataforma(297, 320, True),
    Plataforma(329, 317),
    Plataforma(361, 314),
    Plataforma(393, 311),
    Plataforma(425, 308),
    Plataforma(457, 305),
    Plataforma(489, 302),
    Plataforma(521, 299),
    Plataforma(489, 257, True),
    Plataforma(457, 256, True),
    Plataforma(425, 254),
    Plataforma(393, 252),
    Plataforma(361, 250, True),
    Plataforma(329, 248, True),
    Plataforma(297, 246, True),
    Plataforma(265, 244),
    Plataforma(233, 242),
    Plataforma(201, 240),
    Plataforma(169, 238),
    Plataforma(137, 236),
    Plataforma(105, 234),
    Plataforma(137, 187, True),
    Plataforma(169, 186, True),
    Plataforma(201, 185, True),
    Plataforma(233, 184, True),
    Plataforma(265, 183, True),
    Plataforma(297, 182),
    Plataforma(329, 181),
    Plataforma(361, 180),
    Plataforma(393, 179),
    Plataforma(425, 178),
    Plataforma(457, 177),
    Plataforma(489, 176),
    Plataforma(521, 175),
    Plataforma(489, 124, True),
    Plataforma(457, 123, True),
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

StackBarril(110,70)

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

    def colisao_com_plataformas(self) -> bool:
        for i in range(Plataforma._num_plataformas):
            if self._collides_with(platforms[i]):
                if (
                    self._file == "Mario_Climb.png" or self._file == "Mario_Climb2.png"
                ) and platforms[i]._transparente:
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

    def colisao_com_escadas(self):
        for i in range(Escadas._num_escadas):
            if self._collides_with(escadas[i]):
                return True
        return False



class Mario(Entidades):
    def __init__(
        self,
        animacoes_direita_list: list[str],
        animacoes_esquerda_list: list[str],
        animacoes_subindo_list: list[str],
        animacoes_pulo_list: list[str],
        animacoes_puloesq_list: list[str],
    ):
        super().__init__("Mario_Run1.png", 100, 458, "Mario")
        self.animacoes_direita_list = animacoes_direita_list
        self.animacoes_esquerda_list = animacoes_esquerda_list
        self.animacoes_subindo_list = animacoes_subindo_list
        self.animacoes_pulo_list = animacoes_pulo_list
        self.animacoes_puloesq_list = animacoes_puloesq_list
        self._direita = True

    def update(self):
        self.colisao_com_plataformas()
        if keyboard.is_key_just_down("space") and self.colisao_com_plataformas():
            self._pulando = True
        if self._pulando:
            if self._direita:
                self.pulo(self.animacoes_pulo_list, 8)
            else:
                self.pulo(self.animacoes_puloesq_list, 8)
            self._count += 1
            if self._count == 6:
                self._pulando = False
                self._count = 0
        if keyboard.is_key_down("Left"):
            if self._x <= Max_esquerda:
                self.movimentoX(self.animacoes_esquerda_list, 0)
            else:
                self.movimentoX(self.animacoes_esquerda_list, -3)
            self._direita = False
        if keyboard.is_key_down("Right"):
            if self._x >= Max_direita:
                self.movimentoX(self.animacoes_direita_list, 0)
            else:
                self.movimentoX(self.animacoes_direita_list)
            self._direita = True
        if keyboard.is_key_down("Up"):
            if self.colisao_com_escadas():
                self.movimentoY_escada(self.animacoes_subindo_list)
        if keyboard.is_key_down("Down"):
            if self.colisao_com_escadas():
                self.movimentoY_escada(self.animacoes_subindo_list, -2)
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

    @property
    def x(self):
        return f"{self._x}"

    @x.setter
    def x(self, int: int):
        print(
            f"Preguiçoso... toma seu {int} de volta. Nada de teletransportes por aqui"
        )

    @property
    def y(self):
        return f"{self._y}"

    @y.setter
    def y(self, int: int):
        print(
            f"Preguiçoso... toma seu {int} de volta. Nada de teletransportes por aqui"
        )


class DonkeyKong(Entidades):
    def __init__(
        self,
        animacoes_esquerda_direita_list: list[str],
        animacoes_subindo_list: list[str], intervalo: int
    ):
        super().__init__("dkForward.png", 190, 65, "DonkeyKong")
        self.animacoes_esquerda_direita_list = animacoes_esquerda_direita_list
        self.animacoes_subindo_list = animacoes_subindo_list
        self.timer = Timer(intervalo)
        
        self.penult_tick= False
        self.count= -1
        
        # self.list_countAux_barril = [
        #                 "dkForward.png",    
        #                 "dkLeft.png",
        #                 "dkForward.png",
        #                 "dkRight.png"
        #                 ]
        # self.countAux_barril = ""
       
    def update(self):
        self.timer.update()
        self._file = self.animacoes_esquerda_direita_list[self.timer.ticks % len(self.animacoes_esquerda_direita_list)]

        if self.timer.ticked:
            self.count+= 1
            # if self.count == len(self.animacoes_esquerda_direita_list)+1:
            #     self.count = 0
            # print(self.count)
            # self.countAux_barril = self.list_countAux_barril[self.count]

        if self.count == len(self.animacoes_esquerda_direita_list) :
            self.penult_tick = True
            if self.penult_tick : 
                barril = Barril(["barrel1.png",
                                "barrel2.png",
                                "barrel3.png",
                                "barrel4.png"])
                self.penult_tick = False
            
            self.count= 0
################################ objetos dinamicos:

class ObjDinamico(BaseImage):
    def __init__(self, imagem, x: float, y: float, nome: str = "ObjetoDinamico"):
        super().__init__(imagem, x, y)
        # self._nome = nome
        # self._count = 0
        self._countX = 0
        self._countY = 0
        # self._countJump = 0
        # self._pulando = False

    def __str__(self):
        return f'O objeto é "{self._nome}" e está em x: {self._x} e y: {self._y}'

    def __repr__(self):
        return f'O objeto é "{self._nome}" e está em x: {self._x} e y: {self._y}'

    def movimentoX(self, animacaolist: list[str], velocidade: int = 3):
        self._file = animacaolist[self._countX]
        self._x += velocidade
        if not ((self._countX + 1) % len(animacaolist)):
            self._countX = 0
            return
        self._countX += 1

    def movimentoY(self, animacaolist: list[str], velocidade: int = 2):
        self._file = animacaolist[self._countY]
        self._y -= velocidade
        if not ((self._countY + 1) % len(animacaolist)):
            self._countY = 0
            return
        self._countY += 1

class Barril(ObjDinamico):
    def __init__(self, animacoes_run: list[str]):
        super().__init__("barrel1.png",  250,100 , "Barril")
        self.caindo = False
        self.verificar_escada = False
        self.animacoes_run = animacoes_run

    def update(self):
        if self._x <700:
            self.movimentoX(self.animacoes_run, 3)

        


        

donkeyKong = DonkeyKong(
    [
        "dkForward.png",    
        "dkLeft.png",
        "dkForward.png",
        "dkRight.png"
        ],
    [
        "dkClimbEmpty1.png",
        "dkClimbEmpty2.png"],
     25
)    


mario = Mario(
    [
        "Mario_Run2.png",
        "Mario_Run2.png",
        "Mario_Run3.png",
        "Mario_Run3.png",
        "Mario_Run1.png",
        "Mario_Run1.png",
    ],
    [
        "Mario_Run2esq.png",
        "Mario_Run2esq.png",
        "Mario_Run3esq.png",
        "Mario_Run3esq.png",
        "Mario_Run1esq.png",
        "Mario_Run1esq.png",
    ],
    ["Mario_Climb.png", "Mario_Climb.png", "Mario_Climb2.png", "Mario_Climb2.png"],
    ["Mario_Jump.png"],
    ["Mario_Jumpesq.png"],
)
ponto = Entidades(
    "ponto.png", 100, platforms[0]._y - 1, "a"
)  # PARTE DE CIMA DA PLATAFORMA
ponto = Entidades("ponto2.png", 100, mario._y + 14, "a")  # PÉ DO MARIO
print(f"pé do mário: {mario._y + 14}")
print(f"plataforma: {platforms[0]._y - 1}")
run(globals())