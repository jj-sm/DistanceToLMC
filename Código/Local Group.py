import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Diccionario de Estrellas
stars = {
    "Milky Way": {"distance_ly": 26600, "ra": 266.4051, "dec": -29.0078},
    "Earth": {"distance_ly": 0, "ra": 266.4051, "dec": -29.0078},
    "Andromeda (M31)": {"distance_ly": 2200000, "ra": 10.6848, "dec": 41.2692},
    "Triangulum (M33)": {"distance_ly": 3000000, "ra": 23.4622, "dec": 30.6602},
    "The Milky Way Dwarf": {"distance_ly": 260000, "ra": 170.0965, "dec": -64.1813},
    "Sagittarius Dwarf Elliptical": {"distance_ly": 80000, "ra": 283.8329, "dec": -30.5453},
    "Small Magellanic Cloud": {"distance_ly": 200000, "ra": 18.8988, "dec": -73.0751},
    "Large Magellanic Cloud": {"distance_ly": 163000, "ra": 81.8951, "dec": -69.7561},
    "M32": {"distance_ly": 2600000, "ra": 10.6743, "dec": 40.8685},
    "M110": {"distance_ly": 2600000, "ra": 10.6847, "dec": 41.2698},
    "IC 10": {"distance_ly": 2550000, "ra": 0.4193, "dec": 59.1817},
    "NGC 185": {"distance_ly": 2510000, "ra": 5.5766, "dec": 48.3372},
    "IC 1613": {"distance_ly": 2530000, "ra": 18.1013, "dec": 2.1124},
    "Pegasus Dwarf Irregular": {"distance_ly": 3180000, "ra": 23.4708, "dec": 14.7743},
    "IC 5146": {"distance_ly": 2950000, "ra": 21.5795, "dec": 47.3643},
    "IC 342": {"distance_ly": 7750000, "ra": 3.2803, "dec": 68.7939},
    "Sextans A": {"distance_ly": 4300000, "ra": 10.1332, "dec": -4.7672},
    "Sextans B": {"distance_ly": 4750000, "ra": 10.1169, "dec": 0.9803},
    "WLM": {"distance_ly": 3150000, "ra": 0.7153, "dec": -15.4606},
    "NGC 6822": {"distance_ly": 1700000, "ra": 19.6146, "dec": -14.7936},
    "Phoenix Dwarf": {"distance_ly": 1540000, "ra": 1.2474, "dec": -44.3608},
    "Leo A": {"distance_ly": 2100000, "ra": 9.8729, "dec": 30.9897},
    "Leo I": {"distance_ly": 880000, "ra": 10.6657, "dec": 12.7142},
    "Leo II": {"distance_ly": 780000, "ra": 11.9663, "dec": 22.1552},
    "Tucana Dwarf": {"distance_ly": 2900000, "ra": 22.6533, "dec": -64.7825},
    "Carina Dwarf": {"distance_ly": 3300000, "ra": 6.4464, "dec": -50.9636},
    "Draco Dwarf": {"distance_ly": 2600000, "ra": 17.7656, "dec": 57.9154},
    "Ursa Minor": {"distance_ly": 2550000, "ra": 15.0991, "dec": 67.2196},
    "Hercules Dwarf": {"distance_ly": 1600000, "ra": 16.7109, "dec": 12.7961},
    "Fornax Dwarf": {"distance_ly": 462000, "ra": 2.5625, "dec": -34.4508},
    "Sculptor Dwarf": {"distance_ly": 2900000, "ra": 1.0109, "dec": -33.7081},
    "Sextans Dwarf Sph": {"distance_ly": 4200000, "ra": 10.2063, "dec": -1.5936},
    "Antlia Dwarf": {"distance_ly": 2600000, "ra": 10.2856, "dec": -27.3242},
    "NGC 147": {"distance_ly": 2480000, "ra": 0.4078, "dec": 48.6024},
    "NGC 185": {"distance_ly": 2510000, "ra": 5.5766, "dec": 48.3372},
    "NGC 205": {"distance_ly": 2480000, "ra": 0.4163, "dec": 41.4197},
    "NGC 6822": {"distance_ly": 1700000, "ra": 19.6146, "dec": -14.7936},
    "SagDIG": {"distance_ly": 3940000, "ra": 19.4250, "dec": -17.7686},
    "LGS 3": {"distance_ly": 2080000, "ra": 1.3081, "dec": 22.7683},
    "IC 5152": {"distance_ly": 2600000, "ra": 22.3203, "dec": -51.8236},
    "Pisces I": {"distance_ly": 3200000, "ra": 0.3588, "dec": 5.7025},
    "Andromeda I (M32)": {"distance_ly": 2600000, "ra": 0.7051, "dec": 40.8283},
    "Andromeda II": {"distance_ly": 2600000, "ra": 1.1854, "dec": 38.0086},
    "Andromeda III": {"distance_ly": 2540000, "ra": 0.2402, "dec": 36.3483},
    "Andromeda IV": {"distance_ly": 2760000, "ra": 2.2645, "dec": 47.5503},
    "Andromeda V": {"distance_ly": 2970000, "ra": 0.8277, "dec": 44.3133},
    "Andromeda VI (CasIV)": {"distance_ly": 2980000, "ra": 1.1018, "dec": 45.4708},
    "Andromeda VII (Cassiopeia VII)": {"distance_ly": 2980000, "ra": 2.2725, "dec": 50.3311},
    "Andromeda VIII (Cassiopeia VIII)": {"distance_ly": 2940000, "ra": 1.4345, "dec": 49.5692},
    "Andromeda IX (Cassiopeia IX)": {"distance_ly": 2810000, "ra": 1.0077, "dec": 43.5003},
    "Andromeda X (Cassiopeia X)": {"distance_ly": 2750000, "ra": 2.5166, "dec": 46.0319},
    "Andromeda XI (Cassiopeia XI)": {"distance_ly": 2890000, "ra": 2.1247, "dec": 44.0625},
    "Andromeda XII (Cassiopeia XII)": {"distance_ly": 2720000, "ra": 2.3166, "dec": 42.8953},
    "Andromeda XIII (Cassiopeia XIII)": {"distance_ly": 2760000, "ra": 1.3677, "dec": 41.2028},
}

# Plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Ra y dec
ra = [star["ra"] for star in stars.values()]
dec = [star["dec"] for star in stars.values()]
dist = [star["distance_ly"] for star in stars.values()]

# Plot 3d
colors = []
sizes = []
highlighted_stars = ["Small Magellanic Cloud", "Large Magellanic Cloud"]
mkwy = ["Milky Way"]
eth = ["Earth"]

for star_name in stars:
    if star_name in highlighted_stars:
        colors.append('r') 
        sizes.append(100)  
    else:
        if star_name in mkwy:
            colors.append('y') 
            sizes.append(100)  
        else:
            if star_name in eth:
                colors.append('g')
                sizes.append(50)
            else:
                colors.append('b') 
                sizes.append(20)   


ax.scatter(ra, dec, dist, c=colors, s=sizes)

# Titulos
ax.set_xlabel('RA')
ax.set_ylabel('DEC')
ax.set_zlabel('Distancia (ly)')
plt.title('Grupo Local')

# Show
plt.show()
