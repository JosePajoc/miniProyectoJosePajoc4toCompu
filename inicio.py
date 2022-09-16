from persona import persona
misContactos = []

def crearContacto():
    print("Creando contacto")


def main():
    op = 0
    while op != 7:
        print("--------------------AGENDA 2022-----------------------")
        print("1. Crear contacto")
        print("2. Buscar contacto")
        print("3. Ver contactos")
        print("4. Modificar contacto")
        print("5. Eliminar contacto")
        print("6. Crear reporte en HTML")
        print("7. Salir del programa\n\n")
        op = int(input("Ingrese el número de opción: "))
        if op == 1:
            numero = int(input("Ingrese el número de teléfono: "))
            nombre = input("Ingrese el nombre: ")
            direccion = input("Ingrese la dirección: ")
            crearContacto(numero, nombre, direccion)

#iniciar programa
main()