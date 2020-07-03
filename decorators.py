def decorator1 (text):
    print ("=" * len (text))
    print (text)

def decorator2 (text):
    print (text)
    print ("=" * len (text))

def print_result (result):
    if result:
        print (str(result) + "\n")
    elif result != False:
        print ("\nUno de lo operandos esta fuera de rango.")
