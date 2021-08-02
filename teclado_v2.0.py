import string as s





def mensaje_valido(mensaje):
    """Funcion para ingresar solo caracteres del alfabeto en minúsculas"""

    no_validos = s.digits+s.punctuation+s.ascii_uppercase
    caracter_inv = "Ha ingresado un caracter no válido, por favor ingrese solo letras minúsculas."
    
    while(True):
        
        if [(c, cs)  for c in mensaje for cs in no_validos if c == cs]:
            print (caracter_inv) 
            break   
        else:
            return list(mensaje)


def mapear_caracteres(mensaje):
    letras = [' ', ('a', 'b', 'c'), ('d', 'e', 'f'),('g', 'h', 'i'), ('j', 'k', 'l'), ('m', 'n', 'o'), ('p', 'q', 'r', 's'), ('t', 'u', 'v'), ('w', 'x', 'y', 'z') ]

    #if [(c, cs)  for c in lista for cs in letras if c == cs]:
    #    yield print(True)
    for letra in mensaje:
        print("letra en mensaje: ",letra)
        for  elemento in range(len(letras)):
            print("elemento: ",letras[elemento])
            for caracter in range(len(letras[elemento])):
                print("caracter: ",letras[elemento][caracter])

                if letra in letras[elemento][caracter]:
                    print("encontro: ",letras[elemento][caracter])
                    print(map(lambda caracter: caracter*len(letras[elemento])),letras[elemento])
                else:
                    print("no coincidencia")


print("\n\nTECLADO NUMERICO\n")
resultado =[]
while(True):
    msj=input("Ingrese un mensaje para codificar: ")
    resultado = mensaje_valido(msj)
    print(resultado)
    try:
        print(mapear_caracteres(resultado))
    except:
            continue