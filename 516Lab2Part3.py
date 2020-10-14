import math
import matplotlib.pyplot as plt

pressure_data = [
    41.54,
    159.22,
    325.36,
    533.04,
    816.86,
    1086.84,
    1377.59,
    1834.48,
    2187.53,
    2741.34,
]
flow_rate_data = [
    0.02,
    0.04,
    0.06,
    0.08,
    0.1,
    0.12,
    0.14,
    0.16,
    0.18,
    0.2,
]
for i in flow_rate_data:
    i = i/60
plt.plot(flow_rate_data, pressure_data)
plt.xlabel('Flow Rate (litres/s)')
plt.ylabel('Pressure Difference(Pa)')
plt.show()
