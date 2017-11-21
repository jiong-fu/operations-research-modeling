from gurobi import Model, GRB, quicksum

'''
Minimum Cost Matching Problem

Input
  n - number of sources
  m - number of targets
  c - assignment cost from sources to targets
  
Output
  optimized assignment cost and plan
'''
def solve(n, m, c):
    
    # Create model
    model = Model("Minimum Cost Matching Problem")
    
    # Create variables
    x = {}
    for source in range(n):
        for target in range(m):
            x[source, target] = model.addVar(name="assign_%s_%s" % (source, target), vtype=GRB.BINARY)
    
    # Update model
    model.update()
    
    # Add constraints
    # Each source is assigned to at most one target
    for source in range(n):
        model.addConstr(quicksum(x[source, target] for target in range(m)) <= 1)
    
    # Each target is assigned exactly one source
    for target in range(m):
        model.addConstr(quicksum(x[source, target] for source in range(n)) == 1)
    
    # Set objective function
    model.setObjective(quicksum(x[source, target] * c[source, target] for source in range(n) for target in range(m)))
    
    # Solve model
    model.optimize()
    
    # Print optimized assignment plan
    if model.status == GRB.OPTIMAL:
        print('\nOptimized Assignment Cost: %g' % model.ObjVal)
        for source in range(n):
            for target in range(m):
                if x[source, target].x > 0.5:
                    print("Source %d is assigned to target %d." % (source, target))
    else:
        print('No optimum solution found. Status: %i' % (model.status))
    
    return model