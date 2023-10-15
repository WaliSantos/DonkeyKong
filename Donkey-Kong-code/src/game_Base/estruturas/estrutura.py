from tupy import BaseImage


class Estruturas(BaseImage):
    def __init__(self, imagem: str, x: int, y: int):
        super().__init__(imagem, x, y)
        self._imagem = imagem
        self._x = x
        self._y = y

    def __str__(self):
        # return f"Imagem: {self._imagem}, x: {self._x}, y: {self._y}"
        return f"{self._x}, {self._y}"

    def __repr__(self):
        # return f"Imagem: {self._imagem}, x: {self._x}, y: {self._y}"
        return f"{self._x}, {self._y}"



