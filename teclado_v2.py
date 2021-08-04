from funciones import mensaje_valido





def mapear_caracteres(mensaje):
    letras = [' ', ('a', 'b', 'c'), ('d', 'e', 'f'),('g', 'h', 'i'), ('j', 'k', 'l'), ('m', 'n', 'o'), ('p', 'q', 'r', 's'), ('t', 'u', 'v'), ('w', 'x', 'y', 'z') ]
    print("....")
    print(next((i for i, x in enumerate(letras) if x[0] == "a"), None))
    print(list(filter(lambda item: item == ' ', letras)))
    codificadov2 = []
    if [(c, cs)  for c in mensaje for cs in letras if c in cs]:
            print ("hola") 
            codificadov2.append(letras)
            print(codificadov2)
    else:
        pass

    for letra in mensaje:
        print("letra en mensaje: ",letra)
        for  elemento in range(len(letras)):
            print("elemento: ",letras[elemento])
            for caracter in range(len(letras[elemento])):
                print("caracter: ",letras[elemento][caracter])

                if letra in letras[elemento][caracter]:
                    print("encontro: ",letras[elemento][caracter])
                    indice = [elemento][caracter]
                    print("prueba: ", indice)
                    #print(map(lambda caracter: caracter*len(letras[elemento])),letras[elemento])
                    
                    print("indice: ",[elemento][caracter])
                    print("este: ",letras.index(letra))
                else:
                    print("no coincidencia")
    #letra, elemento, caracter for letra in  mensaje


print("\n\nTECLADO NUMERICO\n")
resultado =[]
while(True):
    msj=input("Ingrese un mensaje para codificar: ")
    resultado = mensaje_valido(msj)
    print(resultado)
    #diccionario_letras = {'2': ['a','b','c']}
    
    try:
        print(mapear_caracteres(resultado))
    except:
            continue
        
 
    

