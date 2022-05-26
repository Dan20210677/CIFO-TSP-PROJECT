# CIFO-TSP-PROJECT

The full tables of the small problems are available in the repository since in the report we only present the parcial tables.

INTRUCTIONS/INFORMATION

selection.py, crossover.py, mutation.py and charles.py are fixed, no need to alter.

data.py is the code to work on the tsp files and create the confusion matrix and graph.
IMPORTANT:
A list of the files added during our project is displaied, change the variable NOME to the name of the file you want to study.

More files can be added with the consideration that: 
-ATSP files might need edit to alter the confusion matrix so each line of the file corresponds to a line of the matrix.
-All files might need edit to alter if there is a space between the variable name and the double dots.

tsp.py is where algorithms are run and tested.
build_table, build_graph and graph are funtions with inputs, but they also need to be changed inside the funtion.

For build_table, need to alter the for cycles to only test the operators required, to only test the combinations wanted.
With all available operators, there are 72 possible combinations, so less operators means less combinations so less running time.
Also the number of repetitions need to be above 30 to mantain statistical significance.

For build_graph, need to alter the operators for each of the two evolutions to the operators required to compare.

For graph, need to alter the operators for the GA algorithm.

The mutation and crossover probabilities are fixed but can be changed at any point.

TSP/ATSP are minimization problems, but the option to change to maximization is available, to do that changes in basically all the code is required.
For TSP/ATSP only changing the fitness funtion might be enough, 
but if the focus is to change the problem, then the operators coded might not be adequate.
