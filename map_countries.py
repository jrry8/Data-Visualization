import pygal

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Americas'
worldmap_chart.add('North America', ['ca', 'mx', 'us'])
worldmap_chart.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
worldmap_chart.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
 'gy', 'pe', 'py', 'sr', 'uy', 've'])
worldmap_chart.render_to_file('americas.svg')