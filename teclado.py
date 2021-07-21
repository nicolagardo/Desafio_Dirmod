import string as s

num_2 = 'a', 'b', 'c'
num_3 = 'd', 'e', 'f'
num_4 = 'g', 'h', 'i'
num_5 = 'j', 'k', 'l'
num_6 = 'm', 'n', 'o'
num_7 = 'p', 'q', 'r', 's'
num_8 = 't', 'u', 'v'
num_9 = 'w', 'x', 'y', 'z'

codificado =[]

def mensaje_valido():
    no_validos = s.digits+s.punctuation+s.ascii_uppercase
    caracter_inv = "Ha ingresado un caracter no válido, por favor ingrese solo letras minúsculas."
    print("\n\nTECLADO NUMERICO\n")
    
    while(True):
        
        msj=input("Ingrese un mensaje para codificar: ")
        if [(c, cs)  for c in msj for cs in no_validos if c == cs]:
            print (caracter_inv)    
        else:
            return msj

def listar_mensaje(msj):
    return list(msj)



while(True):
    var = listar_mensaje(mensaje_valido())


    for l in var:
    
        if l in num_2:
            codificado.append('2'* (num_2.index(l)+1)) 
        elif l in num_3:
            codificado.append('3'* (num_3.index(l)+1))
        elif l in num_4:
            codificado.append('4'* (num_4.index(l)+1))
        elif l in num_5:
            codificado.append('5'* (num_5.index(l)+1))
        elif l in num_6:
            codificado.append('6'* (num_6.index(l)+1))
        elif l in num_7:
            codificado.append('7'* (num_7.index(l)+1))
        elif l in num_8:
            codificado.append('8'* (num_8.index(l)+1))
        elif l in num_9:
            codificado.append('9'* (num_9.index(l)+1))
        elif l == ' ':
            codificado.append('0')
       
    
    j=0
    lista_iguales=[]
    for numero in range(len(codificado)-1):
        j+=1
        if codificado[numero][0] in codificado[j]:
            lista_iguales.append(j)
                
      
    
    lista_nueva =[]
    for numero in lista_iguales:
        lista_nueva.append(numero + lista_iguales.index(numero))


    for numero in range(len(lista_nueva)):
        codificado.insert(lista_nueva[numero], ' ')

   
   
    cod = ''.join(codificado)
    print("Output: ",cod)
    
    codificado.clear()
    