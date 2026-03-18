import json
import module

tasks = module.cargar_tareas()

command = ""

comandos = {
    "help":"mostrar lista de comandos",
    "add":"añadir tarea",
    "delete":"eliminar tarea",
    "list":"mostrar lista de deberes",
    "complete":"Completar tarea",
    "uncomplete":"Desmarcar una tarea",
    "done":"Tareas hechas",
    "pending":"Tareas pendientes",
    "exit":"salir"
}

print("Hola, que deseas hacer?")
while command != "EXIT":
    print("Escribe HELP para ver los comandos")

    command = input(">> ").upper()
    #HELP
    if command == "HELP":
        for key,value in comandos.items():
            print(f"{key} : {value}")

    #ADD
    elif command == "ADD":
        print("Ingrese la tarea a añadir")
        tarea = input(">> ")
        tasks.append({
                "task":tarea,
                "Done":False
            })

        module.guardar_tareas(tasks)
        print("Tarea ingresada correctamente")

    #DELETE
    elif command == "DELETE":
        if len(tasks) == 0:
            print("No hay tareas añadidas")
            continue
        print("Ingrese el numero de la tarea a eliminar")
        if len(tasks) != 0:
            numero_eliminar = module.mostrar_lista_de_tareas(tasks,command)
            eliminada = tasks.pop(numero_eliminar-1)
            module.guardar_tareas(tasks)
            print(f"Se elimino exitosamente {eliminada['task']} de la lista")
    
    #LIST
    elif command == "LIST":
        if len(tasks) == 0:
            print("No hay tareas añadidas")
            continue
        print("Your to do list: ")
        module.mostrar_lista_de_tareas(tasks,command)

    #COMPLETE
    elif command == "COMPLETE":
        if len(tasks) == 0:
            print("No hay tareas añadidas")
            continue
        print("Ingrese el numero de la tarea a marcar como completa")
        completada = module.mostrar_lista_de_tareas(tasks,command)
        tasks[completada-1]["Done"] = True
        print(f"La tarea {tasks[completada-1]['task']} ha sido completada! ")
        module.guardar_tareas(tasks)

    #UNCOMPLETE
    elif command == "UNCOMPLETE":
        if len(tasks) == 0:
            print("No hay tareas añadidas")
            continue
        print("Ingrese el numero de la tarea a quitar de completa")
        completada = module.mostrar_lista_de_tareas(tasks,command)
        tasks[completada-1]["Done"] = False
        print(f"La tarea {tasks[completada-1]['task']} ha sido desmarcada ")
        module.guardar_tareas(tasks)

    #DONE
    elif command == "DONE":
        if len(tasks) == 0:
            print("No hay tareas añadidas")
            continue
        module.filtrar(tasks,command)
    
    #PENDING
    elif command == "PENDING":
        if len(tasks) == 0:
            print("No hay tareas añadidas")
            continue
        module.filtrar(tasks,command)

    else:
        print("Comando no reconocido")
        print("Introduce HELP para ver la lista de comandos")

if command == "EXIT":
    print("Hasta luego!")
