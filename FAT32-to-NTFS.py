import ctypes
import os

def change_filesystem_to_ntfs(drive_letter):
    # Obtener la ruta de la unidad
    drive_path = f"{drive_letter}:\\"

    # Comprobar si la unidad existe
    if not os.path.exists(drive_path):
        print(f"La unidad {drive_letter} no está disponible.")
        return

    # Cambiar el sistema de archivos de FAT32 a NTFS
    result = ctypes.windll.shell32.SHFormatDrive(0, 1, drive_letter + ":", 0)
    if result != 0:
        print("¡El cambio de sistema de archivos ha sido exitoso!")
    else:
        print("¡Ha ocurrido un error al intentar cambiar el sistema de archivos!")

# Cambiar la letra de unidad según tu flash
drive_letter = "F"  # Cambia esto a la letra de unidad de tu flash

# Llamar a la función para cambiar el sistema de archivos
change_filesystem_to_ntfs(drive_letter)
