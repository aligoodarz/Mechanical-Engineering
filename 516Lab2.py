# This code calculates the Reynold Number for a set of flows from their Flow Rate (Q)
# NOTE : The information used here is for water and a pipe with a specified diameter. However these values can easily be changed for the user to choose them


def renumb():
    # Ask for the flow rates
    Q = input('Enter the flow rates seperated by commas')
    q_values = Q.split(',')         # Create a list with the flow rates
    renumblist = []  # Create a placeholder for reynolds numbers
    ro = 998                    # density of water
    moo = 1.003 * (10 ** -3)  # Viscosity of water
    area = 1.2668 * (10**-4)  # Area  of the tube
    diameter = 0.0127  # Diameter of the tube
    for q in q_values:
        q = float(q)                # Change str to float
        v = (q/1000)/area  # calculate flow velocity
        renumb = (ro * v * diameter) / (moo)  # calculate reynolds number
        renumblist.append(renumb)  # add number to the list

    return renumblist  # return the list
