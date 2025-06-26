# print("Ejercicio1")

# total=0
# num1=int(input("ingrese un numero(0 para terminar) "))
# while num1 != 0 :
#     total += num1
#     num1 =int(input("ingrese otro numero(0 para terminar): "))
    
# print("la suma total es:",total)

# print("Ejercicio2")

# contraseña=input("Escribe la contraseña:")

# while contraseña !="andres123":
#     print("contraseña incorrecta")
#     contraseña=input("intente de nuevo: ")
# print("Acceso concedido")


# print("Ejercico3")

# lista=[]

# pro=input("ingrese un producto: ")

# while pro.lower() !="fin":
#     lista.append(pro)
#     producto=input("ingrese el seguiente producto: ")
#     pro=producto
# print("lista de productos:", lista)


print("Ejercicio4")

contador=0
pares=0
impares=0

while contador < 10:
    num = int(input("ingrese un numero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1
print(f"pares: {pares} impares: {impares}")

print("Ejercicio5")

lista=[]
nota=int(input("ingrese una nota: "))

while  nota != "salir"
nota=lista
    if nota <=0 or nota > 10:
        lista.append(nota)