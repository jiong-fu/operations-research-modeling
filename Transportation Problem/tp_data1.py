# Amount of supplies
suppliers = {}
suppliers[0] = 5
suppliers[1] = 3
suppliers[2] = 7
suppliers[3] = 6

# Amount of demands
demands = {}
demands[0] = 2
demands[1] = 4
demands[2] = 5

# Unit transportation cost from suppliers to demands
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

import tp_model
tp_model.solve(suppliers, demands, costs)