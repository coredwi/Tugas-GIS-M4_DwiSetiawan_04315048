import mapnik
m = mapnik.Map(1920,1080)
m.background = mapnik.Color('cyan')

#JAPAN ADMINISTRATIVE
s = mapnik.Style()
r = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#a0a0a0')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('yellow'), 5)
line_symbolizer.stroke_width = 50.0
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style1',s)
ds = mapnik.Shapefile(file="JPN_adm/JPN_adm0.shp")
layer = mapnik.Layer('jpn_adm')
layer.datasource = ds
layer.styles.append('My Style1')
m.layers.append(layer)


#JAPAN ADMINISTRATIVE 2
s = mapnik.Style()
r = mapnik.Rule()

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#d9d9d9')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
r.symbols.append(line_symbolizer) 
s.rules.append(r)

m.append_style('My Style5',s)
ds = mapnik.Shapefile(file="JPN_adm/JPN_adm1.shp")
layer = mapnik.Layer('jpn_adm2')
layer.datasource = ds
layer.styles.append('My Style5')
m.layers.append(layer)


#JAPAN ROADS
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 1)
r.symbols.append(line_symbolizer) 
s.rules.append(r)

m.append_style('My Style6',s)
ds = mapnik.Shapefile(file="JPN_rds/JPN_roads.shp")
layer = mapnik.Layer('jpn_roads')
layer.datasource = ds
layer.styles.append('My Style6')
m.layers.append(layer)


#JAPAN WATER AREA
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'), 1)
line_symbolizer.stroke_width =  5.0
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="JPN_wat/JPN_water_areas_dcw.shp")
layer = mapnik.Layer('japan_water_area')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)


#JAPAN WATER LINES
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'), 1)
r.symbols.append(line_symbolizer) 
s.rules.append(r)

m.append_style('My Style3',s)
ds = mapnik.Shapefile(file="JPN_wat/JPN_water_lines_dcw.shp")
layer = mapnik.Layer('jpn_water_lines')
layer.datasource = ds
layer.styles.append('My Style3')
m.layers.append(layer)


#JAPAN RAILROADS
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('black'), 1)
r.symbols.append(line_symbolizer) 
s.rules.append(r)

m.append_style('My Style4',s)
ds = mapnik.Shapefile(file="JPN_rrd/JPN_rails.shp")
layer = mapnik.Layer('jpn_railroads')
layer.datasource = ds
layer.styles.append('My Style4')
m.layers.append(layer)


m.zoom_all()
mapnik.render_to_file(m, 'japan.pdf', 'pdf')
print "rendered image to 'japan.pdf' "

#JPEG