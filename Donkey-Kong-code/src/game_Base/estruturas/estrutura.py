from tupy import BaseImage


class Estrutura(BaseImage):
    '''
        Classe base para estruturas do jogo.
        Esta classe representa estruturas genéricas que podem existir no jogo.
    '''
    def __init__(self, imagem: str, x: int, y: int)-> None:
        '''
        Inicializa a instância da classe Estruturas
        '''
        super().__init__(imagem, x, y)
        self._imagem = imagem
        self._x = x
        self._y = y

    def __str__(self)->str:
        # return f"Imagem: {self._imagem}, x: {self._x}, y: {self._y}"
        return f"{self._x}, {self._y}"

    def __repr__(self)->str:
        # return f"Imagem: {self._imagem}, x: {self._x}, y: {self._y}"
        return f"{self._x}, {self._y}"



