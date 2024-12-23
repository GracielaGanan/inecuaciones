def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para calcular el MCD de más de dos números
def mcd_multiple(*args):
    result = args[0]
    for num in args[1:]:
        result = mcd(result, num)
    return result

# Entrada de datos
numeros = list(map(int, input("Introduce dos o más números naturales separados por espacios: ").split()))

# Calcular y mostrar el MCD
resultado = mcd_multiple(*numeros)
print(f"El MCD de los números {numeros} es: {resultado}")

