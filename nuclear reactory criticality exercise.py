def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    return False

    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
#This is the correct answer. I was overcoplicating tis once again. Refer to this for later issues. 
    def reactor_efficiency(voltage, current, theoretical_max_power):
    efficiency = (voltage * current) / theoretical_max_power

    if efficiency >= 0.80:
        return 'green'
    if 0.60 <= efficiency < 0.80:
        return 'orange'
    if 0.30 <= efficiency < 0.60:
        return 'red'
    return 'black'


# oRIGINAL EXAMPLE COMMENTED OUT TO FIX FOR TEST
#     def reactor_efficiency(voltage, current, theoretical_max_power):
#         if ((voltage * current) / theoretical_max_power)*100 >= .80
#             return 'green'
#         elif ((voltage * current) / theoretical_max_power)*100 >= .60
#             return 'orange'
#         elif ((voltage * current) / theoretical_max_power)*100 >= .30
#             return 'red'
#         else: 
#             return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    status = (temperature * neutrons_produced_per_second) 

    if status < (.90 * threshold):
        return 'LOW'
    if (.90 * threshold) <= status <= (1.10 * threshold)  #PAY ATTENTION to this part. This simplified way of writing the maths here we need ingraned in our process. 
        return 'NORMAL'
    return 'DANGER'