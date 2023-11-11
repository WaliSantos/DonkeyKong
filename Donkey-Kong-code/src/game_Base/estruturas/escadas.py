
from game_Base.estruturas.estrutura import Estrutura

class Escada(Estrutura):
    '''
        Classe da estrutura escada
    '''
    _num_escadas = 0

    def __init__(self, x: float, y: float)-> None :
        '''
        Inicializa a instância da classe Escada
        '''
        super().__init__("Ladder.png", x, y)
        Escada._num_escadas += 1


