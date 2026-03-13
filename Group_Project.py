#	Clear the terminal
import os
def clear_terminal() :
	os.system('cls' if os.name == 'nt' else 'clear')
clear_terminal()
#  	
#	Calculating Wing Deflection Under a Lift Load
#	This Python code will compute deflection along the wingspan
#	and show the maximum tip deflection under different flight conditions
#

print("Wing Deflection Calculator\n")

# 	User Inputs

rho = float(input("Enter air density (kg/m^3): "))
V = float(input("Enter aircraft flight speed (m/s): "))
S = float(input("Enter wing surface area (m^2): "))
CL = float(input("Enter lift coefficient: "))
L = float(input("Enter wingspan for one wing (m): "))
E = float(input("Enter Young's modulus (Pa): "))
I = float(input("Enter moment of inertia (m^4): "))
print()

#	Behind the scenes calculations

lift = 0.5 * rho * V**2 * S * CL
w = lift / L
max_deflection = (w * L**4) / (8 * E * I)

#	Calculate deflection at different points along the wing

deflection = []
positions = []
steps = 10

for i in range(steps + 1) :
	x = L * i / steps
	y = (w * x**2 / (24 * E * I)) * (6 * L**2 - 4 * L * x + x**2)
	positions.append(x)
	deflection.append(y)
print("Deflection along the wing:")
for i in range(len(positions)) :
	print("x = {:.2f}m, deflection = {:.6f}m".format(positions[i], deflection[i]))
print()
