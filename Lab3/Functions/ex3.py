def solve(numheads, numlegs):
    num_chickens = 0
    num_rabbits = 0


    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:

            return num_chickens, num_rabbits
    

    return None

numheads = 35
numlegs = 94
solution = solve(numheads, numlegs)

if solution:
    num_chickens, num_rabbits = solution
    print("Number of chickens:", num_chickens)
    print("Number of rabbits:", num_rabbits)
else:
    print("No solution found.")
