print("hola")
def calculadora():
    while True:
        try:
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: ingresa números válidos")
            continue

        print("\n1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Módulo")

        op = input("Elige una opción: ")

        if op == "1":
            print("Resultado:", n1 + n2)
        elif op == "2":
            print("Resultado:", n1 - n2)
        elif op == "3":
            print("Resultado:", n1 * n2)
        elif op == "4":
            if n2 != 0:
                print("Resultado:", n1 / n2)
            else:
                print("No se puede dividir entre 0")
        elif op == "5":
            if n2 != 0:
                print("Resultado:", n1 % n2)
            else:
                print("No se puede usar módulo con 0")
        else:
            print("Opción inválida")

        if input("\n¿Quieres continuar? (s/n): ").lower() != "s":
            break

calculadora()
