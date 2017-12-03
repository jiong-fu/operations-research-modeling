from gurobi import Model, GRB, quicksum

'''
Knapsack Problem

Input
  s - size of items
  p - profit of items
  b - knapsack capacity

Output
  optimized packing profit and plan
'''
def solve(s, p, b):
    
    # Create model
    model = Model("Knapsack Problem")
    
    # Create variables
    x = {}
    for item in range(len(s)):
        x[item] = model.addVar(name="item_%s" % item, vtype=GRB.BINARY)
    
    # Update model
    model.update()
    
    # Add constraints
    # The knapsack keeps the capacity
    model.addConstr(quicksum(x[item] * s[item] for item in range(len(s))) <= b)
    
    # Set objective function
    model.setObjective(quicksum(x[item] * p[item] for item in range(len(s))), GRB.MAXIMIZE)
    
    # Solve model
    model.optimize()
    
    # Print optimized packing plan
    if model.status == GRB.OPTIMAL:
        print('\nOptimized Packing Profit: %g' % model.ObjVal)
        for item in range(len(s)):
            if x[item].x > 0.5:
                print("Item %d is packed into knapsack." % item)
    else:
        print('No optimum solution found. Status: %i' % (model.status))
    
    return model