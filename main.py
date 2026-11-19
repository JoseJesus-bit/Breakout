# Para poder usar pyxel es necesario instalarlo en la terminal 
# se puede hacer aqui mismo en vs code con el comando "pip install pyxel" solo elimina las comillas 
# al dar enter debe de apapiprecer algo asi "Successfully installed pyxel-3.0.2"

#En caso de que aparezca el error "ModuleNotFoundError: No module named 'pip'" utilizar el comando "python -m ensurepip --upgrade"
import pyxel
import enum 
from ball import Ball
from paddle import Paddle
#F
class GameState(enum.Enum):
    READY = 0
    RUNNING = 1
    DROPPED = 2
    GAME_OVER = 3
    WIN = 4 
#F--
class App:
    def __init__(self):
        pyxel.init(384,300, display_scale=3, title="Breakout", fps=60)
        pyxel.load("assets/resources.pyxres")
        self.paddle = Paddle()
        self.ball = Ball()
        self.reset_ball()
        self.current_game_state = GameState.READY
        pyxel.run(self.update, self.draw)

    def reset_ball(self):
        self.ball.x = self.paddle.x + self.paddle.w / 2
        self.ball.y = self.paddle.y -self.ball.r
        self.ball.speedX = self.paddle.deflect_force(self.ball.x)
        self.ball.speedY = -2.5
        self.ball

    def update(self):
        self.paddle.update()
        if self.current_game_state == GameState.READY:
            self.ball.x = self.paddle.x + self.paddle.w / 2 + 10
        if self.current_game_state == GameState.RUNNING:
            self.ball.update()
            self.check_collision()
            if self.ball.out_of_bounds:
                self.current_game_state = GameState.DROPPED

    def check_collision(self):
        #bolita contra la barrita
        collision = self.ball.detect_collision(self.paddle, paddle=True)
        if collision:
            pass

    def draw(self):
        pyxel.cls(0)
        self.paddle.draw()
        self.ball.draw()

#f--
# Kickstart our app
App()