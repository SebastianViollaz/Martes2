def QuitarAlumno(ALUMNO,data):
        
    for elemnto in data["Alumnos"]:
        if elemnto["Nombre"] == ALUMNO:
            data["Alumnos"].remove(elemnto)


DATA = {"Alumnos" : []}


while True:
    print()
    print(DATA)
    print(" 1 : Agreagar alumno")
    print(" 2 : Quitar alumno")
    opcion = int(input("Que haces?:"))
    
    if opcion == 1:
        
        nombre = input("Ingrese un nombre: ")
        edad = input("Ingrese una edad: ")
        alumno = {"Nombre": nombre , "Edad": edad}
        DATA["Alumnos"].append(alumno)
        
    elif opcion == 2:
        QuitarAlumno(input("Que alumno quiere quitar? "),DATA)
    else: 
        print("Opcion invalida")