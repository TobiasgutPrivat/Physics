from .Measures import *

mass = 10 * kg  # Mass = 10kg
acceleration = 2 * meter / sec ** 2  # Acceleration = 2m/s²
distance = 10 * meter
time = 2 * sec

# force
force = mass * acceleration
print("Force: ", force)  # Force = 20 kg * m / s^2

force.format({"N": 1}) # nice format
print("Force: ", force)  # Force = 20N

force.format({"N": -1}) # weird format
print("Force: ", force)  # Force = 20 kg^2 * m^2 / N * s^4

# work
work = force * distance
print("Work: ", work)  # Work = 200 kg^2 * m^3 / N * s^4, weird because of weird force-format

work.format({"N": 1})
print("Work: ", work)  # Work = 200N.m

work.format({"J": 1})
print("Work: ", work)  # Work = 200J

# power
power = work / time
print("Power: ", power)  # Power = 100 kg * m^2 / s^3

power.format({"W": 1})
print("Power: ", power)  # Power = 100W