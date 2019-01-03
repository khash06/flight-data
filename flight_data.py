import pandas as pd 
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import shapefile as shp

airlines = pd.read_csv('../flight-delays/airlines.csv')
airports = pd.read_csv('../flight-delays/airports.csv')
flights = pd.read_csv('../flight-delays/flights.csv')


m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')

m.drawcoastlines()
m.drawcountries()
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))

plt.show()
