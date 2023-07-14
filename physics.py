""" the purpose of the funsction i to calculate the buoyancy and pressure of an object 
in water. It also tells us if the object will float on water"""

# adding values
import numpy as np
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

# find angular acceleration
def calculate_angular_acceleration(tau, I):
    if I>=0:
        angular_acceleration = tau/I
        return angular_acceleration
    else:
        return "error"

def calculate_torque(F_magnitude, F_direction, r):
    if r>0:
        F_direction *= np.pi/180
        torque = r*F_magnitude*np.sin(F_direction)
        return torque
    else:
        return "error"
    
def calculate_moment_of_inertia(m,r):
    if m>=0 and r>0:
        moment_of_inertia = m*(r**2)
        return moment_of_inertia
    else:
        return "error"

def calculate_auv_acceleration(F_magnitude, F_angle, mass = 100, volume = 0.1, thruster_distance = 0.5):
    if thruster_distance>=0 and mass>=0 and :



# √√ next time can return the value instead of a string
# √√ don't need to make a class sine the question specified to make a function
# √√ we use classes when we have multiple objects
# the volume, depth, and density cannot be less than 0
# √√ command d can select the same thing that you initially selected
# √√ might not need to set v, mass, and depth to 0 st the start
# √√ elif: only use it when the cases are related to each other
# √√ when returning the value, define the equation so we know what it is when debugging
