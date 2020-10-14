import math


class Manometer:
    def __init__(self, specific_weight, deflection, angle):
        '''Creates a manometer situation as an object.
        Enter Specific Weight as N/m3
        Enter deflection as mm
        Enter angle as degrees'''
        self.specific_weight = specific_weight
        self.deflection = deflection/1000
        self.angle = math.radians(angle)

    def pressure_diff(self):
        '''Calculates the pressure difference and returns it'''
        pressure_diff = self.specific_weight * \
            self.deflection*(math.sin(self.angle))
        return round(pressure_diff, 2)
