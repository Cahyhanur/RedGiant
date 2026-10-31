date=input('Enter the date of today(day/month/year):')

colony=int(input('Enter total amount of colony:'))
oxygenlevel=eval(input('Enter the dome current oxygen level number in percentage:'))
pressurelevel=eval(input('Enter the dome current pressure level number in percentage(kPa):'))
PO2level=(oxygenlevel/100)*pressurelevel
temperature=eval(input('Enter the current temperature in the dome(Celcius):'))



'''
def calculate_oxygen(oxygenlevel):
    if oxygenlevel <= 12:
        if 
        return 'WARNING! OXYGEN LEVEL TOO LOW.CHANCE OF HYPOXIA TO THE COLONY,REQUESTING EMERGENCY REFILL OF OXYGEN GAS FROM EARTH'
    elif oxygenlevel <=30:
        return 'OXYGEN LEVEL ARE IN NORMAL CONDITION'
    else:
        return 'WARNING! OXYGEN LEVEL TOO HIGH.MAY CAUSE OXYGEN TOXICITY TO THE COLONY.REQUESTING OXYGEN REDUCTION FROM THE DOME'
'''
def calculate_PO2(pressure,oxygenlevel):
    if pressure <= 50:
        if oxygenlevel>40:
            return 'THE CONDITION OF ATMOSPHERE IN THE DOME IS IN GOOD CONDITON.'
        else:
            return 'WARNING! PRESSURE LEVEL IS TOO LOW,CHANCE OF EXTREME DECOMPRESSION,REQUESTING EMERGENCY HELP FROM EARTH'
    elif pressure <= 150:
        if oxygenlevel <10:
            return 'WARNING! OXYGEN LEVEL TOO LOW.CHANCE OF HYPOXIA TO THE COLONY,REQUESTING EMERGENCY REFILL OF OXYGEN GAS FROM EARTH'
        elif oxygenlevel <=25:
            return 'THE CONDITION OF ATMOSPHERE IN THE DOME IS IN GOOD CONDITON.'
        else:
            return 'WARNING! OXYGEN LEVEL TOO HIGH.MAY CAUSE OXYGEN TOXICITY TO THE COLONY.REQUESTING OXYGEN REDUCTION FROM THE DOME'
    elif pressure <= 200:
        if oxygenlevel <=8:
            return 'WARNING! OXYGEN LEVEL TOO LOW.CHANCE OF HYPOXIA TO THE COLONY,REQUESTING EMERGENCY REFILL OF OXYGEN GAS FROM EARTH'
        elif oxygenlevel <=12:
            return 'THE CONDITION OF ATMOSPHERE IN THE DOME IS IN GOOD CONDITON.'
        else:
            return 'WARNING! PRESSURE LEVEL OF THE DOME IS TOO HIGH.REQUESTING PRESSURE MIGITATION FROM THE DOME'

def calculate_temperature(temperature):
    if temperature <25:
        return 'very cold'