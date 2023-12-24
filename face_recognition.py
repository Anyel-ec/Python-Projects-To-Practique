import cv2
import face_recognition

def reconocer_caras(imagen_path):
    # Cargar la imagen
    imagen = face_recognition.load_image_file(imagen_path)

    # Encontrar todas las caras en la imagen
    ubicaciones = face_recognition.face_locations(imagen)

    # Dibujar un rectángulo alrededor de cada cara encontrada
    for ubicacion in ubicaciones:
        top, right, bottom, left = ubicacion
        cv2.rectangle(imagen, (left, top), (right, bottom), (0, 255, 0), 2)

    # Mostrar la imagen con las caras resaltadas
    cv2.imshow('Caras Reconocidas', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Ruta de la imagen que deseas analizar
    ruta_imagen = 'ruta/a/tu/imagen.jpg'

    # Llamar a la función para reconocer caras
    reconocer_caras(ruta_imagen)
