# print("condicionales y operaciones")
# print("ejercicio1")

# num=int(input("ingrese un numero por favor: "))

# if num <0: 
#     print("es negativo")
    
# elif num >0:
#     print("es positivo")
    
# else:
#     print("ingrese de nuevo el numero")

# print("ejercicio2")

# num1=int(input("ingrese un numero: "))
# num2=int(input("ingrese otro por favor: "))

# if num1 <num2:
#     print ("es menor que el 2 numero")
    
# elif num2 >num1:
#     print("es meyor que el primer numero")
    
# else:
#     ("ingrese de nuevo el numero")

# print("ejercicio3")

# num3=int(input("ingrese un numero: "))

# if num3 %2==0:
#     print("es par")
    
# elif num3 %2==1:
#     print(" es impar")
    
# else:
#     print("ingrese de nuevo el numero")


# print("Ejercicio4")

# num4=int(input("ingrese un numero: "))

# if num4 <=9:
#     print("no se encuentra del 10 al 20")
    
# elif num4 >=10:
#     print("si se encuentra entre del 10 al 20")
    
# elif num4 >=21:
#     print("no se encuentra de el 10 al 20")
    
# else:
#     print("ingrese de nuevo el numero")


# print("Ejercicio5")

# num5=int(input("ingrese un numero: "))
# num55=int(input("ingrese un segundo numero: "))
# num555=int(input("ingrese un tercer numero: "))

# if num5 >= num55 and num5 >= num555:
#     print("es mayor",num5)
    
# elif num55 >=num5 and num55 >= num555:
#     print("es mayor",num55)
    
# else:
#     print("es mayor el",num555)


# print("Ejercicio6")

# precio=float(input("ingrese el precio final: "))

# if precio >100:
#     descuento= precio*0.10
#     preciofinal=precio-descuento
#     print("el totals supera los 100")
#     print(preciofinal)
# else:
#     print("no tiene descuento")


# print("Ejercicio7")

# edad=int(input("ingrese su edad: "))

# if edad >=18:
#     print("puedes votar")
    
# else:
#     print("no tienes la edad para votar")


# print("Ejercicio8")

# tipo=input("que tipo de cliente es vip o normal: ")
# preciototal=int(input("ingrese el precio total:"))

# if tipo == "vip":
#     descuento= preciototal*0.20
#     preciofinal= preciototal-descuento
#     print("el precio es de",preciofinal)
# else:
#     print("no tienes descuento")


# print("Ejercicio9")

# num6=int(input("ingrese un numero: "))

# if num6 % 5==0 and num6 % 3==0:
#     print("el numero es de 5 y de 3")
    
# else:
#     print("no es multiplo de 5 y de 3")


# print("Ejercicio10")

# num7=int(input("ingrese un numero: "))

# div1=int(input("ingrese un numero: "))
# div2=int(input("ingrese otro numero: "))

# if num7 % div1 == 0 and num7 % div2 ==0:
#     print("el numero",num7 ,"es divisible entre" ,div1 ,"y", div2 )
    
# else:
#     print("no es divisible para los 2 numeros")


# print("listan con condicionales")
# print("Ejercicio11")

# lista=[]

# numer1=int(input("ingrese un numero: "))
# numer2=int(input("ingrese un numero: "))
# numer3=int(input("ingrese un numero: "))
# numer4=int(input("ingrese un numero: "))
# numer5=int(input("ingrese un numero: "))

# lista=[numer1,numer2,numer3,numer4,numer5]

# if lista [2]>10:
#     print("mayor que 10")
    
# else:
#     print("es menor que 10")


# print("Ejercicio12")

# lista=[3,5,7,9]

# numer8=int(input("ingrese un numero: "))

# if numer8==7: 
#     print("adivinaste el numero")
    
# else:
#     print("no esta en lista")


# print("Ejercicio13")

# lista=[4,6,2,8]

# if lista[0] + lista[1] >10:
#     print("la suma es alta")

# elif lista[2]+lista[3] >10:
#     print("la suma es menor")

# elif lista[0] + lista[1] ==10: 
#     print("la suma es igual a 10")
    
# else:
#     print("la suma es menor o igual a 10")
    
    
# print("EJERCICIO14")

# lista=["Ana","luis","Pedro","Marta"]

# nom=lista[3]

# if nom == "Marta":
#     print("el nombre es Marta")
    
# else:
#     print("es otro nombre")
    
    
# print("Ejercicio15")

# color1=input("ingrese un color: ")
# color2=input("ingrese un color: ")
# color3=input("ingrese un color: ")

# lista=[color1,color2,color3]

# if lista[1]== "azul":
#     lista[1]="naranja"
#     print("el color numero 2 ha sido cambiado a", lista[1],"la lista actualizada:", lista)

# else:
#     print("la lista esta asi:", lista)



# print("Tuplas")
# print("Ejercicio16")


# tupla=(5, 8, 12, 20)

# if tupla[0]< tupla[-1]:
#     print("orden ascendente")
    
# else:
#     print("orden descendente")
    
    
# print("Ejercicio17")

# tupla2=(25, 32, 28)

# if tupla2[1] >30:
#     print("Edad mayor de 30")
    
# else:
#     print("edad menor o igual al 30")
    
    
# print("Ejercicio18")

# tupla3=(1, 2, 3)

# lista1=list(tupla3)

# if lista1[1] == 2:
#     lista1[1] = 10
#     tupla3=tuple(lista1)
#     print("la tupla actualizada queda de la siguiente manera:", tupla3,"cambiando el 2 por un 10")
# else:
#     print("lista no necesita actualizacion")


# print("Ejercicio19")

# tupla4=(4, 5)


# usuario2= {"nombre": "Lucía", "edad": 20}

# if usuario2["edad"]>18:
#     usuario2["edad"]=21
#     print("valor de la edad cambiado a 21",usuario2)
    
    
# else:
#     print(usuario2)
    
    
# print("Ejercicio23")

# diccionario={"nombre": "Carlos"}

# if "ciudad" not in diccionario:
#     diccionario["ciudad"] = "Bogotá"

# print(diccionario)


# print("Ejercicio24")

# diccionario2= {"producto": "pan", "precio": 1200}

# if "precio" in diccionario2:
# if tupla4[1] >5:
#     print("coordenada alta")
    
# else:
#     print("coordenada baja")
    
    
# print("Ejercicio20")


# tupla1 = (3, 4)
# tupla2 = (3, 5)

# if tupla1 == tupla2:
#     print("Tuplas iguales")
# else:
#     print("Tuplas diferentes")


# print("diccionarios")
# print("Ejercicio21")

# usuario={"nombre": "juan","edad":17}

# if usuario["edad"]>=18:
#     print("Adulto")
    
# else:
#     print("menor de edad")
    
    
# print("Ejercicio22")
#     print("el precio es de", diccionario2["precio"])
    
# else:
#     print("no hay disponible")


# print("Ejercicio25")

# diccionario3={"pan": 1200, "leche": 2000}

# if "pan" in diccionario3:
#     print("el precio del pan es de", diccionario3["pan"])
    
# else:
#     print("producto no disponible")