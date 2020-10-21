import re


def pedirNumeroEntero():

    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print("Error, introduce un numero entero")

    return num


salir = False
opcion = 0

while not salir:
    print ("_____________________EXPRESIONES REGULARES_____________________")
    print("1. Todas las palabras que tengan una longitud de 7 o más letras")
    print("2. Expresiones que NO finalicen con una vocal")
    print("3. Las palabras que inicien con “M” donde la segunda letra no sea vocal")
    print("4. Expresiones encerradas entre comillas")
    print("5. Ip´s")
    print("6. Horas")
    print("7. Telefonos")
    print("8. Correos electronicos")
    print("9. Url´s")
    print("10. Codigo postal")
    print("11. Salir")

    print("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        print("Todas las palabras que tengan una longitud de 7 o más letras")
        f = open(
            "ejemplo.txt"
        ).read()
        ExpReg = "[A-Za-z]{7,}"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion == 2:
        print("Expresiones que NO finalicen con una vocal")
        f = open(
            "ejemplo.txt"
        ).read()
        ExpReg = "[a-zA-Z]+[^aeiou]\s"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion == 3:
        print("Las palabras que inicien con “M” donde la segunda letra no sea vocal")
        f = open(
            "ejemplo.txt"
        ).read()
        ExpReg = "M[^aeiou][a-zA-Z]{1,}"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion == 4:
        print("Expresiones encerradas entre comillas")
        f = open(
            "ejemplo.txt"
        ).read()
        ExpReg = "(\".*?\"|'.*?')"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion == 5:
        print("Ip´s")
        f = open(
            "ejemplo.txt"
        ).read()
        ExpReg = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion == 6:
        print("Horas")
        f = open(
            "ejemplo.txt"
        ).read()
        ExpReg = "(?:[01]\d|2[0-3]):[0-5]\d"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion == 7:
        print("Telefonos")
        f = open(
            "ejemplo.txt"
        ).read()
        ExpReg = "\d[0-9]{7,10}"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion == 8:
        print("Correos Electronicos")
        f = open(
            "ejemplo.txt"
        ).read()
        ExpReg = "[a-zA-Z0-9.!#$%&'*+=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion == 9:
        print("Url´s")
        f = open(
            "ejemplo.txt"
        ).read()
        ExpReg = "https?:\/\/[\w\-]+\.[\w\-]+[#?]?.*"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)

    elif opcion == 10:
        print("Codigo Postal")
        f = open(
            "ejemplo.txt"
        ).read()
        ExpReg = "^(\d{5}$)"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion == 11:
        salir = True
    else:
        print("Introduce un numero entre 1 y 11")

print("Fin")
