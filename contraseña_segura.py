CAR_ESP = ("*","-","_","$","&","~")

print('''
Introduzca una contraseña que contenga entre 8 y 16 caracteres. 
Debe contener minimamente una mayuscula y un caracter especial (*-_$&~)
''')

def longitud_contraseña(contraseña):
    longitud_valido = False
    if len(contraseña) >= 8 and len(contraseña) <= 16:
        longitud_valido = True

    return longitud_valido

def contiene_mayusculas(contraseña):
    valido_mayusculas = False
    for letra in contraseña:
        if letra.isupper():
            valido_mayusculas = True

    return valido_mayusculas

def contiene_caracter_especial(contraseña):
    caracter_valido = False

    for letra in contraseña:
        if letra in CAR_ESP:
            caracter_valido = True
    
    return caracter_valido

def main():
    contraseña_valida = False
    while contraseña_valida != True:
        contraseña_usuario = input()

        longitud = longitud_contraseña(contraseña_usuario)
        mayuscula = contiene_mayusculas(contraseña_usuario)
        caracter_especial = contiene_caracter_especial(contraseña_usuario)

        if longitud != True:
            print("La longitud de la contraseña es invalida.")
            print("Introduzca otra contraseña")
        elif mayuscula != True:
            print("Necesita introducir minimamente una mayuscula")
            print("Introduzca otra contraseña")
        elif caracter_especial != True:
            print("No contiene ningun caracter especial")
            print("Introduzca otra contraseña")
        else:
            print("La contraseña es valida y segura")
            contraseña_valida = True

main()

    

