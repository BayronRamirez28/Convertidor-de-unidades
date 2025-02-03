from conversiones.longitud import(
    metros_a_kilometros, kilometros_a_metros,
    metros_a_millas, millas_a_metros,
    metros_a_pies, pies_a_metros
)

from conversiones.peso import kilogramos_a_libras, libras_a_kilogramos
from conversiones.temperatura import fahrenheit_a_celsius, celsius_a_fahrenheit

def main():
    print("Conversor de Unidades")
    print("1. Metros a Kilómetros")
    print("2. Kilómetros a Metros")
    print("3. Metros a Millas")
    print("4. Millas a Metros")
    print("5. Metros a Pies")
    print("6. Pies a Metros")
    print("7. Kilogramos a Libras")
    print("8. Libras a Kilogramos")
    print("9. Celsius a Fahrenheit")
    print("10. Fahrenheit a Celsius")

    choice = input("Seleccione una opciń (1-10): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        value = float(input("Ingresa el valor a convertir: "))
        
        if choice == '1':
            print(f"{value} metros son {metros_a_kilometros(value)} kilómetros")
        elif choice == '2':
            print(f"{value} kilómetros son {kilometros_a_metros(value)} metros")
        elif choice == '3':
            print(f"{value} metros son {metros_a_millas(value)} millas")
        elif choice == '4':
            print(f"{value} millas son {millas_a_metros(value)} metros")
        elif choice == '5':
            print(f"{value} metros son {metros_a_pies(value)} pies")
        elif choice == '6':
            print(f"{value} pies son {pies_a_metros(value)} metros")
    elif choice in ['7', '8']:
        value = float(input("Ingresa el valor a convertir: "))
        
        if choice == '7':
            print(f"{value} kilogramos son {kilogramos_a_libras(value)} libras")
        elif choice == '8':
            print(f"{value} libras son {libras_a_kilogramos(value)} kilogramos")
    elif choice in ['9', '10']:
        value = float(input("Ingresa el valor a convertir: "))
        
        if choice == '9':
            print(f"{value} grados Celsius son {celsius_a_fahrenheit(value)} grados Fahrenheit")
        elif choice == '10':
            print(f"{value} grados Fahrenheit son {fahrenheit_a_celsius(value)} grados Celsius")
    else:
        print("Opción no válida. Por favor selecciona una opción del 1 al 10.")

if __name__ == "__main__":
    main()