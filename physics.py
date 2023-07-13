""" the purpose of the funsction i to calculate the buoyancy and pressure of an object 
in water. It also tells us if the object will float on water"""

# adding values
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
    surface_pressure = 101324
    return f"the pressure is {density_fluid*depth*g+surface_pressure} Pascals"


# next time can return th =e value instead of a string
# don't need to make a class sine the question specified to make a function
# we use classes when we have multiple objects
# the volume, depth, and density cannot be less than 0
# command d can select the same thing that you initially selected
# might not need to set v, mass, and depth to 0 st the start
# elif: only use it when the cases are related to each other
# when returning the value, define the equation so we know what it is when debugging
