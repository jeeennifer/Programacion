
usuarios= []

def ingresar():
    while True:
        nombre= input("Ingrese nombre de usuario: ").upper()
        if nombre in usuarios:
            print("Usuario ya existe. Intente otro.")
        else: 
            break


    while True:
        sexo= input("Ingrese sexo (M/F): ").upper()
        if sexo.upper()=="M" or sexo.upper()=="F":
            break
        else:
            print("Debe ingresar solo M O F.")
                        
    while True:
        contraseña = input("Ingrese contraseña: ").upper()
        if len(contraseña)>=8:
                print("Contraseña válida.")
                break
        else:
            print("Contaseña no valida. Intente otra.")
           
     
    usuarios.append({"nombre": nombre, "sexo": sexo, "contraseña": contraseña})
    print("Usuario ingresado con exito!")  
   
    
def buscar():
    nombre=input("Ingrese usuario a buscar: ").upper()
    for usuario in usuarios:
        if nombre==usuario["nombre"]:
            print("El sexo del usuario es:", usuario["sexo"], "y la contraseña es:",  usuario["contraseña"])
            return
       
    print("El usuario no se encuentra. ")

def eliminar():
    nombre=input("Ingrese usuario a eliminar: ").upper()
    for usuario in usuarios:
        if nombre==usuario["nombre"]: 
            usuarios.remove(usuario) 
            print("Usuario eliminado con éxito!")
        else:
            print("No se pudo eliminar usuario!")    

opcion=0

while opcion!=4:
    print("MENU PRINCIPAL")
    print("1. Ingresar usuario.")
    print("2. Buscar usuario. ")
    print("3. Eliminar usuario.")
    print("4. Salir")

    try:
        opcion= int(input("Ingrese una opción: "))
    
        match opcion:
            case 1:
                ingresar()
            case 2:
                buscar()
            case 3: 
                eliminar()
            case 4:
                print("Programa terminado...")
                break
            case _:
                print("Debe ingresar una opción válida!!")

    except ValueError as error:
        print(f"Debe solo ingresar números enteros. Error: {error}")
            



