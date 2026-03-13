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

print("Wing Deflection Simulator\n")

# 	User Inputs - select type of aircraft and wing material
#	Input flight speed and altitude
#   LIst of 6 different aircraft

def calculate_deflection() :    # Gather variable choices
    # 1- Aircraft data (wingspan in meters, reference area in m^2)
    aircraft = {
        "Sailplane (High Performance)" : {"span" : 21.0, "area" : 13.2},
        "Cesna 172" : {"span" : 11.0, "area" : 16.2},
        "Gulfstream G500" : {"span" : 26.5, "area" : 88.0},
        "Boeing 737-800" : {"span" : 35.8, "area" : 124.6},
        "Boeing 787-10" : {"span" : 60.1, "area" : 361.0},
        "Lockheed C-5 Galaxy" : {"span" : 67.9, "area" : 576.0},
    }

    materials = {
        "Carbon Fiber (CFRP)" : 150e9,
        "Aluminum (7075)" : 71.7e9,
        "Titanium Alloy" : 113e9,
        "Sitka Spruce (Wood)" : 11e9,
        "Concrete" : 28e9
    }


    #  Select the airplane

    planes = list(aircraft.keys())
    for i, name in enumerate(planes, 1) :
        print(f"{i}. {name}")
    plane_choice = planes[int(input("\nSelect Aircraft (1-6): ")) - 1]
       


    #  Select the wing material
    mats = list(materials.keys())
    for j, name in enumerate(mats, 1) :
        print(f"{j}. {name}")
    mat_choice = mats[int(input("\nSelect Wing Material (1-5): ")) - 1]


    #   This is a list of inputs and calculations

    air_spd = float(input("\nEnter Air Speed (kts): "))
    v = air_spd * 0.51444  #  m/s

    h = float(input("\nEnter Altitude (meters): "))
    L = 0.0065  #  Temperature lapse rate
    g = 9.81  #  Gravity: It's not just a good idea, it's the law.
    R = 287  #  Gas constant for air (J/kg K)


    rho0 = 1.225  # Air density at sea level
    T0 = 288.15
    rho = rho0 + (1 - (L * h) / T0) ** ((g / (R * L)) - 1)

    print(f"Air density at {h} meters is", round(rho, 3), "kg/m^3")

    cl = 0.6  #This is the lift constant (L) using a higher than typical Cl for general calculations
    E = materials[mat_choice]

    #  This is for determining the thickness profile for the wing depending on AC chosen

    #  Structural Geometry (I value)

    if "Sailplane" in plane_choice :
        thickness_factor = 0.03  #  very thin
    else:
        thickness_factor = 0.12  #Standard airfoil thickness

    span = aircraft[plane_choice]["span"]
    area = aircraft[plane_choice]["area"]

    #  Moment of Inertia (approximated for a wing box)
    #  I = (width * height^3) / 12
    avg_chord = area / span
    height = avg_chord * thickness_factor
    I = (avg_chord * (height**3)) / 12


    #  Let's calculate


    lift = 0.5 * rho * (v**2) * area * cl
    q = (lift / 2) / (span / 2)  #  Load per meter on one wing

    #  Cantilever Deflection: (q * l^4) / (8 * E * I)
    #  L is the length of one wing (half-span)
    L_wing = span / 2
    deflection = (q * (L_wing**4)) / (8 * E * I)

    #  Time to print stuff

    print(f"\n" + "*" * 40)
    print(f"AIRCRAFT: {plane_choice}")
    print(f"MATERIAL: {mat_choice}")
    print(f"FORCE:  {lift:,.3f} N total lift")
    print(f"Estimated Wingtip Deflection: {deflection * 100:.3f} cm")
    print()
    #  Warnings
    if deflection > (L_wing * 0.2) :
        print("Warning: Structural limits likely exceeded!")
    elif "Concrete" in mat_choice :
        print("\033[31m" + "A plane with concrete wings isn't going to get off the ground." + "\033[0m")
    
    # #	Calculate deflection at different points along the wing

    # deflection = []
    # positions = []
    # steps = 10

    # for i in range(steps + 1) :
    #     x = L * i / steps
    #     y = (w * x**2 / (24 * E * I)) * (6 * L**2 - 4 * L * x + x**2)
    #     positions.append(x)
    #     deflection.append(y)
    # print("Deflection along the wing:")
    # for i in range(len(positions)) :
    #     print("x = {:.2f}m, deflection = {:.6f}m".format(positions[i], deflection[i]))
    # print()


if __name__ == "__main__" :    #  This makes sure the code runs only in this file and isn't accidentally run in another
    calculate_deflection()

