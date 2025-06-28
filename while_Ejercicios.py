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


# print("Ejercicio4")

# contador=0
# pares=0
# impares=0

# while contador < 10:
#     num = int(input("ingrese un numero: "))
#     if num % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     contador += 1
# print(f"pares: {pares} impares: {impares}")

# print("Ejercicio5")

# notas=[]
# calificacion=(input("ingrese la nota: "))
# while calificacion!="salir":
#     nota=float(calificacion)
#     if 0<=nota<=5:
#          notas.append(nota)
#          calificacion=(input("ingrese la nota: "))
#     else:
#         print(f"nota invalida")
#         calificacion=(input("ingrese la nota: "))
# if notas:
#     promedio= sum(notas) / len(notas)
#     print(f"la nota final es{promedio}")
# else:
#     (f"no es valido")
    
    
# print("Ejercicio6")

# numero=int(input("ingrese la tabla de multiplicar: "))

# contador=1

# while contador <=10:
#     resultado=numero*contador
#     print(f"{numero}*{contador}={resultado}")
#     contador +=1
        
        
# print("Ejercicio7")

# numero= 17
# while True:
#     num=int(input("intenta adivinar el numero: "))
#     if num==17:
#         print("¡Adivinaste!")
#         break
#     elif num <17:
#         print(f"el numero es mayor")
#     else:
#         print(f"El numero es menor")
        
        
print("Ejercicio8")

fruta=("manzana","piña","uva")
frutas=input("adivina la fruta: ")

while frutas not in fruta:
      print(" no adivinaste una de las 3 ")
      frutas=input("adivina la fruta: ")
print("adivinaste la fruta")
    