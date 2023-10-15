
from game_Base.estruturas.estrutura import Estruturas

class Escadas(Estruturas):
    _num_escadas = 0

    def __init__(self, x: float, y: float):
        super().__init__("Ladder.png", x, y)
        Escadas._num_escadas += 1


