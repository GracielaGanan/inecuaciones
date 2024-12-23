import pygame
import random
import math

# es para iniciar el juego
pygame.init()

# ponemos los colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

# medida de la pantalla
ANCHO = 800
ALTO = 600

# iniciamos la ventana del juego
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Challenge de Pitágoras")

# en esta lista vamos almacenar los triángulos
triangulos = []


def generar_triangulo():
    hipotenusa = random.randint(100, 300)  # Hipotenusa aleatoria
    cateto_ad = random.randint(50, int(hipotenusa))  # Cateto adyacente aleatorio
    cateto_op = math.sqrt(hipotenusa**2 - cateto_ad**2)  # Cateto opuesto usando Pitágoras
    return hipotenusa, cateto_ad, cateto_op

# Función para dibujar el triángulo en pantalla
def dibujar_triangulo(cateto_ad, cateto_op, hipotenusa, pos_x, pos_y):
    punto_A = (pos_x, pos_y)
    punto_B = (pos_x + cateto_ad, pos_y)
    punto_C = (pos_x, pos_y - cateto_op)
    pygame.draw.polygon(screen, AZUL, [punto_A, punto_B, punto_C])


jugando = True
while jugando:
    screen.fill(BLANCO)  # Fondo blanco
    
    # Generamos un nuevo triángulo
    hipotenusa, cateto_ad, cateto_op = generar_triangulo()

    # le preguntamos al jugador por la medida del cateto
    fuente = pygame.font.SysFont('arial', 30)
    texto = fuente.render(f"Ingresa un cateto para la hipotenusa de {hipotenusa}: ", True, NEGRO)
    screen.blit(texto, (20, 20))
    pygame.display.update()

    # entrada del jugador
    input_text = ''
    esperando_entrada = True
    while esperando_entrada:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
                esperando_entrada = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        # Verificar si el número ingresado es correcto
                        cateto_ingresado = float(input_text)
                        if math.isclose(cateto_ingresado, cateto_ad, abs_tol=5):  # Compara con un margen de error
                            
                            pos_x = random.randint(50, ANCHO - 200)
                            pos_y = random.randint(50, ALTO - 200)
                            triangulos.append((cateto_ad, cateto_op, hipotenusa, pos_x, pos_y))
                            esperando_entrada = False
                        else:
                            input_text = ''  # Si el cateto no es correcto, el jugador tiene que intentarlo de nuevo
                    except ValueError:
                        input_text = ''  # Si el ingreso no es un número válido
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
                screen.fill(BLANCO)
                screen.blit(texto, (20, 20))
                texto_ingresado = fuente.render(f"Tu respuesta: {input_text}", True, NEGRO)
                screen.blit(texto_ingresado, (20, 60))
                pygame.display.update()

    # Dibujar los triángulos en la pantalla
    for (cateto_ad, cateto_op, hipotenusa, pos_x, pos_y) in triangulos:
        dibujar_triangulo(cateto_ad, cateto_op, hipotenusa, pos_x, pos_y)

    pygame.display.update()
    pygame.time.delay(500)

pygame.quit()
