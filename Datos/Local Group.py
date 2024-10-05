import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Diccionario de estrellas
stars = {
    "Milky Way": {"distance_ly": 26000, "ra": 266.4051, "dec": -29.0078},
    "Earth": {"distance_ly": 0, "ra": 0, "dec": 0},
    "Andromeda Galaxy": {"distance_ly": 2530000, "ra": 10.6847, "dec": 41.2692},
    "Triangulum Galaxy": {"distance_ly": 3000000, "ra": 23.4622, "dec": 30.6592},
    "Large Magellanic Cloud": {"distance_ly": 163000, "ra": 80.8942, "dec": -69.7561},
    "Small Magellanic Cloud": {"distance_ly": 200000, "ra": 13.1869, "dec": -72.8286},
    "Canis Major Dwarf Galaxy": {"distance_ly": 25000, "ra": 122.2144, "dec": -8.3789},
    "Leo I Dwarf Galaxy": {"distance_ly": 820000, "ra": 152.1175, "dec": 12.3064},
    "Leo II Dwarf Galaxy": {"distance_ly": 690000, "ra": 168.7392, "dec": 22.1514},
    "Sculptor Dwarf Galaxy": {"distance_ly": 280000, "ra": 15.0592, "dec": -33.7083},
    "Fornax Dwarf Galaxy": {"distance_ly": 1470000, "ra": 39.9942, "dec": -34.4506},
    "Ursa Minor Dwarf Galaxy": {"distance_ly": 225000, "ra": 227.2425, "dec": 67.2203},
    "Draco Dwarf Galaxy": {"distance_ly": 260000, "ra": 260.0500, "dec": 57.9153},
    "Carina Dwarf Galaxy": {"distance_ly": 330000, "ra": 115.7050, "dec": -50.7422},
    "Sextans Dwarf Galaxy": {"distance_ly": 2400000, "ra": 153.7250, "dec": -1.4761},
    "Phoenix Dwarf Galaxy": {"distance_ly": 1400000, "ra": 354.2875, "dec": -54.4153},
    "Tucana Dwarf Galaxy": {"distance_ly": 880000, "ra": 343.4950, "dec": -58.5244},
    "Cetus Dwarf Galaxy": {"distance_ly": 800000, "ra": 19.4250, "dec": -17.4661},
    "Pegasus Dwarf Irregular Galaxy": {"distance_ly": 3000000, "ra": 23.4622, "dec": 14.4272},
    "Leo A Dwarf Galaxy": {"distance_ly": 2000000, "ra": 142.6900, "dec": 17.1661},
    "Leo T Dwarf Galaxy": {"distance_ly": 4200000, "ra": 150.1000, "dec": 17.4750},
    "Aquarius Dwarf Galaxy": {"distance_ly": 1600000, "ra": 305.4250, "dec": -12.5456},
    "Bootes I Dwarf Galaxy": {"distance_ly": 197000, "ra": 209.0250, "dec": 14.5139},
    "Bootes II Dwarf Galaxy": {"distance_ly": 420000, "ra": 209.0250, "dec": 12.8667},
    "Canes Venatici I Dwarf Galaxy": {"distance_ly": 720000, "ra": 202.5250, "dec": 33.5500},
    "Canes Venatici II Dwarf Galaxy": {"distance_ly": 1600000, "ra": 194.9250, "dec": 34.3200},
    "Coma Berenices Dwarf Galaxy": {"distance_ly": 44000, "ra": 185.9250, "dec": 23.4639},
    "Hercules Dwarf Galaxy": {"distance_ly": 430000, "ra": 247.7000, "dec": 12.7850},
    "Leo IV Dwarf Galaxy": {"distance_ly": 160000, "ra": 160.1750, "dec": -0.6672},
    "Leo V Dwarf Galaxy": {"distance_ly": 700000, "ra": 172.9250, "dec": 2.2200},
}

#Grafica 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# RA y DEC
ra = [star["ra"] for star in stars.values()]
dec = [star["dec"] for star in stars.values()]
dist = [star["distance_ly"] for star in stars.values()]

#Plot
colors = []
sizes = []
highlighted_stars = ["Small Magellanic Cloud", "Large Magellanic Cloud"]
mkwy = ["Milky Way"]
eth = ["Earth"]

for star_name in stars:
    if star_name in stars:
        colors.append('r')
        sizes.append(100)
    else:
        if star_name in mkwy:
            colors.append('y')
            sizes.append(10)
        else:
            if star_name in eth:
                colors.append('g')
                sizes.append(50)
            else:
                colors.append('g')
                sizes.append(20)

ax.scatter(ra, dist, c=colors, s=sizes)

#Titulos
ax.set_xlabel('RA')
ax.set_ylabel('DEC')
ax.set_zlabel('Distancia (ly)')
plt.title('Grupo Local')

#Show
plt.show()