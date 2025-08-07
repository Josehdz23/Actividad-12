def menu():
    print("")
def ingreso():
    print("")

def main():
    while True:
        try:
            menu()
            op = int(input("Selecciona una opcion: "))
            match op:
                case 1:
                    print("1")
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