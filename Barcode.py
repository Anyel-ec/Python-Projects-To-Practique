import cv2
from pyzbar.pyzbar import decode

# Inicializa la cámara
cap = cv2.VideoCapture(0)

while True:
    # Captura un fotograma de la cámara
    ret, frame = cap.read()

    # Decodifica los códigos de barras en el fotograma
    decoded_objects = decode(frame)

    for obj in decoded_objects:
        barcode_data = obj.data.decode('utf-8')
        barcode_type = obj.type

        # Muestra los resultados en la pantalla
        print(f'Tipo de código de barras: {barcode_type}')
        print(f'Dato del código de barras: {barcode_data}')

    # Muestra el fotograma en una ventana
    cv2.imshow('Codigo de Barras Scanner', frame)

    # Sale del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra la ventana
cap.release()
cv2.destroyAllWindows()
