contador = 1

while contador <= 100:
    print("contador:",contador)
    contador += 1


contador1=int(input("ingrese un numero: "))

while contador1 <0:
    print(f"contador1:,{contador}")
    contador -= 1
    print("termino el contador")


while true:
    texto=input("escribe algo(o escribe ´salir´ para terminar):")
    if texto== "salir":
        break
    print("escribiste:",texto)