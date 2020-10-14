# This Program calculates the pressure difference as a function of a manometer deflection and angle

import math
mono_deflection = input('Enter the monometer deflection? (Seperated by commas)').split(
    ',')  # Manometer deflection in mm and split with comma
# manometer angel with horizontal in degrees
mono_angle = float(input('Enter the angle of monometer?'))
mono_angle = math.radians(mono_angle)  # convert degrees to Radians
y_water = 9790  # Specific weight of water

pressure_dif = []
for deflection in mono_deflection:
    deflection = float(deflection)
    delta_p = (y_water) * (deflection*(10**-3)) * math.sin(mono_angle)
    pressure_dif.append(round(delta_p, 2))

for i in pressure_dif:
    print(i)
