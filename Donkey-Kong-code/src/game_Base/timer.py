class Timer:
   def __init__(self, interval):
      self.interval = interval
      self.counter = 0

   def update(self):
      self.counter += 1

   @property
   def ticked(self):
      return self.counter % self.interval == 0

   @property
   def ticks(self):
      return self.counter // self.interval