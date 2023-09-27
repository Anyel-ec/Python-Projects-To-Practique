import curses
import time

def main(stdscr):
    # Configurar curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(1000)  # Actualizar cada segundo

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Obtener la hora actual
        current_time = time.strftime("%H:%M:%S")

        # Centrar el reloj en la pantalla
        x = width // 2 - len(current_time) // 2
        y = height // 2

        # Imprimir la hora actual en el centro de la pantalla
        stdscr.addstr(y, x, current_time)

        # Refrescar la pantalla
        stdscr.refresh()

        # Salir si se presiona 'q'
        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
