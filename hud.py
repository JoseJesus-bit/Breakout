import pyxel


def draw_hud(score =0, lives=0):
    #Dibujar el marcador
    pyxel.text(10, 5, "Score: " + str(score), 7)
    #Dibujar las vidas
    lives_text = "Lives: " + str(lives)
    pyxel.text(right_text(lives_text), 5, lives_text, 7)
    
    
def draw_dropped():
    tittle = "-1 Vida!, Cuidado!"
    subtitle = "Presiona espacio o Click para continuar"
    pyxel.text(center_text(tittle), pyxel.height / 3, tittle, 7)
    pyxel.text(center_text(subtitle), pyxel.height / 2, subtitle, 7)
    
    
def draw_game_over(score =0):
    tittle = "PERDISTE!"
    score_text = "Puntaje: " + str(score) + " puntos"
    press_enter_text = "Presiona Enter para reiniciar"
    press_esc_salir = "Presiona Esc para salir"
    pyxel.text(center_text(tittle), pyxel.height / 3, tittle, 7)
    pyxel.text(center_text(score_text), pyxel.height / 12 * 5, score_text, 7)
    pyxel.text(center_text(press_enter_text), pyxel.height / 2, press_enter_text, 7)
    pyxel.text(center_text(press_esc_salir), pyxel.height / 1.5, press_esc_salir, 7)

    
    
    
def draw_win(score =0):
    tittle = "FELICIDADES GANASTE!"
    score_text = "Puntaje: " + str(score) + " puntos"
    press_enter_text = "Presiona Enter para reiniciar"
    press_esc_salir = "Presiona Esc para salir"
    pyxel.text(center_text(tittle), pyxel.height / 3, tittle, 7)
    pyxel.text(center_text(score_text), pyxel.height / 12 * 5, score_text, 7)
    pyxel.text(center_text(press_enter_text), pyxel.height / 2, press_enter_text, 7)
    pyxel.text(center_text(press_esc_salir), pyxel.height / 1.5, press_esc_salir, 7)
    
    

# Hacemos una funcion que nos ayude para calcular el inicio del juego y el valor en el centro del juego
def center_text(text, char_width = pyxel.FONT_WIDTH):
    text_width = len(text) * char_width
    return (pyxel.width - text_width) / 2

# Otra funcion que nos ayude a alinear el texto 
def right_text(text, char_width = pyxel.FONT_WIDTH):
    text_width = len(text) * char_width
    return pyxel.width - (text_width + char_width)