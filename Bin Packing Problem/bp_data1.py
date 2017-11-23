# Size of items
sizes = {}
sizes[0] = 8
sizes[1] = 5
sizes[2] = 7
sizes[3] = 4

# Number of bins
bins = 5

# Bin capacity
capacity = 12

import bp_model
bp_model.solve(sizes, bins, capacity)