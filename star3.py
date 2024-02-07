from skyfield.api import load, N, W, wgs84

# Create a timescale and ask the current time.
ts = load.timescale()
t = ts.now()

# Load the JPL ephemeris DE421 (covers 1900-2050).
planets = load('de421.bsp')
earth, mars = planets['earth'], planets['mars']


cincinnati = earth + wgs84.latlon(39.1031 * N, 84.5120 * W)
astrometric = cincinnati.at(t).observe(mars)
alt, az, d = astrometric.apparent().altaz()

print(alt)
print(az)