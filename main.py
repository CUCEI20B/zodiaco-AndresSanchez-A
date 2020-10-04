print("Simbolo del Zodiaco")
dia = int(input("Numero de dia de nacimiento: "))
mes = int(input("Numero de mes de nacimiento: "))
if mes == 12: 
    if dia >= 1 and dia <= 21:
        print("Tu simbolo es sagitario")
    if dia >= 22 and dia <= 31:
        print("Tu simbolo es capricornio")
elif mes == 1: 
    if dia >= 1 and dia <= 20:
        print("Tu simbolo es capricornio")
    if dia >= 21 and dia <= 31:
        print("Tu simbolo es acuario")
elif mes == 2: 
    if dia >= 1 and dia <= 18:
        print("Tu simbolo es acuario")
    if dia >= 19 and dia <= 28:
        print("Tu simbolo es piscis")
elif mes == 3: 
    if dia >= 1 and dia <= 20:
        print("Tu simbolo es piscis")
    if dia >= 21 and dia <= 31:
        print("Tu simbolo es aries")
elif mes == 4: 
    if dia >= 1 and dia <= 20:
        print("Tu simbolo es aries")
    if dia >= 21 and dia <= 30:
        print("Tu simbolo es tauro")
elif mes == 5: 
    if dia >= 1 and dia <= 20:
        print("Tu simbolo es tauro")
    if dia >= 21 and dia <= 30:
        print("Tu simbolo es geminis")
elif mes == 6: 
    if dia >= 1 and dia <= 21:
        print("Tu simbolo es geminis")
    if dia >= 22 and dia <= 30:
        print("Tu simbolo es cancer")
elif mes == 7: 
    if dia >= 1 and dia <= 22:
        print("Tu simbolo es cancer")
    if dia >= 23 and dia <= 31:
        print("Tu simbolo es leo")
elif mes == 8: 
    if dia >= 1 and dia <= 22:
        print("Tu simbolo es leo")
    if dia >= 23 and dia <= 31:
        print("Tu simbolo es virgo")
elif mes == 9: 
    if dia >= 1 and dia <= 22:
        print("Tu simbolo es virgo")
    if dia >= 23 and dia <= 30:
        print("Tu simbolo es libra")
elif mes == 10: 
    if dia >= 1 and dia <= 22:
        print("Tu simbolo es libra")
    if dia >= 23 and dia <= 31:
        print("Tu simbolo es escorpio")
elif mes == 11: 
    if dia >= 1 and dia <= 22:
        print("Tu simbolo es escorpio")
    if dia >= 23 and dia <= 30:
        print("Tu simbolo es sagitario")
else:
    print("Error en lo datos ingresados")