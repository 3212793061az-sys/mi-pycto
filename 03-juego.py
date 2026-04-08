print("🧠 Bienvenido al juego de acertijos")
print("Adivina la respuesta correcta para ganar\n")

respuesta_correcta = "sombra"
respuesta_correcta2 = "promesa"
intentos = 3

while intentos > 0:
    respuesta = input("Vuelo sin alas, lloro sin ojos. ¿Qué soy? ").strip().lower()
    
    if respuesta == respuesta_correcta:
        print("🎉 ¡Correcto! Ganaste la primera.\n")
        
      
        intentos2 = 3
        while intentos2 > 0:
            pregunta = input("Me puedes romper sin tocarme, puedes decirme sin hablar. ¿Qué soy? ").strip().lower()
            
            if pregunta == respuesta_correcta2:
                print("🎉 ¡Correcto! Ganaste todo el juego 😎")
                break
            else:
                intentos2 -= 1
                print("❌ Incorrecto. Te quedan", intentos2, "intentos.\n"
    else:
        intentos -= 1
        print("❌ Incorrecto. Te quedan", intentos, "intentos.\n")

if intentos == 0:
    print("💀 Perdiste. La respuesta era:", respuesta_correcta)