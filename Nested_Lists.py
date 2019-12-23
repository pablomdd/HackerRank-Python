calificaciones = []
puntajes = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    calificaciones.append([name, score])
    puntajes.append(score)

segundo_mas_bajo = sorted(list(dict.fromkeys(puntajes)))[1]

for nombre, cali in sorted(calificaciones):
    if cali == segundo_mas_bajo:
        print(nombre)
