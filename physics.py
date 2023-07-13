v = 0
mass = 0
depth = int
density_fluid = 1000
g = 9.81


# calculate and return the buoyancy
def calculate_buoyancy(v):
    return f"the buoyancy is {v*density_fluid*g} Newtons"


# tell the user if the object will flaot or not
def will_it_float(v, mass):
    return v * density_fluid * g > mass * g


# calculate and return the pressure
def calculate_pressure(depth):
    return f"the pressure is {density_fluid*depth*g} Pascals"
