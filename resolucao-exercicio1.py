class Monitor:
  def __init__(self, maxima_x, maxima_y, atual_x, atual_y, volume = 0, ligado = False):
    self.maxima_x = maxima_x
    self.maxima_y = maxima_y
    self.atual_x = atual_x
    self.atual_y = atual_y
    self.volume = volume
    self.ligado = ligado

  def aumentaVolume(self):
    if self.ligado and self.volume < 100 :
      self.volume += 5

  def diminuiVolume(self):
    if self.ligado and self.volume > 0 :
      self.volume -= 5

  def liga(self):
    self.ligado = True

  def desliga(self):
    self.ligado = False

  def alteraResolucao(self, horizontal, vertical):
    if not self.ligado :
      return
    if horizontal > self.maxima_x or vertical > self.maxima_y :
      return
    self.atual_y = vertical
    self.atual_x = horizontal

monitor1 = Monitor(1920, 1080, 840, 600)

print(monitor1.ligado)

monitor1.liga()

print(monitor1.volume)
monitor1.aumentaVolume()
monitor1.aumentaVolume()
monitor1.aumentaVolume()
monitor1.diminuiVolume()
print(monitor1.volume)

print(monitor1.atual_x)
print(monitor1.atual_y)

monitor1.alteraResolucao(1280, 720)

print(monitor1.atual_x)
print(monitor1.atual_y)

