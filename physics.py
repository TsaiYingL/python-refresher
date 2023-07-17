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
def calculate_acceleration(F: int or float, m: int or float):
    if m >= 0:
        acceleration = F / m
        return acceleration
    else:
        return "error"


# will return error if m = 0


# calculates the angular acceleration
def calculate_angular_acceleration(tau, I):
    if I >= 0:
        angular_acceleration = tau / I
        return angular_acceleration
    else:
        return "error"


# calculates the torque
def calculate_torque(F_magnitude, F_direction, r):
    if r > 0:
        torque = r * F_magnitude * np.sin(np.deg2rad(F_direction))
        return torque
    else:
        return "error"


# np.deg2rad changes degrees to rads


# calculates the moment of inertia
def calculate_moment_of_inertia(m, r):
    if m >= 0 and r > 0:
        moment_of_inertia = m * np.power(r, 2)
        return moment_of_inertia
    else:
        raise ValueError()


# calculate the acceleration of AUV (with 1 thruster)
def calculate_auv_acceleration(
    F_magnitude,
    F_angle,
    mass: float = 100,
    volume: float = 0.1,
    thruster_distance: float = 0.5,
):
    if thruster_distance >= 0 and mass >= 0 and volume >= 0:
        force = np.array([np.cos(F_angle), np.sin(F_angle)]) * F_magnitude
        acceleration = force / mass
        # acceleration_x = F_magnitude * np.cos(F_angle) / mass
        # acceleration_y = F_magnitude * np.sin(F_angle) / mass
        # return (acceleration_x, acceleration_y)
        return acceleration


# better not to round since it will affect the precision***


# calculate the angular acceleration of AUV (with 1 thruster)
def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    if thruster_distance >= 0 and inertia >= 0:
        torque = F_magnitude * np.sin(F_angle) * thruster_distance
        angular_acceleration = torque / inertia
        return angular_acceleration


# use the function that is being defined before


# calculate the acceleration of AUV (with 4 thrusters)
def calculate_auv2_acceleration(
    T: np.ndarray, alpha: int or float, theta: int or float, mass=100
):
    if T.shape == (4,) and mass >= 0:
        trig = np.array(
            [
                [np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
                [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)],
            ]
        )
        robot_force = np.sum(trig * T, axis=1)
        force = np.sum(
            np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
            * robot_force,
            axis=1,
        )
        acceleration = force / mass
        acceleration_x = round(acceleration[0], 10)
        acceleration_y = round(acceleration[1], 10)
        return (acceleration_x, acceleration_y)
    else:
        return "error"


# try to use np.matmul
# should ask for a 4x1 array, not 1x4 shape(1,4)
# raise ValueError, not return


# calculate the angular acceleration of the AUV (with 4 thrusters)
def calculate_auv2_angular_acceleration(
    T: np.ndarray, alpha, L: int or float, l: int or float, inertia=100
):
    if T.shape == (4,) and inertia >= 0 and L >= 0 and l >= 0:
        trig = np.array(
            [
                l * np.cos(alpha) + L * np.sin(alpha),
                l * np.cos(alpha) - L * np.sin(alpha),
                -l * np.cos(alpha) - L * np.sin(alpha),
                -l * np.cos(alpha) + L * np.sin(alpha),
            ]
        )
        torque = np.sum(trig * T)
        alpha = round(torque / inertia, 10)
        return alpha
    else:
        return "error"


# np.array([1,-1,1,-1]) is a 4x1 matrix; np.array([1,-1,1,-1]).T (transpose) is a 1x4 matrix


if __name__ == "__main__":
    print(
        calculate_auv2_angular_acceleration(
            np.array([200, 200, 100, 100]), np.pi / 3, 100, 50
        )
    )
    print(200 * (100 * (np.sin(np.pi / 3)) + 50 * (np.cos(np.pi / 3))))
    print(200 * (100 * (np.sin(np.pi / 3)) - 50 * (np.cos(np.pi / 3))))
    print(100 * (-100 * (np.sin(np.pi / 3)) - 50 * (np.cos(np.pi / 3))))
    print(100 * (-100 * (np.sin(np.pi / 3)) + 50 * (np.cos(np.pi / 3))))
    print(np.cos(np.pi / 3))

    print(calculate_auv_acceleration(10, np.pi / 2), (0, 0.1))

# √√ next time can return the value instead of a string
# √√ don't need to make a class sine the question specified to make a function
# √√ we use classes when we have multiple objects
# the volume, depth, and density cannot be less than 0
# √√ command d can select the same thing that you initially selected
# √√ might not need to set v, mass, and depth to 0 st the start
# √√ elif: only use it when the cases are related to each other
# √√ when returning the value, define the equation so we know what it is when debugging
