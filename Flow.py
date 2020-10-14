import math


class Flow:
    def __init__(self, flowrate, diameter, density, viscosity):
        '''
        enter flow rate in liters/s
        enter diameter in mm
        enter density in kg/m3
        enter viscosity in (N.s/m2)
        '''
        self.flowrate = flowrate/1000
        self.diameter = diameter/1000
        self.density = density
        self.viscosity = viscosity
        self.area = (math.pi)*(self.diameter/2)**2
        self.velocity = self.flowrate / self.area

    def get_flowrate(self):
        ''' 
        returns the flow rate samples'''
        return self.flowrate

    def get_diameter(self):
        '''
        returns the diameter of pipe'''
        return self.diameter

    def get_desnity(self):
        '''
        returns the density of the fluid in pipe'''
        return self.density

    def get_viscosity(self):
        '''
        returns the viscosity of the fluid in pipe'''
        return self.viscosity

    def reynolds_number(self):
        '''Calculates the Reynolds number for the data'''
        re_number = (self.density * self.velocity *
                     self.diameter) / (self.viscosity)
        return round(re_number, 2)
