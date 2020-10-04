print("Simbolo del Zodiaco")
mes = int(input("Numero de mes de nacimiento: "))
dia = int(input("Numero de dia de nacimiento: "))
if mes == 12 or mes == 1: 
    if dia >= 22 and dia <= 31:
        print("Tu simbolo es Capricornio")
    if dia >= 1 and dia <= 20:
        print("Tu simbolo es Capricornio")
else:
    print("Error en lo datos ingresados")