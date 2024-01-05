#Bryan F. Rocha, CISA3309_600_202230: Scripting Languages, instructor: Zechun Cao, 06/15/2022

#This program tries to simulate the control mechanism of an thermostate in only one instance.
#The thermostat has three exclusive settings: 1-A/C, 2-Heating, 0-None (or standby).
# It monitors the current temperature and turns on A/C or heater to control the indoor temperature then decides what to turn ON or OFF.
#In order to get this program working was neccesary to control the program flow using several forms of IFstatements.

#prompt and input thermostate state
thermostate = int(input('Set the thermostate to (1-AC, 2-Heating, 0-None): '))

#prompt and input low temperature
low = int(input('Low temperature for heating (F): '))

#prompt and input high temperature
high = int(input('High temperature for A/C (F): '))

#prompt and input AC state
ac = int(input('Is the AC on (1-Yes, 0-No): '))

#prompt and input heater state
heater = int(input('Is the Heater on (1-Yes, 0-No): '))

#prompt and input current temperature
temp = int(input('Current temperature (F):'))

#This is the first if statement with booleans for the AC
#If the current temperature is lower than the high value,If the A/C is OFF, then don’t change anything
if (thermostate == 1) and (ac == 0 and heater == 0) and (temp < high and temp > low ):
    print('[Settings= ',thermostate,'AC=OFF','Heater=OFF','Low =',low,' High=',high,'Temp=',temp,']')
    print('Temperature below the high setting')
    print('[Settings= ', thermostate, 'AC=OFF', 'Heater=OFF','Low =', low, ' High=', high, 'Temp=', temp, ']')

#If the current temperature is higher than the high value,If the A/C is OFF, then turn ON the A/C
elif (thermostate == 1) and(ac == 0 and heater == 0) and (temp > low and temp > high):
    print('[Settings= ', thermostate, 'AC=OFF','Heater=OFF','Low =', low, ' High=', high, 'Temp=', temp,']')
    print('***Turn on the AC\n','[Settings= ', thermostate, 'AC=ON','Heater=OFF','Low =', low, ' High=', high, 'Temp=', temp,']')

#If the current temperature is higher than the high value,If the A/C is ON, then don’t change anything
elif (thermostate == 1) and (ac == 1 and heater == 0) and (temp >= high ):
    print('[Settings= ',thermostate,'AC=ON','Heater=OFF','Low =',low,' High=',high,'Temp=',temp,']')
    print('[Settings= ', thermostate, 'AC=ON', 'Heater=OFF','Low =', low, ' High=', high, 'Temp=', temp, ']')

#If the current temperature is lower than the high value, If the A/C is ON, turn OFF the A/C
elif (thermostate == 1) and(ac == 1 and heater == 0) and (temp > low and temp < high):
    print('[Settings= ', thermostate, 'AC=ON','Heater=OFF','Low =', low, ' High=', high, 'Temp=', temp,']')
    print('***Turn off the AC\n','[Settings= ', thermostate, 'AC=OFF','Heater=OFF','Low =', low, ' High=', high, 'Temp=', temp,']')
#If A/C and Heater are ON displays a message
elif (thermostate == 1) and(ac == 1 and heater == 1):
    print('Sorry, only one can be ON at time, not both.')

#This is the second if statement with booleans for the Heater
#If the current temperature is higher than the low value,If the Heater is OFF, then don’t change anything
if (thermostate == 2) and (ac == 0 and heater == 0) and (temp <= high and temp >= low ):
    print('[Settings= ',thermostate,'AC=OFF','Heater=OFF','Low =',low,' High=',high,'Temp=',temp,']')
    print('Temperature above the low setting')
    print('[Settings= ', thermostate, 'AC=OFF','Heater=OFF','Low =', low, ' High=', high, 'Temp=', temp, ']')
#If the current temperature is lower than the low value,If the Heater is OFF, then turn ON the Heater
elif (thermostate == 2) and(ac == 0 and heater == 0) and (temp < low):
    print('[Settings= ', thermostate, 'AC=OFF','Heater=OFF','Low =', low, ' High=', high, 'Temp=', temp,']')
    print('***Turn on the Heating\n','[Settings= ', thermostate, 'AC=ON','Heater=OFF','Low =', low, ' High=', high, 'Temp=', temp,']')

#If the current temperature is lower than the low value,If the Heater is ON, then don’t change anything
elif (thermostate == 2) and (ac == 0 and heater == 1) and (temp <= low ):
    print('[Settings= ',thermostate,'AC=OFF','Heater=ON','Low =',low,' High=',high,'Temp=',temp,']')
    print('[Settings= ', thermostate, 'AC=OFF', 'Heater=ON','Low =', low, ' High=', high, 'Temp=', temp, ']')

#If the current temperature is higher than the low value, If the Heater is ON, turn OFF the A/C
elif (thermostate == 2) and(ac == 0 and heater == 1) and (temp > low ):
    print('[Settings= ', thermostate, 'AC=OFF','Heater=ON','Low =', low, ' High=', high, 'Temp=', temp,']')
    print('***Turn off the Heating\n','[Settings= ', thermostate, 'AC=OFF','Heater=OFF','Low =', low, ' High=', high, 'Temp=', temp,']')

#If A/C and Heater are ON displays a message
elif (thermostate == 2) and(ac == 1 and heater == 1):
    print('Sorry, only one can be ON at time, not both.')

#This is the last If statement, this one just prints a message
if thermostate == 0:
    print('Have a nice day.')

