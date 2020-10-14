import math
mono_deflection = float(input('Enter the monometer deflection?'))
mono_angle = float(input('Enter the angle of monometer?'))
mono_angle = math.radians(mono_angle)
y_water = 9790

pressure_dif = []
while mono_deflection != 0:
    delta_p = (y_water) * (mono_deflection*(10**-3)) * math.sin(mono_angle)
    pressure_dif.append(round(delta_p, 2))
    mono_deflection = float(input('Enter the monometer deflection'))

for i in pressure_dif:
    print(i)
