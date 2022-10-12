print("Nombre")
Nombre = input()
print("Ciudad")
Ciudad = input()
print("Año de nacimiento")
Nacimiento = input()
print("Nombre de tu Mascota")
Mascota = input()

edad = 2022 - int(Nacimiento)

print("Mensaje: ")
print(f"Hola {Nombre}, tu edad es de {edad}. Que lindo {Ciudad} !, ¡Espero que {Mascota} esté muy bien!")

tupla = (Nombre, Ciudad, edad, Mascota)
print(f"La tupla es {tupla}")
print(f"la cantidad de elementos en esta tupla es de {len(tupla)}")
print(f"Edad esta en la posición {tupla.index(edad)} de ésta tupla")

tuplaA = ("Martin", 32, "Moncho"), ("Alejandro", 28, "Rayo"), ("Javier", 34, "Rosa")
print(f"El segundo valor de la 3er tupla es {tuplaA[2][1]}")