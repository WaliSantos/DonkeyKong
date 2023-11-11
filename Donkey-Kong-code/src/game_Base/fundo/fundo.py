from tupy import BaseImage

class Fundo(BaseImage):
    '''
        Classe do Fundo do game DonkeyKong
    '''
    def __init__(self, x=0, y=0):
        '''
            Inicializa a instância da classe Fundo
        '''
        super().__init__("fundo.png", x, y)

        
