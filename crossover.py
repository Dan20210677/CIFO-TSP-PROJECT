#Done

from random import randint, sample
from charles import Population, Individual

def single_point_co(p1, p2):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_point = randint(1, len(p1)-1)

    o1 = list(p1).copy()
    for i in range(co_point):
        o1[o1.index(p2[i])] = o1[i]
        o1[i] = p2[i]
    o2 = list(p2).copy()
    for i in range(co_point):
        o2[o2.index(p1[i])] = o2[i]
        o2[i] = p1[i]

    return o1, o2

def cycle_co(p1, p2):
    """Implementation of cycle crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    p1=list(p1)
    p2=list(p2)
    cycles = [-1]*len(p1)
    cycle_no = 1
    cyclestart = (i for i,v in enumerate(cycles) if v < 0)

    for pos in cyclestart:

        while cycles[pos] < 0:
            cycles[pos] = cycle_no
            pos = p1.index(p2[pos])

        cycle_no += 1

    o1 = [p1[i] if n%2 else p2[i] for i,n in enumerate(cycles)]
    o2 = [p2[i] if n%2 else p1[i] for i,n in enumerate(cycles)]
    return o1, o2

def ordered_co(p1, p2):
    """Implementation of ordered crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    o1 = []
    o2 = []
    o1P1 = []
    o1P2 = []
    o2P1 = []
    o2P2 = []

    g = sorted(sample(range(len(p1)+1), 2))

    for i in range(g[0], g[1]):
        o1P1.append(p1[i])
        o2P1.append(p2[i])

    o1P2 = [item for item in p2 if item not in o1P1]
    o2P2 = [item for item in p1 if item not in o2P1]
    j=0
    k=0
    for i in range(len(p1)):
        if i < g[0]:
            o1.append(o1P2[j])
            o2.append(o2P2[j])
            j=j+1
        elif i < g[1]:
            o1.append(o1P1[k])
            o2.append(o2P1[k])
            k=k+1
        else:
            o1.append(o1P2[j])
            o2.append(o2P2[j])
            j=j+1
    return o1, o2

if __name__ == '__main__':
    p1, p2 = [5, 7, 1, 3, 6, 4, 2], [4, 6, 2, 7, 3, 1, 5]
    o1, o2 = ordered_co(p1, p2)
    print(o1, o2)
