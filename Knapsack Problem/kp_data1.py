# Size of items
sizes = {}
sizes[0] = 8
sizes[1] = 5
sizes[2] = 7
sizes[3] = 4

# Profit of items
profits = {}
profits[0] = 2
profits[1] = 4
profits[2] = 3
profits[3] = 5

# Knapsack capacity
capacity = 12

import kp_model
kp_model.solve(sizes, profits, capacity)