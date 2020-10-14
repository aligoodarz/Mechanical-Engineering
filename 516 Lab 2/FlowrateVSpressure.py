'''This program is made to plot the flow rate VS the pressure difference in the manometer'''

import matplotlib.pyplot as plt
from Flow import Flow
from Manometer import Manometer
flow_list = [0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2]
flow_rate_values = []

for flow in flow_list:      # This block creates a list with the flow rate values
    flow_object = Flow(flow, 12.7, 998, 1.003 * (10**-3))
    flow_rate_values.append(flow_object.get_flowrate())

deflection_list = [6, 23, 47, 77, 118, 157, 199, 265, 316, 396]
pressure_difference_values = []
for deflection in deflection_list:  # This block creates a list with pressure_difference values
    manometer = Manometer(9790, deflection, 45)
    pressure_difference_values.append(manometer.pressure_diff())

plt.plot(flow_rate_values, pressure_difference_values)  # This plots the graph
plt.show()
print('done')
