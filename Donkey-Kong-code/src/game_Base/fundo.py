from tupy import BaseImage

class Fundo(BaseImage):
    def __init__(self, x=0, y=0):
        super().__init__("fundo.png", x, y)

        
