

recursos = [
    ["Ana", 8, 8, 8, 8, 8],
    ["Luis", 9, 9, 9, 9, 9],
    ["Carlos", 6, 7, 7, 8, 6],
    ["Marta", 10, 10, 8, 9, 9]
]


def calcular_jornada(recurso):
    nombre = recurso[0]
    total = 0

    for i in range(1, len(recurso)):
        total += recurso[i]

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total, clasificacion



print("+----------+--------------+--------------------+")
print("| Nombre   | Total Horas  | Clasificación      |")
print("+----------+--------------+--------------------+")


for recurso in recursos:
    nombre, total, clasificacion = calcular_jornada(recurso)
    print(f"| {nombre:<8} | {total:<12} | {clasificacion:<18} |")


print("+----------+--------------+--------------------+")
