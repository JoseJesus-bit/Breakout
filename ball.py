import pyxel


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedX = 2.0
        self.speedY = -1.5
        self.r = 2
        self.out_of_bounds = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.r, 7)

    def update(self):
        # mueve la bola,  y checa si rebota
        self.x += self.speedX
        self.y += self.speedY
        if self.x + self.r >= pyxel.width:
            self.speedX = self.speedX * -1
        elif self.y - self.r <= 0:
            self.speedY = self.speedY * -1
        elif self.x - self.r <= 0:
            self.speedX = self.speedX * -1
        elif self.y - self.r > pyxel.height:
            self.out_of_bounds = True