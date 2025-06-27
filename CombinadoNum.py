from itertools import combinations

values = [
    48260, 183160, 25340, 40931, 3721, 91580, 36034, 5842, 22172, 3067, 4953, 297691, 261657, 1, 2, 11, 3916, 43076, 26673, 96400, 192800, 50800, 313349, 
]

valor_objeto = 39598

for r in range(2, 11):  # Itera sobre tamaños de combinación de 2 a 10
    sum_result = [combo for combo in combinations(values, r) if sum(combo) == valor_objeto]
    resta_result = [combo for combo in combinations(values, r) if any(abs(x - y) == valor_objeto for x in combo for y in combo if x != y)] 
    multiplicacion_result = [combo for combo in combinations(values, r) if any(x * y == valor_objeto for x in combo for y in combo if x != y)] 
    division_result = [combo for combo in combinations(values, r) if any(x / y == valor_objeto for x in combo for y in combo if y != 0 and x!=y)] 

    if sum_result:
        print(f"Suma {r}: {sum_result}")
    if resta_result:
        print(f"Resta {r}: {resta_result}")
    if multiplicacion_result:
        print(f"Multiplicación {r}: {multiplicacion_result}")
    if division_result:
        print(f"División {r}: {division_result}")

        
"""

# Suma objetivo
valor_objeto = 1908

# Tolerancia para manejar redondeos (1 unidad hacia arriba o hacia abajo)
tolerance = 1

# Buscar combinaciones cuya suma, descontando el 5%, se aproxime al valor_objeto
sum_result = [
    combo for combo in combinations(values, 2)
    if abs(sum(combo) * 0.95 - valor_objeto) <= tolerance
]

# Imprimir las combinaciones encontradas
print(sum_result)

"""