"""

Problem: user wants to quickly group towns
Solution: PDF with one town per layer to check on/off (security ruled online-version out)

Project: Small GIS request
Author: Christian Spanring

"""

import arcpy

# the map document, dataframe, town feature class and town group layer
mxd = arcpy.mapping.MapDocument(r'C:/dev/python/arcpy/mxd/towns.mxd')
df = arcpy.mapping.ListDataFrames(mxd, 'Towns')[0]
fc = 'C:/dev/python/arcpy/shapefile/towns.shp'
townGroup = arcpy.mapping.ListLayers(mxd, "Town Layers", df)[0]

# search cursor
towns = arcpy.SearchCursor(fc)

for town in towns:

    townLayer = arcpy.mapping.Layer(r'C:/dev/python/arcpy/lyr/town-template.lyr')
	
    townName = town.getValue('name')
    
    # adjusting name and definition query
    townLayer.name = townName
    townLayer.definitionQuery = '"name" = \'' + townName + '\''
    
    # add layer to layergroup
    arcpy.mapping.AddLayerToGroup(df, townGroup, townLayer, "BOTTOM")
    print "added layer for %s" % (townName)

print "writing townlayers.mxd"
mxd.saveACopy(r'C:/dev/python/arcpy/mxd/townlayers.mxd')

print "exporting to townlayers.pdf"
arcpy.mapping.ExportToPDF(mxd, r'C:/dev/python/arcpy/pdf/townlayers.pdf', layers_attributes='LAYERS_ONLY' , resolution=300)

del mxd, df, fc, towns, townGroup, townLayer