import math
import pygame

# ==========================================
# 1. CLASE PROPIA DE MATRICES Y TRANSFORMACIONES 2D/3D
# ==========================================
class Matriz:
    def __init__(self, filas, columnas, datos=None):
        self.filas = filas
        self.columnas = columnas
        if datos:
            self.datos = [fila[:] for fila in datos]
        else:
            self.datos = [[0.0 for _ in range(columnas)] for _ in range(filas)]

    @staticmethod
    def identidad(n):
        m = Matriz(n, n)
        for i in range(n):
            m.datos[i][i] = 1.0
        return m

    def multiplicar(self, otro):
        if self.columnas != otro.filas:
            raise ValueError("Dimensiones incompatibles para multiplicación de matrices.")
        resultado = Matriz(self.filas, otro.columnas)
        for i in range(self.filas):
            for j in range(otro.columnas):
                suma = 0.0
                for k in range(self.columnas):
                    suma += self.datos[i][k] * otro.datos[k][j]
                resultado.datos[i][j] = suma
        return resultado

    # Transformaciones Homogéneas 2D (3x3)
    @staticmethod
    def traslacion_2d(dx, dy):
        return Matriz(3, 3, [[1, 0, dx], [0, 1, dy], [0, 0, 1]])

    @staticmethod
    def rotacion_2d(angulo_grados):
        rad = math.radians(angulo_grados)
        c, s = math.cos(rad), math.sin(rad)
        return Matriz(3, 3, [[c, -s, 0], [s, c, 0], [0, 0, 1]])

    @staticmethod
    def escalamiento_2d(sx, sy):
        return Matriz(3, 3, [[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

    @staticmethod
    def sesgado_2d(shx, shy):
        return Matriz(3, 3, [[1, shx, 0], [shy, 1, 0], [0, 0, 1]])

    @staticmethod
    def reflexion_2d(eje='x'):
        if eje == 'x':
            return Matriz(3, 3, [[1, 0, 0], [0, -1, 0], [0, 0, 1]])
        elif eje == 'y':
            return Matriz(3, 3, [[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
        return Matriz.identidad(3)


# ==========================================
# 2. CURVAS DE BÉZIER (Para pistas o trayectorias)
# ==========================================
def curva_bezier(puntos_control, muestras=100):
    """Calcula los puntos de una curva de Bézier de n-ésimo grado."""
    n = len(puntos_control) - 1
    curva = []
    for t in range(muestras + 1):
        t_val = t / float(muestras)
        x, y = 0.0, 0.0
        for i, (px, py) in enumerate(puntos_control):
            combinatorio = math.comb(n, i)
            factor = combinatorio * (t_val ** i) * ((1 - t_val) ** (n - i))
            x += px * factor
            y += py * factor
        curva.append((x, y))
    return curva


# ==========================================
# 3. PROCESAMIENTO DE IMAGEN BMP (Modelos de color)
# ==========================================
def procesar_bmp_grises(matriz_pixels):
    """Convierte una matriz de píxeles RGB a escala de grises (luminancia)."""
    resultado = []
    for fila in matriz_pixels:
        nueva_fila = []
        for r, g, b in fila:
            gris = int(0.299 * r + 0.587 * g + 0.114 * b)
            nueva_fila.append((gris, gris, gris))
        resultado.append(nueva_fila)
    return resultado

def procesar_bmp_negativo(matriz_pixels):
    """Aplica efecto negativo a la imagen."""
    resultado = []
    for fila in matriz_pixels:
        nueva_fila = []
        for r, g, b in fila:
            nueva_fila.append((255 - r, 255 - g, 255 - b))
        resultado.append(nueva_fila)
    return resultado


# ==========================================
# 4. OBJETOS 3D Y ELIMINACIÓN DE CARAS OCULTAS
# ==========================================
class Objeto3D:
    def __init__(self, vertices, caras):
        self.vertices = vertices  # Lista de tuplas (x, y, z)
        self.caras = caras        # Lista de listas con índices de vértices

    def proyeccion_perspectiva(self, fov, distancia_camara):
        proyectados = []
        for x, y, z in self.vertices:
            factor = fov / (z + distancia_camara)
            px = x * factor + 400  # Centrado en pantalla de 800x600
            py = -y * factor + 300
            proyectados.append((px, py, z))
        return proyectados


# ==========================================
# 5. BUCLE PRINCIPAL E INTERACCIÓN (Pygame)
# ==========================================
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Proyecto Final de Graficación - Motor Base")
    clock = pygame.time.Clock()

    # Datos de prueba para Curva de Bézier (ej. diseño de pista o ruta enemiga)
    puntos_control = [(100, 450), (250, 100), (550, 100), (700, 450)]
    pista_bezier = curva_bezier(puntos_control, 60)

    # Definición de un Objeto 3D (Cubo con vértices, aristas y caras)
    vertices_cubo = [
        (-40, -40, -40), (40, -40, -40), (40, 40, -40), (-40, 40, -40),
        (-40, -40, 40),  (40, -40, 40),  (40, 40, 40),  (-40, 40, 40)
    ]
    caras_cubo = [
        (0, 1, 2, 3), (5, 4, 7, 6), (4, 0, 3, 7),
        (1, 5, 6, 2), (4, 5, 1, 0), (3, 2, 6, 7)
    ]
    cubo = Objeto3D(vertices_cubo, caras_cubo)

    angulo = 0
    running = True
    while running:
        screen.fill((15, 15, 25))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Dibuja elementos 2D (Líneas, Polilíneas y Curvas) ---
        if len(pista_bezier) > 1:
            pygame.draw.aalines(screen, (0, 200, 255), False, pista_bezier)

        # --- Transformaciones y proyecciones 3D con Vector Normal (Backface Culling) ---
        angulo += 1
        rad = math.radians(angulo)
        c, s = math.cos(rad), math.sin(rad)

        verts_rotados = []
        for x, y, z in cubo.vertices:
            # Rotación en ejes Y y X
            x_rot = x * c + z * s
            z_rot = -x * s + z * c
            y_rot = y
            verts_rotados.append((x_rot, y_rot, z_rot + 300))

        # Renderizado de caras ocultas aplicando producto cruz (vector normal)
        for cara in caras_cubo:
            p0 = verts_rotados[cara[0]]
            p1 = verts_rotados[cara[1]]
            p2 = verts_rotados[cara[2]]

            # Cálculo del vector normal de la cara
            v1 = (p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2])
            v2 = (p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2])
            nz = v1[0] * v2[1] - v1[1] * v2[0]

            # Si nz < 0, la cara apunta hacia el observador (se dibuja)
            if nz < 0:
                pts_2d = []
                for idx in cara:
                    vx, vy, vz = verts_rotados[idx]
                    f = 350 / vz
                    pts_2d.append((vx * f + 400, vy * f + 300))
                
                # Relleno de polígono y wireframe (Modelos de color básicos)
                pygame.draw.polygon(screen, (50, 120, 200), pts_2d)
                pygame.draw.polygon(screen, (200, 220, 255), pts_2d, 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()