class Timer:
   '''
      Classe Timer para controlar o tempo 
   '''
   def __init__(self, interval: int)->None:
      '''
         Inicializa a instância da classe Timer
      '''
      self.interval = interval
      self.counter = 0

   def update(self)-> None:
      self.counter += 1
   @property
   def ticked(self)-> bool:
      return self.counter % self.interval == 0

   @property
   def ticks(self)-> int:
      return self.counter // self.interval

        
