#Done

from random import randint, sample


def swap_mutation(individual):
    """Swap mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py
    Returns:
        Individual: Mutated Individual
    """
    mut_points = sample(range(len(individual)), 2)
    individual[mut_points[0]], individual[mut_points[1]] = individual[mut_points[1]], individual[mut_points[0]]

    return individual

def inversion_mutation(individual):
    """Inversion mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py
    Returns:
        Individual: Mutated Individual
    """
    mut_points = sorted(sample(range(len(individual)+1), 2))
    individual=individual[:mut_points[0]]+list(reversed(individual[mut_points[0]:mut_points[1]]))+individual[mut_points[1]:]

    return individual

def insertion_mutation(individual):
    """Insertion mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py
    Returns:
        Individual: Mutated Individual
    """
    individual = list(individual)
    mut_points = sample(range(len(individual)), 1)
    insert = [individual[mut_points[0]]]
    individual.pop(mut_points[0])
    new_mut_points = sample(range(len(individual)+1), 1)
    individual=individual[:new_mut_points[0]]+insert+individual[new_mut_points[0]:]


    return individual

def displacement_mutation(individual):
    """Displacement mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py
    Returns:
        Individual: Mutated Individual
    """
    individual = list(individual)
    mut_points = sorted(sample(range(len(individual)), 2))
    displace = individual[mut_points[0]:mut_points[1]]
    individual = individual[:mut_points[0]]+individual[mut_points[1]:]
    new_mut_points = sample(range(len(individual)+1), 1)
    individual = individual[:new_mut_points[0]]+displace+individual[new_mut_points[0]:]
    return individual

if __name__ == '__main__':
    test = [0,1,2,3,4,5,6,7]
    test = displacement_mutation(test)
    print(test)