import json

def guardar_tareas(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks, file, indent=4)

def cargar_tareas():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def mostrar_lista_de_tareas(tasks,command):
    if len(tasks) != 0:
        for i in range(0,len(tasks)):
            estado = "✓" if tasks[i]["Done"] else " ✗ "
            print(f"{i+1}. {tasks[i]['task']} [{estado}]")
        if command=="LIST":
            return
    
        numero_eliminar = input(">> ")
        while not numero_eliminar.isdigit() or int(numero_eliminar)<1 or int(numero_eliminar) > len(tasks):
            numero_eliminar = input("Ingrese un numero valido >> ")
        return int(numero_eliminar)

def filtrar(tasks,command):
    if command == "DONE":
        if not any(task["Done"] for task in tasks):
            print("No hay tareas completadas")
            return
        
    if command == "PENDING":
        if not any( not task["Done"] for task in tasks):
            print("No hay tareas pendientes")
            return

    if len(tasks) != 0:
        for i in range(0,len(tasks)):
            estado = "✓" if tasks[i]["Done"] else " ✗ "
            if command == "DONE" and tasks[i]["Done"]:
                print(f"{i+1}. {tasks[i]['task']} [{estado}]")
            if command == "PENDING" and not tasks[i]["Done"]:
                print(f"{i+1}. {tasks[i]['task']} [{estado}]")
