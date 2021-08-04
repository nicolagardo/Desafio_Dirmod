from funciones import mensaje_valido as mv
import string as s

alfabeto ={'0' : ' ', '2' : ['a', 'b', 'c'], '3' : ['d', 'e', 'f'], '4' : ['g', 'h', 'i'], '5' : ['j', 'k', 'l'],
'6' : ['m', 'n', 'o'], '7' : ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'],'9' : ['w', 'x', 'y', 'z']}

def obtener_clave(val):
    for clave, valor, in alfabeto.items():
        for elemento in range(len(valor)):
         if val == valor[elemento]:
             return clave #*(value.index(elemento) +1) 





print("\n\nTECLADO NUMERICO v3\n")
resultado =[]
lista = []
while(True):
    msj=input("Ingrese un mensaje para codificar: ")
    resultado = mv(msj)
    if resultado :
        break
    print(resultado)
for letra in resultado:
    print(obtener_clave(letra))
    
    lista.append(obtener_clave(letra))
print(lista)

"""en proceso"""