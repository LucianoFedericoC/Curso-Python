lista = []

primero = input("¿Desea cargar un alumno? (s/n) ")
while not (primero == 'S' or primero == 'N' or primero == 's' or primero == 'n' or primero == 'Si' or primero == 'No' or primero == 'si' or primero == 'no'):
    print("Por favor resnponda con si/no o s/n")
    primero = input("¿Desea cargar un alumno? (s/n)")
    
if primero == 'S' or primero == 's' or primero == 'Si' or primero == 'si' :
    apellido = str(input("Escriba el apellido: "))
    promedio = float(input("Escriba el promedio (ejemplo 5.0): "))
    if promedio >= 1 and promedio <= 10 : 
        lista.append(apellido)
        lista.append(promedio)

    
    print("Por favor escriba el promedio con un rango de 1 al 10")
    apellido = str(input("Escriba el apellido: "))
    promedio = float(input("Escriba el promedio: "))
    
    print(lista)

    