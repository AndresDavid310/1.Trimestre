num1=int(input("ingrese un numero: "))
num2=int(input("ingrese otro numero: "))

oper=num1 * num2

if oper >50:
    print("el numero es mayor a 50")
    
elif oper <=49:
    print("el numero es menor de 50")
    
elif oper == 50:
    print("el numero es igual a 50")
    
else:
    print("no cumple la condicion")