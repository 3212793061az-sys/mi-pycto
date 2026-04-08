usuarios = {}

# Agregar usuario
def agregar_usuario(username, password):
    if username in usuarios:
        print("❌ El usuario ya existe")
    else:
        usuarios[username] = password
        print("✅ Usuario agregado correctamente")

# Eliminar usuario
def eliminar_usuario(username):
    if username in usuarios:
        del usuarios[username]
        print("🗑️ Usuario eliminado")
    else:
        print("❌ Usuario no encontrado")

# Mostrar usuarios
def listar_usuarios():
    if usuarios:
        print("📋 Lista de usuarios:")
        for user in usuarios:
            print(f"- {user}")
    else:
        print("No hay usuarios")

# Menú simple
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar usuario")
    print("2. Eliminar usuario")
    print("3. Listar usuarios")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        user = input("Usuario: ")
        password = input("Contraseña: ")
        agregar_usuario(user, password)

    elif opcion == "2":
        user = input("Usuario a eliminar: ")
        eliminar_usuario(user)

    elif opcion == "3":
        listar_usuarios()

    elif opcion == "4":
        print("👋 Saliendo...")
        break

    else:
        print("❌ Opción inválida")