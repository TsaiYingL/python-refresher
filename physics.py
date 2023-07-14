""" the purpose of the funsction i to calculate the buoyancy and pressure of an object 
in water. It also tells us if the object will float on water"""

# adding values
density_fluid = 1000
g = 9.81


# calculate and return the buoyancy
def calculate_buoyancy(v):
    if v >= 0 and density_fluid >= 0:
        buoyancy = v * density_fluid * g
        return buoyancy
    else:
        return "error"


# tell the user if the object will flaot or not
def will_it_float(v, mass):
    if v >= 0 and density_fluid >= 0 and mass >= 0:
        will_float = v * density_fluid * g > mass * g
        return will_float
    else:
        return "error"


# calculate and return the pressure
def calculate_pressure(depth):
    if density_fluid >= 0:
        if depth < 0:
            depth = abs(depth)
        surface_pressure = 101324
        pressure = density_fluid * depth * g + surface_pressure
        return pressure
    else:
        return "error"


# calculates the acceleration of an object
def calculate_acceleration(F, m):
    if m >= 0:
        acceleration = F / m
        return acceleration
    else:
        return "error"


# √√ next time can return the value instead of a string
# √√ don't need to make a class sine the question specified to make a function
# √√ we use classes when we have multiple objects
# the volume, depth, and density cannot be less than 0
# √√ command d can select the same thing that you initially selected
# √√ might not need to set v, mass, and depth to 0 st the start
# √√ elif: only use it when the cases are related to each other
# √√ when returning the value, define the equation so we know what it is when debugging
