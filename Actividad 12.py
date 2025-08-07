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

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[1]["repartidos"] < pivote[1]["repartidos"]]
        iguales = [x for x in lista if x[1]["repartidos"] == pivote[1]["repartidos"]]
        mayores = [x for x in lista[1:] if x[1]["repartidos"] > pivote[1]["repartidos"]]
        return quick_sort(mayores) + iguales + quick_sort(menores)

def mostrarRepartidores():
    if repartidores:
        print("\n= = = = = Registro Original = = = = =")
        for clave, datos in repartidores.items():
            print(f"Nombre: {clave} Paquetes Entregados: {datos['repartidos']} Zona: {datos['zona']}\n")
        print("\n= = = = = Ranking = = = = =")
        lista = list(repartidores.items())
        ordenado = quick_sort(lista)
        ordenadoD = dict(ordenado)
        for clave2, datos2 in ordenadoD.items():
            print(f"Nombre: {clave2} Paquetes Entregados: {datos2['repartidos']} Zona: {datos2['zona']}\n")
    else:
        print("No hay repartidores registrados")

def busqueda_secuencial(lista, busqueda):
    for j in range(len(lista)):
        if lista[j] == busqueda:
            return j
    return -1

def buscarRepartidor():
    if repartidores:
        buscar = input("Ingrese el nombre de un repartidor: ")
        b = busqueda_secuencial(list(repartidores.keys()), buscar)
        if b != -1:
            print(f"{buscar} entregó {repartidores[buscar]['repartidos']} paquetes")
        else:
            print("No existe")
    else:
        print("No hay repartidores registrados")

def main():
    while True:
        try:
            menu()
            op = int(input("Selecciona una opcion: "))
            match op:
                case 1:
                    ingreso()
                case 2:
                    mostrarRepartidores()
                case 3:
                    buscarRepartidor()
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