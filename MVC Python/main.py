from controller import TaskController

def main():
    controller = TaskController()

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            task = input("Ingrese la tarea: ")
            controller.add_task(task)
            print("Tarea agregada.")
        elif choice == "2":
            controller.show_tasks()
        elif choice == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
