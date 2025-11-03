from pulp import *

model = LpProblem("Minimize Objective Function", LpMinimize)

x1 = LpVariable("x1", lowBound=0, cat='Continuous')
x2 = LpVariable("x2", lowBound=0, cat='Continuous')
x3 = LpVariable("x3", lowBound=0, cat='Continuous')

# Define objective function
model += x1 + 2*x2 + 3*x3, "Objective"

model += -2*x1 + x2 + x3 >= 3
model += x1 + x3 >= 2

model.solve()

print("Optimal Solution:")
print("x1 =", value(x1))
print("x2 =", value(x2))
print("x3 =", value(x3))
print("Objective =", value(model.objective))