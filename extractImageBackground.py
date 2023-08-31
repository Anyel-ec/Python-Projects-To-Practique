import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('imagen.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización para separar el objeto del fondo
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Encontrar contornos en la imagen umbralizada
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear una máscara en blanco del mismo tamaño que la imagen
mask = np.zeros_like(image)

# Dibujar los contornos en la máscara
cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

# Extraer el objeto en primer plano usando la máscara
foreground = cv2.bitwise_and(image, mask)

# Mostrar la imagen original, la máscara y el objeto en primer plano
cv2.imshow('Original', image)
cv2.imshow('Mask', mask)
cv2.imshow('Foreground', foreground)
cv2.waitKey(0)
cv2.destroyAllWindows()
