import json
import pygal

from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    data = json.load(f)

pops_low, pops_mid, pops_high = dict(), dict(), dict()
for dict in data:
    if dict['Year'] == '2010':
        country_name = dict['Country Name']
        population = int(float(dict['Value']))
        code = get_country_code(country_name)
        if code:
            if population < 10000000:
                pops_low[code] = population
            elif population < 1000000000:
                pops_mid[code] = population
            else:
                pops_high[code] = population

wm = pygal.maps.world.World()
wm.title = 'Country Populations in 2010'
wm.add('<10m', pops_low)
wm.add('10m-1bn', pops_mid)
wm.add('>1bn', pops_high)
wm.render_to_file('world_pop.svg')
