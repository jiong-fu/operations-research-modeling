# Number of workers
workers = 4

# Number of machines
machines = 3

# Assignment cost from workers to machines
costs = {}
costs[0, 0] = 3
costs[0, 1] = 2
costs[0, 2] = 3
costs[1, 0] = 1
costs[1, 1] = 4
costs[1, 2] = 2
costs[2, 0] = 2
costs[2, 1] = 3
costs[2, 2] = 2
costs[3, 0] = 3
costs[3, 1] = 1
costs[3, 2] = 4

import mcmp_model
mcmp_model.solve(workers, machines, costs)