v = 0
mass = 0
depth = int
density_fluid = 1000
g = 9.81


def calculate_buoyancy(v):
    return f"the buoyancy is {v*density_fluid*g} Newtons"


def will_it_float(v, mass):
    return v * density_fluid * g >= mass * g


def calculate_pressure(depth):
    return f"the pressure is {density_fluid*depth*g} Pascals"
