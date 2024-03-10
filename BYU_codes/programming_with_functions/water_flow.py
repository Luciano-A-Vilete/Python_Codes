
def water_column_height(tower_height, tank_height):
    h = tower_height + (3 * tank_height) / 4
    return h

# water_flow.py

def pressure_gain_from_water_height(height):
    # Constants
    density_of_water = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2    
    # Calculating pressure
    pressure = (density_of_water * gravity * height) / 1000  # in kilopascals
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    # Constants
    density_of_water = 998.2  # kg/m^3
    # Calculating pressure loss
    pressure_loss = - (friction_factor * pipe_length * density_of_water * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss