from pygal.maps.world import COUNTRIES

code = dict()
for k, v in COUNTRIES.items():
    code[v] = k

# returns pygal 2-digit country code
def get_country_code(country_name):
    return code.get(country_name)