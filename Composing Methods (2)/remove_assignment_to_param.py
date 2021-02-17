class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value
class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
    def get_distance(self, distance):
        if distance.unit != 'km':
            if distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
                # convert from light-year to km unit        
                in_km = distance.value * 9.461e12
                return Distance(in_km, "km") 
            else:
                raise KeyError("unit is Unknown")
    def get_speed(self, converted_distance, time):
        return converted_distance.value/time # [km per sec]
    def get_mass(self, mass):
        if mass.unit != 'kg':
            if mass.unit == "solar-mass":
                # convert from solar mass to kg
                value = mass.value * 1.98892e30 # [kg]
                return Mass(value, 'kg')
            else:
                raise KeyError("unit is Unknown")
    def calculate_kinetic_energy(self, mass, distance, time):
        converted_distance = self.get_distance(distance)
        speed = self.get_speed(converted_distance, time)
        converted_mass = self.get_mass(mass)    
        return 0.5 * converted_mass.value * speed ** 2

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(mass.calculate_kinetic_energy(mass, distance, 3600e20))