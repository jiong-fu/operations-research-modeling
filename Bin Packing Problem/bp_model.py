from gurobi import Model, GRB, quicksum

'''
Bin Packing Problem

Input
  s - size of items
  m - number of bins
  b - bin capacity
  
Output
  optimized bin count and packing plan
'''
def solve(s, m, b):
    
    # Create model
    model = Model("Bin Packing Problem")
    
    # Create variables
    x = {}
    for item in range(len(s)):
        for bin in range(m):
            x[item, bin] = model.addVar(name="pack_%s_%s" % (item, bin), vtype=GRB.BINARY)
    
    y = {}
    for bin in range(m):
        y[bin] = model.addVar(name="bin_%s" % bin, vtype=GRB.BINARY)
    
    # Update model
    model.update()
    
    # Add constraints
    # Each item is assigned to exactly one bin
    for item in range(len(s)):
        model.addConstr(quicksum(x[item, bin] for bin in range(m)) == 1)
    
    # Each bin keeps the capacity
    for bin in range(m):
        model.addConstr(quicksum(x[item, bin] * s[item] for item in range(len(s))) <= b * y[bin])
    
    # Set objective function
    model.setObjective(quicksum(y[item] for item in range(m)), GRB.MINIMIZE)

    # Solve model
    model.optimize()
    
    # Print optimized packing plan
    if model.status == GRB.OPTIMAL:
        print('\nOptimized Bin Count: %g' % model.ObjVal)
        for bin in range(m):
            if y[bin].x > 0.5:
                print("Bin %d is opened for use." % bin)

        for item in range(len(s)):
            for bin in range(m):
                if x[item, bin].x > 0.5:
                    print("Item %d is packed into bin %d." % (item, bin))
    else:
        print('No optimum solution found. Status: %i' % (model.status))
    
    return model