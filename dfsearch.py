import sys, rushutils_uninformed, os.path, visualisation
from timeit import default_timer as timer


def dfs():
    """
    calculates a path to a winning state
    """
    while len(stack):

        # get the first node from the stack
        node = stack.pop()

        # generate all possible children
        for move in node.get_moves():
            child = node.move(move[0], move[1])

            # check if child has already been processed
            if child not in closed:

                # add child to closed list and to the stack
                closed.add(child)
                stack.append(child)

            # check if current child is a solution
            if move[0] == 0:
                if child.win():
                    solutions.append(child)

# check if file is supplied
if len(sys.argv) <= 1:
    print "No file is supplied"
    print "Usage: python dfsearch.py <board.txt>"
    sys.exit()

# check if file exists
elif not os.path.isfile(sys.argv[1]):
    print "File can't be loaded"
    print "Usage: python dfsearch.py <board.txt>"
    sys.exit()

# load board from file
else:

    # initialize root node
    root = rushutils_uninformed.Board()
    root.load_from_file(sys.argv[1])

    # initialize queue, solutions list, and closed archive
    closed = set()
    stack = list()
    solutions = list()
    closed.add(root)
    stack.append(root)

# start the timer
start = timer()

# get first route to solution
dfs()

# stop the timer
end = timer()

# get the moves to the winning state
shortest_solution = list()
for path in solutions:
    solution = list()
    current = path
    while current.parent is not None:
        solution.append(current.moved)
        current = current.parent
    if len(shortest_solution) == 0 or len(shortest_solution) > len(solution):
        solution.reverse()
        shortest_solution = solution

# print results
print "\nExplored %d states in %f seconds" % (len(closed), (end - start))
print "\nFound %d solutions, shortest solution takes %d moves" % (len(solutions), len(shortest_solution))
print shortest_solution
print

# start visualisation if wanted
if raw_input("View visualisation of solution? (Y/N): ").lower() == 'y':
    vis = visualisation.Visualisation(root, moves)
