import math as mt

#Algunas funciones lambdas para acortar el código posterior
suma = lambda a, b: a + b
resta = lambda a, b: a - b
por = lambda a, b: a * b
dividido = lambda a, b: a / b if b != 0 else None
exponente = lambda a, b: a ** b

logaritmo = lambda a, b: mt.log(a, b) if b > 0 else None
logaritmoNatural = lambda a: mt.log(a)

seno = lambda a: mt.sin(a)
coseno = lambda a: mt.cos(a)
tagente = lambda a: seno(a) / coseno(a) if coseno(a) != 0 else None

cosecante = lambda a: 1 / seno(a) if seno(a) !=0 else None
secante = lambda a: 1 / coseno(a) if coseno(a) !=0 else None
cotagente = lambda a: coseno(a) / seno(a) if seno(a) != 0 else None

arcotagente = lambda a: mt.atan(a)
arcocoseno = lambda a: mt.acos(a) if a < 1 and -1 < a else None
arcoseno = lambda a: mt.asin(a) if a < 1 and -1 < a else None

def single_input_command (operator):
    inp = input("Ingrese el numero: ")
    try:
        inp = float(inp)
        return operator (inp)
    except ValueError:
        print ("\nAlgo que ingresaste no es aceptado como valor numerico")
        print ("Por favor, revise lo que ingresaste")
        return False
    
def doble_input_command (operator):
    inp1 = input("Ingrese el primer numero: ")
    inp2 = input("Ingrese el segundo numero: ")
    try:
        inp1 = float(inp1)
        inp2 = float(inp2)
        return operator (inp1, inp2)
    except ValueError:
        print ("Algo que ingresaste no es aceptado como valor numerico")
        print ("Por favor, revise lo que ingresaste")
        return None
