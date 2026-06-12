import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
GRIS = (197, 188, 188)

class CuadroTexto:
    def __init__(self, x, y, ancho, alto, color):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = color
        self.texto = ''
        self.fuente = pygame.font.Font(None, 32)
        self.activo = False

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                self.activo = True
            else:
                self.activo = False
        if evento.type == pygame.KEYDOWN:
            if self.activo:
                if evento.key == pygame.K_RETURN:
                    return self.texto
                elif evento.key == pygame.K_BACKSPACE:
                    self.texto = self.texto[:-1]
                else:
                    self.texto += evento.unicode
        return None

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, self.rect, 2)
        texto_superficie = self.fuente.render(self.texto, True, NEGRO)
        ventana.blit(texto_superficie, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(ventana, self.color, self.rect, 2)
