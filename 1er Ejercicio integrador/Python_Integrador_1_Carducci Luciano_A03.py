print("¡Bienvenido!")
option = 0

animals = []


def CreateAnimals():
    registros = int(input("¿Cuántos registros desea agregar?: "))
    print("Usted agregará " + str(registros) + " animales")
    for i in range(registros):
        esp = input("Escriba la especie " + str(i) + ": ")
        pob = int(input("Escriba la población de la especie " + str(i) + ": "))
        if pob == 0:
            pob = "Extinto"
        elif pob < 10000:
            pob = "En vias de extincion"
        else:
            pob = "Fuera de peligro de extincion"
        ubi = input("Escriba la ubicación de la especie " + str(i) + ": ")
        animals.append({"especie": esp, "poblacion": pob, "ubicacion": ubi})
    return animals


def ConsultAnimals():
    return animals


while option != 3:
    print("Eliga una de las siguientes optiones")
    print("1: Ingresar registro de animals")
    print("2: consultar registro de animals cargados")
    print("3: salir del programa")
    option = input("Opción: ")
    if int(option) == 1:
        CreateAnimals()
    elif int(option) == 2:
        if len(animals):
            print(ConsultAnimals())
        else:
            print("La lista esta vacía")
    elif int(option) == 3:
        print("Muchas gracias por utilizar nuestro servicio")
        break
    else:
        print("La opción elegida no es valida")
