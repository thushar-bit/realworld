pressure =  eval(input('enter the pressure'))
volume = eval(input('enter the volume'))
celsius = eval(input('enter the temperature'))
constant = 8.314
temp = celsius + 273.15
n = (pressure * volume) / (constant * temp)
print(n)