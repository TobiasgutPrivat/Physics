from PhysicObject.PhysicalObject import PhysicalObject  # Relative import for standalone execution

# Create a new physical object
obj = PhysicalObject("Object")

# Define properties
obj.set_property("m", 10)  # Mass = 10kg
obj.set_property("a", 2)   # Acceleration = 2m/s²

# System automatically calculates Force (F = m * a)
print(obj)

# Introduce a conflict
obj.set_property("m", 25)  # Manually override force
print(obj)

# Define a new property
obj.set_property("A", 5)  # Area = 5m²

# System calculates pressure (p = F / A)
print(obj)