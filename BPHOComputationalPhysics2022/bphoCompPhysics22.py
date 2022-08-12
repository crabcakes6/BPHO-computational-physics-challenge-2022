# %%

import matplotlib.pyplot as plt
import math

plt.xlabel("altitude",fontsize=18)
plt.ylabel("tboil",fontsize=18)

U = [0,0.25,0.5,0.75,1]
iU = 1 #ind variable

g = 9.8076

temperature = 15 #celcius
h = 0 #km
pressure = 1013.25 #mbar
hh = 0.01 #delta h
x = []
y = []

for i in range(2000):

  saturation = 6.1121 * (math.e**( (18.678-(temperature)/234.5)*(temperature/(temperature + 257.14)))) 

  r = ((287/461.5)*(iU*saturation)) / (pressure-(iU*saturation))

  lapseRate = g * ((1 + ((r*2501000)/(287*(temperature+273)))) / (1003.5 + (((2501000**2)*r))/(461.5*((temperature+273)**2)))) *1000
  p = -((0.02896*g)/(8.314*(temperature+273)))*(pressure-iU*(1-(0.01802/0.02896)*saturation))*hh 
  tBoil = (((1/100) - ((8.314/45.07) * math.log((pressure/1013.25), math.e)))**-1)
  tDew = (243.04*(math.log(iU)+((17.625*temperature)/(243.04+temperature)))) / (17.625-math.log(iU)-((17.625*temperature)/(243.04+temperature)))

  h += hh
  temperature = (temperature - lapseRate * hh)
  pressure += p

  x.append(h)
  y.append(tDew)

#plt.ylim([0, 10])
plt.plot(x, y)
plt.show()

# %%