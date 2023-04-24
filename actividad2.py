a = int(input("Ingresa un numero: "))
b = int(input("Ingrese otro numero: "))

c = a // b
r = a & b

if a >= b:
    print("no se puede imprimir la serie")
else:
    while a<= b:
        print(a)
        a +=7