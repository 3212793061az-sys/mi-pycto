def registrar_usuario():
    usuario = input("Ingresa el nombre de usuario: ")
    contraseña = input("Ingresa la contraseña: ")

    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario},{contraseña}\n")

    print("Usuario registrado correctamente.")

def mostrar_usuarios():
    try:
        with open("usuarios.txt", "r") as archivo:
            print("\nUsuarios registrados:")
            for linea in archivo:
                usuario, contraseña = linea.strip().split(",")
                print(f"Usuario: {usuario} | Contraseña: {contraseña}")
    except FileNotFoundError:
        print("No hay usuarios registrados.")

# Menú simple
while True:
    print("\n1. Registrar usuario")
    print("2. Mostrar usuarios")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        mostrar_usuarios()
    elif opcion == "3":
        break
    else:
        print("Opción inválida")