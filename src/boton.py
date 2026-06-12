import pygame

class Boton:
    def __init__(self, x, y, ancho, alto, imagen_ruta, texto="", fuente=None):
        # Cargar la imagen y escalarla al tamaño del botón
        self.imagen = pygame.image.load(imagen_ruta)
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        # Crear un rectángulo para la colisión y la posición del botón
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        # Texto opcional para añadir sobre el botón
        self.texto = texto
        # Usar la fuente proporcionada o una por defecto
        self.fuente = fuente if fuente else pygame.font.Font(None, 24)

    def dibujar(self, ventana):
        # Dibujar el botón usando la imagen
        ventana.blit(self.imagen, (self.rect.x, self.rect.y))
        # Si el botón tiene texto, renderizarlo encima de la imagen
        if self.texto:
            texto_renderizado = self.fuente.render(self.texto, True, (255, 255, 255))
            texto_rect = texto_renderizado.get_rect(center=self.rect.center)
            ventana.blit(texto_renderizado, texto_rect)

    def es_clicado(self, posicion):
        # Verificar si el botón ha sido clicado en una posición dada
        return self.rect.collidepoint(posicion)
