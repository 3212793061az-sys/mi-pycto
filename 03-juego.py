# Juego de acertijo simple

print("🧠 Bienvenido al juego de acertijos")
print("Adivina la respuesta correcta para ganar\n")

respuesta_correcta = "sombra"
intentos = 3

while intentos > 0:
    respuesta = input("Vuelo sin alas, lloro sin ojos. ¿Qué soy? ").lower()

    if respuesta == respuesta_correcta:
        print("🎉 ¡Correcto! Ganaste.")
        break
    else:
        intentos -= 1
        print("❌ Incorrecto. Te quedan", intentos, "intentos.\n")

if intentos == 0:
    print("💀 Perdiste. La respuesta era:", respuesta_correcta)