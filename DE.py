import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the system of equations
def system_of_eqs(x, y):
    f, g = y
    return [g,- f]

# Initial conditions
initial_conditions = [1, 1]  # [f(0), f'(0)]

# Time span (x values)
x_span = [0, 10]  # You can adjust the upper limit as needed

# Solve the differential equation
solution = solve_ivp(system_of_eqs, x_span, initial_conditions, t_eval=np.linspace(0, 10, 100))

# Plotting the solution
plt.plot(solution.t, solution.y[0], label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x) and f\'(x)')
plt.title('Solution of f\'\'(x) = f(x) with f(0)=1, f\'(0)=1')
plt.legend()
plt.grid(True)
plt.show()