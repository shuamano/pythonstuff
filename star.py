from skyfield.api import N, W, wgs84

boston = earth + wgs84.latlon(42.3583 * N, 71.0636 * W)
astrometric = boston.at(t).observe(mars)
alt, az, d = astrometric.apparent().altaz()

print(alt)
print(az)