#   ---------------------------------
#   |  On A Wing And A Prayer       |
#   |      Group Project            |
#   |  Wing Deflection Calculator   |
#   ---------------------------------

#   Clear the terminal to ensure a clean ouput  -  Jay's User-Defined Function
import os
def clear_term() :
    os.system('cls' if os.name == 'nt' else 'clear')
clear_term()

#   Define a header that will be used during the output section  -  Jay's User-Defined Function
def header() :
    print("\033[36m")
    print("*" * 50)
    print("          WING DEFLECTION CALCULATOR\n")
    print("            On a Wing and a Prayer\n\n")
    print("               Brought to you by\n")
    print("       Alessndra, Aeryn, Kyra, Jacob, Jay")
    print("*" * 50)
    print("\033[0m")


#---------------------
#   Main Functions
#---------------------

#   User-Defined Function for selecting an aircraft

def select_aircraft(aircraft) :
    print("Available Aircraft:")
    planes = list(aircraft.keys())

    for i, name in enumerate(planes, 1) :
        print (f"{i}. {name}")

    choice = int(input("Select Aircraft")) - 1
    return planes[choice]


#   User-Defined Function for selecting wing material

def select_material(materials) :
    print("Wing Materials:")
    mats = list(materials.key())

    for i, name in enumerate(mats, 1) :
        print(f"{i}. {name}")

    choice = int(input("Select Wing Material: ")) - 1
    return mats[choice]


#---------------------
#   Input Functions
#---------------------

#   User-Defined Function for flight conditions

def get_flight_conditions() :
    air_speed = float(input("Enter Air Speed (kts): "))
    altitude = float(input("Enter Altitude (meters): "))

    v = air_speed * 0.51444     #   Convert air speed from kts to m/s
    return v, altitude


#---------------------
#   The Physics Part
#---------------------

def calculate_air_density(h) :
    L = 0.0065  #   Temperature lapse rate
    g = 9.817   #   Gravity: It's not just a good idea, it's the law!
    R = 287     #   Gas Constant for air


header()

