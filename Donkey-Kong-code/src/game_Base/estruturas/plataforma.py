from game_Base.estruturas.estrutura import Estrutura
from game_Base.variaveis.globais import mario_em_pe_na_plataforma


class Plataforma(Estrutura):
    '''
        Classe da estrutura Plataforma
    '''
    _num_plataformas = 0

    def __init__(
        self,
        x: int,
        y: int,
        transparência_mario: bool = False,
        transparência_barril: bool = False,
    )-> None:
        '''
        Inicializa a instância da classe Plataforma
        '''
        super().__init__("Platform.png", x, y)
        Plataforma._num_plataformas += 1
        self._posterior = y - mario_em_pe_na_plataforma  # Região em que o Mario fica em pé na plataforma
        self._transparente_mario = transparência_mario
        self._transparente_barril = transparência_barril
