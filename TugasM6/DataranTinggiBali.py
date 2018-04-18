import mapnik
m = mapnik.Map(720,480)
m.background = mapnik.Color('red')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#fcff00')
r.symbols.append(polygon_symbolizer) 

#######
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('black'), 0.2)
line_symbolizer.stroke_width =  5.0

r.symbols.append(line_symbolizer) 

#point_sym = mapnik.PointSymbolizer()
#point_sym.allow_overlap = True
#r.symbols.append(point_sym) 

s.rules.append(r)

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_provinsi/INDONESIA_PROP.shp")
layer = mapnik.Layer('Indo')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)


#######
r.symbols.append(line_symbolizer) 

point_sym = mapnik.PointSymbolizer()
point_sym.file = "/simbol.png"
point_sym.allow_overlap = True
point_sym.transform = "scale(0.02, 0.02)"
r.symbols.append(point_sym) 

s.rules.append(r)

m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="DataranTinggi/Coba.shp")
layer = mapnik.Layer('DataranTinggi')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)


#######
m.zoom_all()
mapnik.render_to_file(m, 'bali.pdf', 'pdf')
print "rendered image to 'SUKSES!!!' "

#PDF