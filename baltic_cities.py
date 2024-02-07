Riga = {'population': 609489, 'land area': 307}
Vilnius = {'population': 602430, 'land area': 401}

riga_population = Riga['population']
riga_land_area = Riga['land area']
riga_population_density = riga_population // riga_land_area
Vilnius_population = Vilnius['population']
Vilnius_land_area = Vilnius['land area']
vilnius_population_density = Vilnius_population // Vilnius_land_area

print(f"Riga:\n\tPopulation: {riga_population}\n\tLand Area: {riga_land_area}\n\tPopulation density: {riga_population_density} people Per square kilometer")
print(f"Vilnius:\n\tPopulation: {Vilnius_population}\n\tLand Area: {Vilnius_land_area}\n\tPopulation Density: {vilnius_population_density} people per square kilometer")
