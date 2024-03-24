import cv2

# Cargar la imagen
image = cv2.imread('imagen.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Crear un objeto BackgroundSubtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

# Aplicar la segmentación de fondo
foreground_mask = bg_subtractor.apply(gray)

# Invertir la máscara para obtener el primer plano
foreground = cv2.bitwise_and(image, image, mask=foreground_mask)
background = cv2.bitwise_and(image, image, mask=~foreground_mask)

# Mostrar resultados
cv2.imshow('Original', image)
cv2.imshow('Foreground', foreground)
cv2.imshow('Background', background)
cv2.waitKey(0)
cv2.destroyAllWindows()
