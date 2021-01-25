
# The diet problem 

import cvxpy as cp
import numpy as np

cost = np.matrix( [0.18,0.23,0.05] )
x = cp.Variable(3) 
objective = cp.Minimize(cost*x)

constraints = [x[0]*107+x[1]*500+x[2]*0 >= 5000,x[0]*107+x[1]*500+x[2]*0 <= 50000,x[0]*72+x[1]*121+x[2]*10 >= 2000,x[0]*72+x[1]*121+x[2]*10 <= 2250,x[0] <= 10,x[1]<= 10,x[2]<= 10]

prob = cp.Problem(objective, constraints)
result = prob.solve()
print(x.value)
