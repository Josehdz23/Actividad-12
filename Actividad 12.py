repartidores = {}
def menu():
    print("\n===== Control de Entregas =====\n1. Ingreso de repartidores\n2. Ordenamiento por paquetes\n3. Busqueda de repartidor\n4. Estadisticas\n5. Salir")

def ingreso():
    while True:
        try:
            NoRepartidores = int(input("Ingrese cuántos repartidores participaron: "))
            for i in range(NoRepartidores):
                print(f"\nRepartidor {i+1}: ")
                while True:
                    nombre = input("Ingrese nombre: ")
                    if nombre in repartidores:
                        print(f"El nombre ({nombre}) ya existe, reintente")
                    else:
                        if nombre or nombre.isspace():
                            break
                        else:
                            print("El nombre no es válido")
                while True:
                    try:
                        cantidad = int(input("Ingrese cantidad de paquetes entregados: "))
                        if cantidad > 0:
                            break
                        else:
                            print("No se permiten cantidades negativas, reintente")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
                while True:
                    zona = input("Ingrese la zona (Norte, Sur, Este, Oeste): ").upper()
                    if ((zona == "NORTE") or (zona == "SUR")) or ((zona == "ESTE") or (zona == "OESTE")):
                        break
                    else:
                        print("La zona ingresada no es válida")
                repartidores[nombre] = {
                    "repartidos": cantidad,
                    "zona": zona
                }
                print("\nRepartidor guardado con exito")
            break
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")

def main():
    while True:
        try:
            menu()
            op = int(input("Selecciona una opcion: "))
            match op:
                case 1:
                    ingreso()
                case 2:
                    print("2")
                case 3:
                    print("3")
                case 4:
                    print("4")
                case 5:
                    print("5")
                    break
                case _:
                    print("Opcion invalida, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
main()