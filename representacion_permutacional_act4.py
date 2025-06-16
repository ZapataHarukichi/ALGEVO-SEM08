import random
import numpy as np
import pandas as pd

df = pd.read_csv('notas_1u.csv')
alumnos = df['Alumno'].tolist()
notas = df['Nota'].tolist()

def crear_cromosoma():
    cromosoma = list(range(39))
    random.shuffle(cromosoma)
    return cromosoma

def decodificar_cromosoma(cromosoma):
    asignaciones = {
        'A': cromosoma[0: 13],
        'B': cromosoma[13: 26],
        'C': cromosoma[26: 39]
    }
    return asignaciones


def calcular_fitness(cromosoma):
    asignaciones = decodificar_cromosoma(cromosoma)
    bajo_rendimiento = [i for i, nota in enumerate(notas) if nota < 11]

    conteos = {'A': 0, 'B': 0, 'C': 0}
    for alumno in bajo_rendimiento:
        for grupo in ['A', 'B', 'C']:
            if alumno in asignaciones[grupo]:
                conteos[grupo] += 1
                break
    
    if any(conteo == len(bajo_rendimiento) for conteo in conteos.values()):
        return -1000 #penalización fuerte

    promedios = []
    for grupo in ['A', 'B', 'C']:
        notas_grupo = [notas[i] for i in asignaciones[grupo]]
        promedios.append(np.mean(notas_grupo))

    return -np.std(promedios)


def mutacion_swap(cromosoma): #???
    cromosoma_mutado = cromosoma.copy()
    i, j = random.sample(range(39), 2)
    cromosoma_mutado[i], cromosoma_mutado[j] = cromosoma_mutado[j], cromosoma_mutado[i]
    return cromosoma_mutado

    

def algoritmo_genetico(generaciones=100, tam_poblacion=50):
    poblacion = [crear_cromosoma() for _ in range(tam_poblacion)]
    mejor_fitness = float('-inf')
    mejor_cromosoma = None
    
    historial_fitness = []
    for gen in range(generaciones):
        fitness_scores = [(c, calcular_fitness(c)) for c in poblacion]
        fitness_scores.sort(key =lambda x: x[1], reverse=True) #???

        historial_fitness.append(fitness_scores[0][1])
        if fitness_scores[0][1] > mejor_fitness:
            mejor_fitness = fitness_scores[0][1]
            mejor_cromosoma = fitness_scores[0][0]

        nueva_poblacion = []
        elite = int(tam_poblacion * 0.2)
        nueva_poblacion.extend([x[0] for x in fitness_scores[:elite]]) #???

        while len(nueva_poblacion) < tam_poblacion:
            padre = random.choice(fitness_scores[:tam_poblacion//2])[0] #???
            hijo = mutacion_swap(padre)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

        if gen % 20 == 0:
            print(f"Generacion {gen}: Mejor fitness = {fitness_scores[0][1]:.4f}")

    return mejor_cromosoma, historial_fitness

# Ejecución
print("REPRESENTACIÓN PERMUTACIONAL")
print("Cromosoma: Permutación de 39 alumnos")
print("Examen A = pos 0–12 | B = 13–25 | C = 26–38\n")

mejor_soluc, historial_fitness = algoritmo_genetico()
asignaciones_finales = decodificar_cromosoma(mejor_soluc)

print("\nDistribución final:")
for examen in ['A', 'B', 'C']:
    indices = asignaciones_finales[examen]
    notas_examen = [notas[i] for i in indices]
    promedio = np.mean(notas_examen)
    print(f"Examen {examen}: {len(indices)} alumnos, promedio = {promedio:.2f}")
    print(f"Alumnos: {[alumnos[i] for i in indices[:5]]} ...")

print("\nAnálisis final: ")
promedios = []
for examen in ['A', 'B', 'C']:
    notas_examen = [notas[i] for i in asignaciones_finales[examen]]
    promedios.append(np.mean(notas_examen))

print(f"Desviación estándar entre promedios: {np.std(promedios):.4f}")


import visualizacion
visualizacion.graficar_evolucion_fitness(historial_fitness, guardar_como='fitness_repre_permutacional.png')
visualizacion.graficar_histograma_notas(asignaciones_finales, notas, guardar_como='notas_repre_permutacional.png')

