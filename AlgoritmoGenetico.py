# importar librerias
import pygad  # libreria para algoritmos geneticos
import numpy  # libreria para operaciones matematicas


inputs = [0.4, 1, 0.7, 8]  # arreglo de entradas para la red neuronal
desired_output = 32  # salida deseada para la red neuronal


# funcion de fitness con dos parametros de entrada
def fitness_func(solution, solution_idx):
    # salida de la red neuronal en donde se multiplica la solucion por las entradas
    output = numpy.sum(solution*inputs)
    # calculo de la funcion de fitness con la salida de la red neuronal
    fitness = 1.0 / (numpy.abs(output - desired_output) + 0.000001)
    return fitness  # retorno de la funcion de fitness


# configuracion del algoritmo genetico
ga_instance = pygad.GA(num_generations=100,  # numero de generaciones
                       sol_per_pop=10,  # numero de soluciones por poblacion
                       num_genes=len(inputs),  # numero de genes por solucion
                       num_parents_mating=2,  # numero de padres por generacion
                       fitness_func=fitness_func,  # funcion de fitness
                       mutation_type="random",  # tipo de mutacion
                       mutation_probability=0.6)  # probabilidad de mutacion
ga_instance.run()  # ejecucion del algoritmo genetico
ga_instance.plot_fitness()  # grafica de la funcion de fitness

# 1. ¿Si ejecuto el código varias veces se obtiene la misma respuesta?
# No, debido a que el algoritmo genetico es un algoritmo probabilistico
# 2. ¿La función fitness_func() declarada sirve problemas generales o específico(s)?
# Sirve para problemas especificos, ya que la funcion de fitness se calcula con la salida de la red neuronal
#3. ¿Qué representa en el código la variable fitness?
# Representa el valor de la funcion de fitness
# 4. ¿Qué podemos observar en el gráfico generado por plot_fitness?
# Podemos observar la evolucion de la funcion de fitness en cada generacion
#5. ¿Aproximadamente en cuantas generaciones deja de mejorar el fitness?
# En la generacion 50
