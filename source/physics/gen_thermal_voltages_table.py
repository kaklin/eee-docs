from scipy.constants import k, e
# k = scipy.constants.k
# q = scipy.constants('e')


def celsius_to_kelvin(C):
    return C + 273.15


def kelvin_to_celsius(K):
    return K - 273.15


def thermal_voltage(T):
    return k * T / e


# print(thermal_voltage(celsius_to_kelvin(25)))
output_string = '{},{},{:.2f}mV\n'
with open('thermal_voltages.csv', 'w') as csv:
    for temp in [-55, -40, 0, 25, 27, 70, 85, 125]:
        csv.write(output_string.format(celsius_to_kelvin(temp), temp, 1e3*thermal_voltage(celsius_to_kelvin(temp))))
