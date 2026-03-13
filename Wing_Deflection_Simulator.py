# Wing Deflection Simulator
import os


# ---------------------------------------
# Utility Functions
# ---------------------------------------

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# ---------------------------------------
# Menu Functions
# ---------------------------------------

def select_aircraft(aircraft):
    print("\nAvailable Aircraft:")
    planes = list(aircraft.keys())

    for i, name in enumerate(planes, 1):
        print(f"{i}. {name}")

    choice = int(input("\nSelect Aircraft: ")) - 1
    return planes[choice]


def select_material(materials):
    print("\nWing Materials:")
    mats = list(materials.keys())

    for i, name in enumerate(mats, 1):
        print(f"{i}. {name}")

    choice = int(input("\nSelect Material: ")) - 1
    return mats[choice]


# ---------------------------------------
# Input Functions
# ---------------------------------------

def get_flight_conditions():
    air_speed = float(input("\nEnter Air Speed (kts): "))
    altitude = float(input("Enter Altitude (meters): "))

    v = air_speed * 0.51444
    return v, altitude


# ---------------------------------------
# Physics Functions
# ---------------------------------------

def calculate_air_density(h):

    L = 0.0065
    g = 9.81
    R = 287
    rho0 = 1.225
    T0 = 288.15

    rho = rho0 + (1 - (L * h) / T0) ** ((g / (R * L)) - 1)

    return rho


def determine_thickness(plane_choice):

    if "Sailplane" in plane_choice:
        return 0.03
    else:
        return 0.12


def calculate_moment_of_inertia(span, area, thickness_factor):

    avg_chord = area / span
    height = avg_chord * thickness_factor

    I = (avg_chord * height**3) / 12

    return I


def calculate_wing_deflection(rho, v, area, span, cl, E, I):

    lift = 0.5 * rho * v**2 * area * cl

    q = (lift / 2) / (span / 2)

    L_wing = span / 2

    deflection = (q * L_wing**4) / (8 * E * I)

    return lift, deflection, L_wing


# ---------------------------------------
# Output Functions
# ---------------------------------------

def display_air_density(rho, altitude):
    print(f"\nAir density at {altitude} meters: {rho:.3f} kg/m^3")


def display_results(plane, material, lift, deflection, L_wing):

    print("\n" + "*" * 40)
    print(f"AIRCRAFT: {plane}")
    print(f"MATERIAL: {material}")
    print(f"TOTAL LIFT: {lift:,.3f} N")
    print(f"Estimated Wingtip Deflection: {deflection * 1:.3f} cm")

    if deflection > (L_wing * 0.2):
        print("Warning: Structural limits likely exceeded!")

    if "Concrete" in material:
        print("A plane with concrete wings isn't going to get off the ground.")


# ---------------------------------------
# Main Program
# ---------------------------------------

def main():

    clear_terminal()

    print("Wing Deflection Simulator\n")

    aircraft = {
        "Sailplane (High Performance)": {"span": 21.0, "area": 13.2},
        "Cessna 172": {"span": 11.0, "area": 16.2},
        "Gulfstream G500": {"span": 26.5, "area": 88.0},
        "Boeing 737-800": {"span": 35.8, "area": 124.6},
        "Boeing 787-10": {"span": 60.1, "area": 361.0},
        "Lockheed C-5 Galaxy": {"span": 67.9, "area": 576.0},
    }

    materials = {
        "Carbon Fiber (CFRP)": 150e9,
        "Aluminum (7075)": 71.7e9,
        "Titanium Alloy": 113e9,
        "Sitka Spruce (Wood)": 11e9,
        "Concrete": 28e9
    }

    cl = 0.6

    plane_choice = select_aircraft(aircraft)
    mat_choice = select_material(materials)

    v, altitude = get_flight_conditions()

    rho = calculate_air_density(altitude)

    display_air_density(rho, altitude)

    span = aircraft[plane_choice]["span"]
    area = aircraft[plane_choice]["area"]

    thickness_factor = determine_thickness(plane_choice)

    I = calculate_moment_of_inertia(span, area, thickness_factor)

    E = materials[mat_choice]

    lift, deflection, L_wing = calculate_wing_deflection(
        rho, v, area, span, cl, E, I
    )

    display_results(plane_choice, mat_choice, lift, deflection, L_wing)


# ---------------------------------------

if __name__ == "__main__":
    main()