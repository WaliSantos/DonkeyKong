from tupy import BaseImage

class Fundo(BaseImage):
    '''
        Classe do Fundo do game DonkeyKong
    '''
    def __init__(self, x:int = 0, y:int = 0):
        '''
            Inicializa a instância da classe Fundo
        '''
        super().__init__("fundo.png", x, y)