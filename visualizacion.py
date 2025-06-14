import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def graficar_evolucion_fitness(historial_fitness, titulo='Evolución del Fitness'):
    plt.figure(figsize=(10, 5))
    plt.plot(historial_fitness, marker='o', color='green')
    plt.title(titulo)
    plt.xlabel('Generación')
    plt.ylabel('Fitness')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def graficar_histograma_notas(asignaciones, notas, titulo='Distribución de Notas por Examen'):
    datos = []
    for grupo, indices in asignaciones.items():
        for i in indices:
            datos.append({'Examen': grupo, 'Nota': notas[i]})

    df_notas = sns.load_dataset("tips")  # solo para asegurar que seaborn está bien cargado (evita errores)
    plt.figure(figsize=(10, 6))
    sns.histplot(data=datos, x='Nota', hue='Examen', multiple='stack', palette='Set2', bins=10)
    plt.title(titulo)
    plt.xlabel('Nota')
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.show()

def comparar_representaciones(stats):
    # stats debe ser una lista de tuplas: [(label, lista_notas_A, lista_notas_B, lista_notas_C), ...]
    plt.figure(figsize=(12, 6))

    for i, (label, notas_A, notas_B, notas_C) in enumerate(stats):
        plt.subplot(1, len(stats), i + 1)
        sns.boxplot(data=[notas_A, notas_B, notas_C], palette='Set3')
        plt.xticks([0, 1, 2], ['A', 'B', 'C'])
        plt.title(label)
        plt.ylabel('Nota')
        plt.ylim(0, 20)

    plt.tight_layout()
    plt.show()

