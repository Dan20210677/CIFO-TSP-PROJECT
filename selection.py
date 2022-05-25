#DONE

from random import uniform, choice, sample
from operator import attrgetter


def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "max":
        # Sum total fitness
        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += individual.fitness
            if position > spin:
                return individual

    elif population.optim == "min":
        total_fitness = sum([1/i.fitness for i in population])
        spin = uniform(0, total_fitness)
        position = 0
        for individual in population:
            position += 1/individual.fitness
            if position > spin:
                return individual
    else:
        raise Exception("No optimization specified (min or max).")

def tournament(population, size = 20):
    """Tournament implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.
    Returns:
        Individual: selected individual.
    """

    # Select individuals based on tournament size
    tournament = sample(population.individuals, size)
    # Check if the problem is max or min
    if population.optim == 'max':
        return max(tournament, key=attrgetter("fitness"))
    elif population.optim == 'min':
        return min(tournament, key=attrgetter("fitness"))
    else:
        raise Exception("No optimization specified (min or max).")

def ranking(population):
    """Ranking implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "max":
        d = {i: i.fitness for i in population}
        ord_d = sorted(d.items(), key=lambda item: item[1])
        ord = [ord_d[i][0] for i in range(len(ord_d))]
        total = sum(range(len(population) + 1))
        spin = uniform(0, 1)
        position = 0
        for i in range(len(ord)):
            position += (i+1)/total
            if position > spin:
                return ord[i]

    elif population.optim == "min":
        d = {i: i.fitness for i in population}
        ord_d = sorted(d.items(), key=lambda item: item[1], reverse=True)
        ord = [ord_d[i][0] for i in range(len(ord_d))]
        total = sum(range(len(population)+1))
        spin = uniform(0, 1)
        position = 0
        for i in range(len(ord)):
            position += (i+1)/total
            if position > spin:
                return ord[i]
    else:
        raise Exception("No optimization specified (min or max).")