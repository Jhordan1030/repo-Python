def crear_usuario():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu Apellido: ")
    edad = int(input("Ingresa tu edad: "))

    if edad >= 18:
        print("Cuenta creada")
        saldo = float(input("Ingrese su saldo: "))
        print("Nombre: ", nombre,
        "\nApellido: ", apellido ,
          "\nEdad: ", edad , "\nSaldo: ", saldo)
        
        
        return saldo
    else:
        print("Cuenta no creada por que eres menor de edad")
        return None
    
        
    
def menu():
    print("Menu de opciones")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Salir / Finalizar")

def Depositar(saldo):
    depositar = float(input("Valor a Depsitar: "))
    saldo += depositar
    print("Depositaste: " , depositar ,
          "\nTu saldo es: " , saldo)
    return saldo

def Retirar(saldo):
    retirar = float(input("Cuanto desea retirar: "))
    saldo -= retirar
    print("Retiraste: " , retirar ,
          "\nTu saldo es: " , saldo)
    return saldo


saldo = crear_usuario()
crear_usuario
while True:
    menu()
    opcion =input("Elija una opcio (1, 2, 3): ")

    if opcion == '1':
        Depositar(saldo)
    elif opcion == '2':
        Retirar(saldo)
    elif opcion == '3':
        print("Saliendo del cajero....")
        break
    else:
        print("Opcion no validad. Vuelva a escoger")