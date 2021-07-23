import string as s

letras = [' ', ('a', 'b', 'c'), ('d', 'e', 'f'),('g', 'h', 'i'), ('j', 'k', 'l'), ('m', 'n', 'o'), ('p', 'q', 'r', 's'), ('t', 'u', 'v'), ('w', 'x', 'y', 'z') ]




def mensaje_valido(mensaje):

    no_validos = s.digits+s.punctuation+s.ascii_uppercase
    caracter_inv = "Ha ingresado un caracter no válido, por favor ingrese solo letras minúsculas."
    
    while(True):
        
        if [(c, cs)  for c in mensaje for cs in no_validos if c == cs]:
            print (caracter_inv) 
            break   
        else:
            return list(mensaje)
def mapear_caracteres(lista):
    pass


print("\n\nTECLADO NUMERICO\n")
    
while(True):
    msj=input("Ingrese un mensaje para codificar: ")
    resultado = mensaje_valido(msj)
    print(resultado)
