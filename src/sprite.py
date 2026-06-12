import pygame

class SpritesMascota:
    def __init__(self):
        # Para cada etapa, define una lista con las imágenes de la animación
        self.sprites = {
            1: [pygame.image.load("assets/sprites/jyarimon_1.png"),
                pygame.image.load("assets/sprites/jyarimon_2.png")],
            2: [pygame.image.load("assets/sprites/gigimon_1.png"),
                pygame.image.load("assets/sprites/gigimon_2.png")],
            "3A": [pygame.image.load("assets/sprites/guilmon_1.png"),
                   pygame.image.load("assets/sprites/guilmon_2.png")],
            "3B": [pygame.image.load("assets/sprites/vmon_1.png"),
                   pygame.image.load("assets/sprites/vmon_2.png")],
            "4A": [pygame.image.load("assets/sprites/growmon_1.png"),
                   pygame.image.load("assets/sprites/growmon_2.png")],
            "4B": [pygame.image.load("assets/sprites/growmonorg_1.png"),
                   pygame.image.load("assets/sprites/growmonorg_2.png")],
            "4C": [pygame.image.load("assets/sprites/vdramon_1.png"),
                   pygame.image.load("assets/sprites/vdramon_2.png")],
            "4D": [pygame.image.load("assets/sprites/xvmon_1.png"),
                   pygame.image.load("assets/sprites/xvmon_2.png")],
            "5A": [pygame.image.load("assets/sprites/megalogrowmon_1.png"),
                   pygame.image.load("assets/sprites/megalogrowmon_2.png")],
            "5B": [pygame.image.load("assets/sprites/mgorg_1.png"),
                   pygame.image.load("assets/sprites/mgorg_2.png")],
            "5C": [pygame.image.load("assets/sprites/aerovdramon_1.png"),
                   pygame.image.load("assets/sprites/aerovdramon_2.png")],
            "5D": [pygame.image.load("assets/sprites/paildramon_1.png"),
                   pygame.image.load("assets/sprites/paildramon_2.png")],
            "6A": [pygame.image.load("assets/sprites/dukemon_1.png"),
                   pygame.image.load("assets/sprites/dukemon_2.png")],
            "6B": [pygame.image.load("assets/sprites/megidramon_1.png"),
                   pygame.image.load("assets/sprites/megidramon_2.png")],
            "6C": [pygame.image.load("assets/sprites/ulforcevdramon_1.png"),
                   pygame.image.load("assets/sprites/ulforcevdramon_2.png")],
            "6D": [pygame.image.load("assets/sprites/imperialdramondm_1.png"),
                   pygame.image.load("assets/sprites/imperialdramondm_2.png")],
            "6E": [pygame.image.load("assets/sprites/magnamon_1.png"),
                   pygame.image.load("assets/sprites/magnamon_2.png")],
            "7A": [pygame.image.load("assets/sprites/dukemoncm_1.png"),
                   pygame.image.load("assets/sprites/dukemoncm_2.png")],
            "7B": [pygame.image.load("assets/sprites/imperialdramonfm_1.png"),
                   pygame.image.load("assets/sprites/imperialdramonfm_2.png")]
        }

        # Ajustar el tamaño de las imágenes (2 por etapa)
        for key in self.sprites:
            self.sprites[key] = [pygame.transform.scale(img, (300, 300)) for img in self.sprites[key]]

    def obtener_sprite(self, etapa, indice_frame):
        # Devuelve el frame correspondiente en la animación de la etapa
        if etapa in self.sprites:
            return self.sprites[etapa][indice_frame]
        return None

