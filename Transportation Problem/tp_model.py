from gurobi import Model, GRB, quicksum

'''
Transportation Problem

Input
  n - amount of supplies
  m - amount of demands
  c - unit transportation cost from suppliers to demands
  
Output
  optimized transportation cost and plan
'''
def solve(n, m, c):
    
    # Create model
    model = Model("Transportation Problem")
    
    # Create variables
    x = {}
    for supply in range(len(n)):
        for demand in range(len(m)):
            x[supply, demand] = model.addVar(name="transport_%s_%s" % (supply, demand), vtype=GRB.INTEGER)
    
    # Update model
    model.update()
    
    # Add constraints
    # Each supplier keeps the capacity
    for supply in range(len(n)):
        model.addConstr(quicksum(x[supply, demand] for demand in range(len(m))) <= n[supply])
    
    # Each demand is satisfied
    for demand in range(len(m)):
        model.addConstr(quicksum(x[supply, demand] for supply in range(len(n))) == m[demand])
    
    # Set objective function
    model.setObjective(quicksum(x[supply, demand] * c[supply, demand] for supply in range(len(n)) for demand in range(len(m))))
    
    # Solve model
    model.optimize()
    
    # Print optimized transportation plan
    if model.status == GRB.OPTIMAL:
        print('\nOptimized Transportation Cost: %g' % model.ObjVal)
        for supply in range(len(n)):
            for demand in range(len(m)):
                if x[supply, demand].x > 0.5:
                    print("Supplier %d transports %d units to demand %d." % (supply, x[supply, demand].x, demand))
    else:
        print('No optimum solution found. Status: %i' % (model.status))
    
    return model