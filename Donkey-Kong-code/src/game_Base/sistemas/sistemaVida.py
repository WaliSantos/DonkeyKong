from tupy import BaseGroup, Image, Rectangle

class SistemaVida(BaseGroup):
    '''
        Classe do sistema de vida de alguma entidade. No jogo, apenas o mário a utiliza. 
    '''
    def __init__(self) -> None:
        '''
            incializa a instância da classe SistemaVida
        '''
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
        '''
            Método que permite reduzir uma vida da entidade que esteja utilizando o sistema vida
        '''
        coracao = self._objects[-1]
        self._remove(coracao)
        coracao._destroy()