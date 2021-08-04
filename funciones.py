
def mensaje_valido(mensaje):
    """Funcion para ingresar solo caracteres del alfabeto en minúsculas"""
    import string as s

    no_validos = s.digits+s.punctuation+s.ascii_uppercase
    caracter_inv = "Ha ingresado un caracter no válido, por favor ingrese solo letras minúsculas."
    
    while(True):
        
        if [(c, cs)  for c in mensaje for cs in no_validos if c == cs]:
            print (caracter_inv) 
            break   
        else:
            return list(mensaje)
