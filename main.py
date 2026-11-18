# Para poder usar pyxel es necesario instalarlo en la terminal 
# se puede hacer aqui mismo en vs code con el comando "pip install pyxel" solo elimina las comillas 
# al dar enter debe de aparecer algo asi "Successfully installed pyxel-3.0.2"

#En caso de que aparezca el error "ModuleNotFoundError: No module named 'pip'" utilizar el comando "python -m ensurepip --upgrade"
import pyxel
from ball import Ball
from paddle import Paddle

class App:
    def __init__(self):
        pyxel.init(384,300, display_scale=3, title="Breakout", fps=60)
        pyxel.load("assets/resources.pyxres")
        self.paddle = Paddle()
        self.ball = Ball(100, 100)
        pyxel.run(self.update, self.draw)


    def update(self):
        self.ball.update()

    def draw(self):
        pyxel.cls(0)
        self.paddle.draw()
        self.ball.draw()


# Kickstart our app
App()