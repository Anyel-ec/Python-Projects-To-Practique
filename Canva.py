import cv2
import numpy as np

# Cargamos la imagen
imagen = cv2.imread('anyel-ec.jpg')

# Convertimos la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicamos un desenfoque para reducir el ruido
gris = cv2.GaussianBlur(gris, (5, 5), 0)

# Detectamos los bordes en la imagen
bordes = cv2.Canny(gris, 50, 150, apertureSize=3)

# Buscamos contornos en la imagen
contornos, _ = cv2.findContours(bordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iteramos a través de los contornos encontrados
for contorno in contornos:
    # Aproximamos el contorno a una forma más simple (en este caso, un polígono)
    epsilon = 0.04 * cv2.arcLength(contorno, True)
    approx = cv2.approxPolyDP(contorno, epsilon, True)

    # Si el polígono tiene 4 vértices, es un cuadrado
    if len(approx) == 4:
        cv2.drawContours(imagen, [approx], 0, (0, 255, 0), 2)

# Mostramos la imagen con los cuadrados detectados
cv2.imshow('Imagen con cuadrados', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
