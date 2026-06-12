import pygame
import threading
import sys  # Asegúrate de importar sys para poder salir correctamente
from cuadroTexto import CuadroTexto
from boton import Boton
from mascota import MascotaVirtual  # Asumiendo que tienes esta clase en mascota.py

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO_VENTANA = 480
ALTO_VENTANA = 640

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (114, 193, 255)
ROJO = (255, 118, 114)
VERDE = (131, 255, 114)
GRIS = (197, 188, 188)

color_texto = (255, 255, 255)

# Crear la ventana del juego
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), pygame.RESIZABLE)
pygame.display.set_caption("Mascota Virtual")

#fuente
fuente_personalizada = pygame.font.Font("assets/fonts/MinimalPixelv2.ttf")

# Cargar imagen del botón
imagen_boton = "assets/sprites/boton.png"  # Asegúrate de tener la imagen

# Crear botón con imagen
boton = Boton(160, 350, 160, 50, imagen_boton, )

# Inicializa el reloj
reloj = pygame.time.Clock()

#Fondo juego
fondo = pygame.image.load('assets/sprites/park2.png')
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

# Cargar una imagen de fondo para la pantalla de inicio
fondo_inicio = pygame.image.load('assets/sprites/inicio.png')
fondo_inicio = pygame.transform.scale(fondo_inicio, (ANCHO_VENTANA, ALTO_VENTANA))


# Función para dibujar barras de atributos
def dibujar_barra(ventana, x, y, ancho, alto, valor_actual, valor_max, color_borde, color_relleno,texto, fuente, color_texto):
    # Dibujar el borde de la barra
    pygame.draw.rect(ventana, color_borde, (x, y, ancho, alto), 2)
    
    # Calcular el ancho de la barra rellena según el valor actual
    ancho_relleno = (valor_actual / valor_max) * (ancho - 4)  # Dejamos 2 píxeles de margen para el borde
    
    # Dibujar el relleno de la barra
    pygame.draw.rect(ventana, color_relleno, (x + 2, y + 2, ancho_relleno, alto - 4))

    # Renderizar el texto
    texto_renderizado = fuente.render(texto, True, color_texto)
    
    # Calcular la posición del texto para centrarlo en la barra
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))

    # Dibujar el texto en la pantalla
    ventana.blit(texto_renderizado, texto_rect)

# Función principal del juego
def juego():
    ventana_inicio = True
    cuadro_texto = CuadroTexto(160, 60, 160, 40, NEGRO,)
    boton_cargar = Boton(160, 130, 160, 50, "assets/sprites/boton.png", "Cargar Partida", fuente_personalizada)
    boton_nueva = Boton(160, 450, 160, 50, "assets/sprites/boton.png", "Nueva Partida", fuente_personalizada)
    boton_salir_inicio = Boton(160, 550, 160, 50, "assets/sprites/boton.png", "Salir", fuente_personalizada)

    mascota = None  # Inicializar la variable mascota

    while ventana_inicio:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Manejar cuadro de texto
            nombre = cuadro_texto.manejar_evento(evento)
            if nombre is not None:
                mascota = MascotaVirtual(nombre)
                ventana_inicio = False

            # Manejar botones
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion = pygame.mouse.get_pos()
                if boton_cargar.es_clicado(posicion):
                    mascota = MascotaVirtual("Mascota")
                    mascota.cargar_progreso()
                    ventana_inicio = False
                if boton_nueva.es_clicado(posicion):
                    nombre = cuadro_texto.texto
                    if nombre:
                        mascota = MascotaVirtual(nombre)
                        ventana_inicio = False
                if boton_salir_inicio.es_clicado(posicion):
                    pygame.quit()
                    sys.exit()  # Termina el programa correctamente

        # Dibujar pantalla inicial
        ventana.blit(fondo_inicio, (0, 0))
        cuadro_texto.dibujar(ventana)
        boton_cargar.dibujar(ventana)
        boton_nueva.dibujar(ventana)
        boton_salir_inicio.dibujar(ventana)
        pygame.display.flip()

    # Hilos para manejar atributos de la mascota
    thread_disminuir = threading.Thread(target=mascota.disminuir_atributos)
    thread_disminuir.start()

    thread_etapa = threading.Thread(target=mascota.aumentar_etapa)
    thread_etapa.start()

    # Crear botones
    boton_alimentar = Boton(0, 600, 96, 40,"assets/sprites/boton.png" ,"Alimentar",fuente_personalizada)
    boton_acariciar = Boton(96, 600, 96, 40, "assets/sprites/boton.png", "Acariciar", fuente_personalizada)
    boton_banar = Boton(192, 600, 96, 40, "assets/sprites/boton.png", "Asear", fuente_personalizada)
    boton_entrenar = Boton(288, 600, 96, 40, "assets/sprites/boton.png", "Entrenar",fuente_personalizada)
    boton_guardar_progreso = Boton(384, 600, 96, 40, "assets/sprites/boton.png", "Guardar",fuente_personalizada)
    boton_salir_juego = Boton(384, 5, 96, 40, "assets/sprites/boton.png", "Salir",fuente_personalizada)

    en_juego = True
    while en_juego:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = False
                pygame.quit()
                sys.exit()  # Termina el programa correctamente

            # Manejar botones durante el juego
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion = pygame.mouse.get_pos()
                
                if boton_alimentar.es_clicado(posicion):
                    mascota.alimentar()
                if boton_acariciar.es_clicado(posicion):
                    mascota.acariciar()
                if boton_banar.es_clicado(posicion):
                    mascota.banar()
                if boton_entrenar.es_clicado(posicion):
                    mascota.entrenar()
                if boton_guardar_progreso.es_clicado(posicion):
                    mascota.guardar_progreso()
                if boton_salir_juego.es_clicado(posicion):
                    en_juego = False
                    pygame.quit()
                    sys.exit()  # Termina el programa correctamente

        # Dibujar el fondo
        ventana.blit(fondo, (0, 0))  # Dibuja el fondo en la posición (0, 0)
        
        #Dibujar el botón en la ventana
        ventana.fill((0, 0, 0))  # Fondo negro
        boton.dibujar(ventana)
        
        # Rellenar la pantalla de blanco
        ventana.blit(fondo, (0, 0))  # Dibuja el fondo en la posición (0, 0)

        # Dibujar los botones
        boton_alimentar.dibujar(ventana)
        boton_acariciar.dibujar(ventana)
        boton_banar.dibujar(ventana)
        boton_entrenar.dibujar(ventana)
        boton_guardar_progreso.dibujar(ventana)
        boton_salir_juego.dibujar(ventana)

        # Dibujar las barras de atributos
        dibujar_barra(ventana, 5, 5, 200, 30, mascota.salud, 100, NEGRO, VERDE,"Salud",fuente_personalizada,NEGRO)
        dibujar_barra(ventana, 5, 40, 200, 30, mascota.carino, 100, NEGRO, ROJO,"Amistad",fuente_personalizada,NEGRO)
        dibujar_barra(ventana, 5, 75, 200, 30, mascota.higiene, 100, NEGRO, AZUL,"Higiene", fuente_personalizada,NEGRO)

        # Mostrar estado de la mascota
       # mascota.mostrar_estado(ventana)

        # Mostrar el sprite de la mascota según la etapa actual
        mascota.mostrar_sprite(ventana)

        
        # Actualizar la pantalla
        pygame.display.flip()

        # Limitar a 60 FPS
        reloj.tick(60)

    # Asegurarse de que los hilos terminen
    thread_disminuir.join()
    thread_etapa.join()

    pygame.quit()
    sys.exit()

# Llamar a la función principal
if __name__ == "__main__":
    juego()
