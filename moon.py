from skyfield.api import load, N, W, wgs84

# Create a timescale and ask the current time.
ts = load.timescale()
t = ts.now()

	object = input('planet?\n')

# Load the JPL ephemeris DE421 (covers 1900-2050).
planets = load('de421.bsp')
earth, mars, moon = planets['earth'], planets['mars'], planets['moon']


cincinnati = earth + wgs84.latlon(39.20709055126398 * N, 84.44333871312355 * W)
astrometric = cincinnati.at(t).observe(planet)
alt, az, d = astrometric.apparent().altaz()

print(alt)
print(az)

39.20709055126398, -84.44333871312355