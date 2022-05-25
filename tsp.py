#DONE

from charles import Population, Individual
from data import distance_matrix
from copy import deepcopy
from selection import fps, tournament, ranking
from mutation import swap_mutation, inversion_mutation, insertion_mutation, displacement_mutation
from crossover import single_point_co, cycle_co, ordered_co
from operator import attrgetter
import pandas as pd
import statistics as st
import dataframe_image as dfi
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def get_fitness(self):
    """A simple objective function to calculate distances
    for the TSP problem.

    Returns:
        int: the total distance of the path
    """
    fitness = 0
    for i in range(len(self.representation)):
        fitness += distance_matrix[self.representation[i - 1]][self.representation[i]]
    return int(fitness)

#USELESS?
def get_neighbours(self):
    """A neighbourhood function for the TSP problem. Switches
    indexes around in pairs.

    Returns:
        list: a list of individuals
    """
    n = [deepcopy(self.representation) for i in range(len(self.representation) - 1)]

    for count, i in enumerate(n):
        i[count], i[count + 1] = i[count + 1], i[count]

    n = [Individual(i) for i in n]
    return n


# Monkey patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours

def build_table(gen_number=50, repeat=100, pop_size=100, optim=min, name="name"):
    """
    Build table to compare different configurations.

    Args:
        gen_number: the number of generations for evolve.
        repeat: number of repetitions for each configuration. most be above 30.
        pop_size: size of population.
        optim = min or max problem, write the function not the string.
        Note: the tsp problem is a min problem,
        but with changes to the fitness function it can become a max problem
        name = just the name of the file it exports, should be representative of the problem.
    Result:
        a table with the combination, the best outcome, the mean value and the standard deviation.
    """
    df = pd.DataFrame()
    for sel in [ranking, tournament]: #any selection methods wanted to test
        for cross in [cycle_co, ordered_co]: #any crossover methods wanted to test
            for mut in [inversion_mutation, displacement_mutation]: #any mutation methods wanted to test
                for elit in [True]: #True and/or False
                    record=[]
                    for i in range(repeat):
                        pop = Population(
                            size=pop_size,
                            sol_size=len(distance_matrix[0]),
                            valid_set=[i for i in range(len(distance_matrix[0]))],
                            replacement=False,
                            optim=optim.__name__,
                        )

                        pop.evolve(gens=gen_number, select=sel, crossover=cross, mutate=mut,
                            co_p=0.8, mu_p=0.2, elitism=elit)

                        fitnesses=[i.fitness for i in pop.individuals]
                        record.append(optim(fitnesses))
                    dict = {'select':sel.__name__, 'cross':cross.__name__, 'mut':mut.__name__, 'elit':elit,
                        'best result': optim(record), 'mean results': st.mean(record), 'std results': st.stdev(record)}
                    df = df.append(dict, ignore_index=True)
    print(df)
    dfi.export(df, name+".png")

#build_table(gen_number=50, repeat=100, pop_size=100, optim=min, name="ulysses16")
#build_table(gen_number=50, repeat=100, pop_size=100, optim=min, name="br17")
#build_table(gen_number=3000, repeat=30, pop_size=100, optim=min, name="eil76")
#build_table(gen_number=3000, repeat=30, pop_size=100, optim=min, name="ftv70")

def build_graph(gen_number=50, repeat=100, pop_size=100, optim=min, name="name"):
    """
    builds a graph comparing two configurations of operators.

    Args:
        gen_number: the number of generations for evolve.
        repeat: number of repetitions for each configuration. most be above 30.
        pop_size: size of population.
        optim = min or max problem, write the function not the string.
        Note: the tsp problem is a min problem,
        but with changes to the fitness function it can become a max problem
        name = just the name of the file it exports, should be representative of the problem.
    Result:
        graph with three lines in blue three lines in red,
        the center line representing the mean value of each generation,
        other lanes considering the standard deviation.
        first configuration in blue second configuration in red.
    """
    lista_0 = []
    lista_1 = []
    for i in range(repeat):
        for j in range(2):
            pop = Population(
            size=pop_size,
            sol_size=len(distance_matrix[0]),
            valid_set=[i for i in range(len(distance_matrix[0]))],
            replacement=False,
            optim=optim.__name__,
            )
            if j == 0:
                gen = pop.evolve(gens=gen_number, select=tournament, crossover=ordered_co, mutate=inversion_mutation,
                                   co_p=0.8, mu_p=0.2, elitism=True)
                #ITS IMPORTANT TO CHANGE THE CONFIGURATION TO COMPARE
                lista_0.append(gen)

            if j == 1:
                gen = pop.evolve(gens=gen_number, select=ranking, crossover=ordered_co, mutate=displacement_mutation,
                                   co_p=0.8, mu_p=0.2, elitism=True)
                #ITS IMPORTANT TO CHANGE THE CONFIGURATION TO COMPARE
                lista_1.append(gen)
    df_0 = pd.DataFrame(lista_0)
    df_1 = pd.DataFrame(lista_1)
    for i in df_0.columns:
        df_0[i] = pd.to_numeric(df_0[i])
    for i in df_1.columns:
        df_1[i] = pd.to_numeric(df_1[i])
    plt.plot(df_0.mean(axis=0), color='blue')
    plt.plot(df_0.mean(axis=0)+df_0.std(axis=0), color='blue', linestyle='dashed')
    plt.plot(df_0.mean(axis=0)-df_0.std(axis=0), color='blue', linestyle='dashed')
    plt.plot(df_1.mean(axis=0), color='red')
    plt.plot(df_1.mean(axis=0)+df_1.std(axis=0), color='red', linestyle='dashed')
    plt.plot(df_1.mean(axis=0)-df_1.std(axis=0), color='red', linestyle='dashed')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title(name, size=15)
    plt.savefig(name+'_compare.png')
    plt.show()

#build_graph(3000, 30, 100, min, "ftv70")

def graph (gen_number=50, pop_size=100, optim=min, name="name"):
    """
        builds a graph of the GA algorithm.

        Args:
            gen_number: the number of generations for evolve.
            pop_size: size of population.
            optim = min or max problem, write the function not the string.
            Note: the tsp problem is a min problem,
            but with changes to the fitness function it can become a max problem
            name = just the name of the file it exports, should be representative of the problem.
        Result:
            graph with the best individual of the population for each generation.
        """
    pop = Population(
        size=pop_size,
        sol_size=len(distance_matrix[0]),
        valid_set=[i for i in range(len(distance_matrix[0]))],
        replacement=False,
        optim=optim.__name__,
    )

    fitness = pop.evolve(gens=gen_number, select=fps, crossover=cycle_co, mutate=swap_mutation,
                     co_p=0.8, mu_p=0.2, elitism=True)
    #IMPORTANT TO CHANGE THE CONFIGURATION

    fig, axes = plt.subplots(1, 1)
    axes.plot(fitness.keys(), fitness.values())
    axes.yaxis.set_major_locator(MaxNLocator(8))
    axes.set_title("Best Fitness in each Generation")
    axes.set_xlabel("Generation")
    axes.set_ylabel("Fitness")
    #plt.savefig(name+'_graph.png')
    plt.show()

#graph(3000, 100, min, "eil76")
#graph(3000, 100, min, "ftv70")