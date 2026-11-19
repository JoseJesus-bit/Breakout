import pyxel
from math import copysign, ceil

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
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

#frijolito
    def detect_collision(self, obj , paddle = False): #Funcion de las coliciones de la barrita
        #Calcular el numero de coliciones que hay entre la bola y la barrita
        num_steps = ceil(max(abs(self.speedX), abs(self.speedY)))
        if num_steps == 0:
            return False # la bolita no se mueve

        #Calcular el incremento de la bola en cada paso
        step_size = 1.0 / num_steps

        #Verificar las coliciones de la bola con la barrita
        for step in range(1, num_steps + 1):
            t = step * step_size   #interpolacion entre el paso actual y el siguiente
            sub_ball_x = self.x + t * self.speedX
            sub_ball_y = self.y + t * self.speedY

            #verificar si la bola esta dentro de los limites del objeto
            if(
                sub_ball_x + self.r >= obj.x
                and sub_ball_x - self.r <= obj.x + obj.w
                and sub_ball_y + self.r >= obj.y
                and sub_ball_y - self.r <= obj.y + obj.h
            ):
                #si pelota choca con la barrita, refleja la bolita
                if paddle:
                    self.speedX =  obj.deflect_force(self.x)
                    self.speedY = self.speedY * -1
                return True
        return False #No hubo colicion
