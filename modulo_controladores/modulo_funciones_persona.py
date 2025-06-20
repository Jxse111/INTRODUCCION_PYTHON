def esMayor(edad):
    if edad >= 18:
        print("Eres mayor de edad")
    elif edad < 18 and edad >= 1:
        print("Eres menor de edad")
    else: 
        raise Exception("Tu edad no puede ser 0")
try:
    esMayor()
except Exception as ex:
    print("ERROR:",ex) 