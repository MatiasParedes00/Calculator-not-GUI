import functions as fun
import decorators as deco
import sys

while True:
    deco.decorator1 ("Ingrese la clave:")
    print ("1) Operacion de un solo operando")
    print ("2) Operacion de dos operandos")
    deco.decorator2 ("3) Salir")
    inp = input(": ")

    if inp == "1":
        deco.decorator1 ("Ingrese la clave:")
        print ("1) Logaritmo Natural")
        print ("2) Seno")
        print ("3) Coseno")
        print ("4) Tagente")
        print ("5) Cosecante")
        print ("6) Secante")
        print ("7) Cotagente")
        print ("8) Arcoseno")
        print ("9) Arco-coseno")
        print ("10) Arcotagente")
        deco.decorator2 ("11) Volver")
        inp = input(": ")
        
        if inp == "1":
            result = fun.single_input_command (fun.logaritmoNatural)
            deco.print_result (result)
            
        elif inp == "2":
            result = fun.single_input_command (fun.seno)
            deco.print_result (result)
            
        elif inp == "3":
            result = fun.single_input_command (fun.coseno)
            deco.print_result (result)
            
        elif inp == "4":
            result = fun.single_input_command (fun.tagente)
            deco.print_result (result)

        elif inp == "5":
            result = fun.single_input_command (fun.cosecante)
            deco.print_result (result)

        elif inp == "6":
            result = fun.single_input_command (fun.secante)
            deco.print_result (result)

        elif inp == "7":
            result = fun.single_input_command (fun.cotagente)
            deco.print_result (result)

        elif inp == "8":
            result = fun.single_input_command (fun.arcoseno)
            deco.print_result (result)

        elif inp == "9":
            result = fun.single_input_command (fun.arcocoseno)
            deco.print_result (result)

        elif inp == "10":
            result = fun.single_input_command (fun.arcotagente)
            deco.print_result (result)

        elif inp == "11":
            continue
        
        else:
            print("Clave Incorrecta")

    elif inp == "2":
        deco.decorator1 ("Ingrese la clave:")
        print ("1) Suma")
        print ("2) Resta")
        print ("3) Multiplicacion")
        print ("4) Division")
        print ("5) Exponenciacion")
        print ("6) Logaritmo")
        deco.decorator2 ("7) Volver")
        inp = input(": ")

        if inp == "1":
            result = fun.doble_input_command (fun.suma)
            deco.print_result (result)
            
        elif inp == "2":
            result = fun.doble_input_command (fun.resta)
            deco.print_result (result)
            
        elif inp == "3":
            result = fun.doble_input_command (fun.por)
            deco.print_result (result)
            
        elif inp == "4":
            result = fun.doble_input_command (fun.dividido)
            deco.print_result (result)

        elif inp == "5":
            result = fun.doble_input_command (fun.exponente)
            deco.print_result (result)

        elif inp == "6":
            result = fun.doble_input_command (fun.logaritmo)
            deco.print_result (result)

        elif inp == "7":
            continue

        else:
            print ("Clave Incorrecta\n")

    elif inp == "3":
        while True:
            inp = input("Estas seguro/a? (S/N): ")

            if inp == "S" or inp == "s":
                sys.exit(0)

            elif inp == "N" or inp == "n":
                break

            else:
                print ("Clave incorrecta\n")
                continue

    else:
        print ("Clave incorrecta\n")
        continue
