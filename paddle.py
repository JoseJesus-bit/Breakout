import pyxel

class Paddle:
    def __init__(self):
        self.w = 48
        self.h = 8 
        self.x = pyxel.width / 2 - self.w / 2
        self.y = pyxel.height - 50
        self.mid_sections = 4   
        self.sprite_img = 0        
        self.sprite_w = 8  
        self.sprite_end_U = 8
        self.sprite_end_V = 0
        self.sprite_mid_U = 0
        self.sprite_mid_V = 8

    def draw(self):
        # Lado izquierdo de la paleta
        pyxel.blt(
            self.x,
            self.y,
            self.sprite_img,
            self.sprite_end_U,
            self.sprite_end_V,
            self.sprite_w,
            self.sprite_w
        )
        
        # Secciones del centro de la paleta
        for i in range(0, self.mid_sections):
            pyxel.blt(
                self.x + self.sprite_w + (self.sprite_w * i),
                self.y,
                self.sprite_img,
                self.sprite_mid_U,
                self.sprite_mid_V,
                self.sprite_w,
                self.sprite_w
            )

        # Lado derecho de la paleta 
        pyxel.blt(
            self.x + self.sprite_w + (self.sprite_w * self.mid_sections),
            self.y,
            self.sprite_img,
            self.sprite_end_U,
            self.sprite_end_V,
            self.sprite_w * -1,
            self.sprite_w
        )