import json
import time
import pygame
from sprite import SpritesMascota

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
GRIS = (197, 188, 188)

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO_VENTANA = 480
ALTO_VENTANA = 640

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mascota Virtual")


class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.carino = 100
        self.higiene = 100
        self.fuerza = 0
        self.poder = 0
        self.etapa = 1
        self.viva = True
        self.sprites = SpritesMascota()

        # Animación
        self.sprite_actual = 0  # Índice del frame actual (0 o 1)
        self.tiempo_animacion = 0
        self.duracion_frame = 200  # Duración en milisegundos de cada frame

    def mostrar_sprite(self, ventana):
        # Obtener el frame actual de la animación
        sprite = self.sprites.obtener_sprite(self.etapa, self.sprite_actual)
        if sprite:
            ventana.blit(sprite, (90, 200))

        # Control del tiempo para cambiar de frame
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_animacion > self.duracion_frame:
            self.sprite_actual = (self.sprite_actual + 1) % 2  # Alterna entre 0 y 1
            self.tiempo_animacion = tiempo_actual

    def mostrar_estado(self, ventana):
        fuente = pygame.font.Font(None, 36)
        texto = f"Salud: {self.salud}, Cariño: {self.carino}, Higiene: {self.higiene}, Fuerza: {self.fuerza}, Poder: {self.poder}, Etapa: {self.etapa}"
        estado_mascota = fuente.render(texto, True, NEGRO)
        ventana.blit(estado_mascota, (50, 50))

    # Métodos de alimentar, acariciar, bañar, etc...
    # (Todo lo relacionado a la lógica de la mascota)

    def actualizar_poder(self):
        self.poder = self.fuerza // 5

    def alimentar(self):
        if self.salud < 100:
            self.salud += 10
            if self.salud > 100:
                self.salud = 100
            print(f"Has alimentado a {self.nombre}. Salud aumentada.")
        else:
            print(f"{self.nombre} ya está en su salud máxima.")

    def acariciar(self):
        if self.carino < 100:
            self.carino += 10
            if self.carino > 100:
                self.carino = 100
            print(f"Has acariciado a {self.nombre}. Cariño aumentado.")
        else:
            print(f"{self.nombre} ya está en su máximo cariño.")

    def banar(self):
        if self.higiene < 100:
            self.higiene += 10
            if self.higiene > 100:
                self.higiene = 100
            print(f"Has bañado a {self.nombre}. Higiene aumentada.")
        else:
            print(f"{self.nombre} ya está en su máxima higiene.")

    def entrenar(self):
        if self.salud > 5 and self.higiene > 5:
            self.fuerza += 1
            self.higiene -= 5
            self.actualizar_poder()
            print(f"Has entrenado a {self.nombre}. Fuerza aumentada en 1 punto, higiene reducida en 5 puntos.")
        else:
            print(f"{self.nombre} no puede entrenar. Necesita más salud y/o higiene.")

    def disminuir_atributos(self):
        while self.viva:
            if self.salud > 0:
                self.salud -= 1
            if self.salud < 0:
                self.salud = 0
            if self.carino > 0:
                self.carino -= 1
            if self.carino < 0:
                self.carino = 0
            if self.higiene > 0:
                self.higiene -= 1
            if self.higiene < 0:
                self.higiene = 0
            if self.salud == 0 or self.carino == 0 or self.higiene == 0:
                self.viva = False
                print(f"{self.nombre} se ha debilitado demasiado y no puede continuar.")
            time.sleep(5)
    
    def aumentar_etapa(self):
        time.sleep(20)
        if self.etapa == 1:
            self.etapa = 2
            print(f"{self.nombre} ha alcanzado la Etapa 2.")

        time.sleep(30)
        if self.etapa == 2:
            if self.poder >= 3:
                self.etapa = "3A"
                print(f"{self.nombre} ha alcanzado la Etapa 3A debido a su alto poder.")
            else:
                self.etapa = "3B"
                print(f"{self.nombre} ha alcanzado la Etapa 3B debido a su bajo poder.")

        time.sleep(50)
        if self.etapa == "3A":
            if self.poder >= 10:
                self.etapa = "4A"
                print(f"{self.nombre} ha alcanzado la Etapa 4A.")
            elif 5 <= self.poder < 10:
                self.etapa = "4B"
                print(f"{self.nombre} ha alcanzado la Etapa 4B.")
            elif self.poder < 5:
                self.etapa = "4D"
                print(f"{self.nombre} ha alcanzado la Etapa 4D.")

        elif self.etapa == "3B":
            if self.poder >= 5:
                self.etapa = "4B"
                print(f"{self.nombre} ha alcanzado la Etapa 4B.")
            elif 2 < self.poder < 5:
                self.etapa = "4C"
                print(f"{self.nombre} ha alcanzado la Etapa 4C.")
            elif self.poder <= 2:
                self.etapa = "4D"
                print(f"{self.nombre} ha alcanzado la Etapa 4D.")

        time.sleep(90)
        if self.etapa == "4A":
            if self.poder >= 20:
                self.etapa = "5A"
                print(f"{self.nombre} ha alcanzado la Etapa 5A.")
            elif 10 <= self.poder < 20:
                self.etapa = "5B"
                print(f"{self.nombre} ha alcanzado la Etapa 5B.")

        elif self.etapa == "4B":
            if self.poder >= 30:
                self.etapa = "5A"
                print(f"{self.nombre} ha alcanzado la Etapa 5A.")
            elif 6 < self.poder < 30:
                self.etapa = "5B"
                print(f"{self.nombre} ha alcanzado la Etapa 5B.")
        
        elif self.etapa == "4C":
            if self.poder >= 20:
                self.etapa = "5C"
                print(f"{self.nombre} ha alcanzado la Etapa 5C.")
            elif 6 < self.poder < 20:
                self.etapa = "5D"
                print(f"{self.nombre} ha alcanzado la Etapa 5D.")

        elif self.etapa == "4D":
            if self.poder >= 30:
                self.etapa = "5C"
                print(f"{self.nombre} ha alcanzado la Etapa 5C.")
            elif 6 < self.poder < 30:
                self.etapa = "5D"
                print(f"{self.nombre} ha alcanzado la Etapa 5D.")

        time.sleep(120)
        if self.etapa == "5A":
            if self.poder >= 30:
                self.etapa = "6A"
                print(f"{self.nombre} ha alcanzado la Etapa 6A.")
            elif 20 <= self.poder < 30:
                self.etapa = "6B"
                print(f"{self.nombre} ha alcanzado la Etapa 6B.")

        elif self.etapa == "5B":
            if self.poder >= 60:
                self.etapa = "6A"
                print(f"{self.nombre} ha alcanzado la Etapa 6A.")
            elif 10 < self.poder < 60:
                self.etapa = "6B"
                print(f"{self.nombre} ha alcanzado la Etapa 6B.")
        
        elif self.etapa == "5C":
            if self.poder >= 25:
                self.etapa = "6C"
                print(f"{self.nombre} ha alcanzado la Etapa 6C.")

        elif self.etapa == "5D":
            if self.poder >= 35:
                self.etapa = "6D"
                print(f"{self.nombre} ha alcanzado la Etapa 6D.")
            elif 6 < self.poder < 35:
                self.etapa = "6E"
                print(f"{self.nombre} ha alcanzado la Etapa 6E.")

        time.sleep(130)
        if self.etapa == "6A":
            if self.poder >= 65:
                self.etapa = "7A"
                print(f"{self.nombre} ha alcanzado la Etapa 7A.")
            elif 40 <= self.poder < 65:
                self.etapa = "7A"
                print(f"{self.nombre} ha alcanzado la Etapa 7A.")

        elif self.etapa == "6D":
            if self.poder >= 40:
                self.etapa = "7B"
                print(f"{self.nombre} ha alcanzado la Etapa 6A.")



    def guardar_progreso(self):
        estado_mascota = {
            "nombre": self.nombre,
            "salud": self.salud,
            "carino": self.carino,
            "higiene": self.higiene,
            "fuerza": self.fuerza,
            "poder": self.poder,
            "etapa": self.etapa,
            "viva": self.viva
        }
        
        with open("saves/progreso_mascota.json", "w") as archivo:
            json.dump(estado_mascota, archivo)
        print(f"Progreso de {self.nombre} guardado correctamente.")

    def cargar_progreso(self):
        try:
            with open("saves/progreso_mascota.json", "r") as archivo:
                estado_mascota = json.load(archivo)
                self.__dict__.update(estado_mascota)
            print(f"Progreso de {self.nombre} cargado correctamente.")
        except FileNotFoundError:
            print("No hay un progreso guardado.")

