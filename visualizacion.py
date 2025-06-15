import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def graficar_evolucion_fitness(historial_fitness, guardar_como='fitness.png'):
    plt.figure(figsize=(10, 5))
    plt.plot(historial_fitness, marker='o', color='green')
    plt.title("Evolución del fitness por generación")
    plt.xlabel('Generación')
    plt.ylabel('Fitness')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(guardar_como)
    plt.close()

def graficar_histograma_notas(asignaciones, notas, titulo='Distribución de Notas por Examen'):
    plt.figure(figsize=(10, 6))
    for examen, color in zip(['A', 'B', 'C'], ['#1f77b4', '#2ca02c', '#d62728']):
        notas_examen = [notas[i] for i in asignaciones[examen]]
        sns.histplot(notas_examen, kde=False, bins=10, label=f'Examen {examen}', color=color, alpha=0.6)

    plt.title("Distribución de notas por examen")
    plt.xlabel("Nota")
    plt.ylabel("Frecuencia")
    plt.legend()
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


