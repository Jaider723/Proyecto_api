from api.importar_datos import get_datos
from ui.imprimir_datos import imprimir_tabla

def main():
    
    departamento = input("Ingrese el departamento: ").upper()
    municipio = input("Ingrese el municipio: ").upper()
    cultivo = input("Ingrese el cultivo: ").capitalize()
    datos = get_datos(departamento, municipio, cultivo)
    if datos.empty:
        print("\nNo se encontraron datos.")
    else:
        print("")
        imprimir_tabla(datos)
    
main()
