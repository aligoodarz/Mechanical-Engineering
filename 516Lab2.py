import matplotlib


def renumb():
    Q = input('Enter the flow rates seperated by commas')
    q_values = Q.split(',')
    renumblist = []
    ro = 998
    moo = 1.003 * (10 ** -3)
    area = 1.2668 * (10**-4)
    diameter = 0.0127
    for q in q_values:
        q = float(q)
        v = (q/1000)/area
        renumb = (ro * v * diameter) / (moo)
        renumblist.append(renumb)

    return renumblist


print(renumb())
