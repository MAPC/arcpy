"""

Problem: get all layer sources from a map document
Solution: write a txt file 

Project: Small GIS request
Author: Christian Spanring

"""

import arcpy, sys, os

mxd = arcpy.mapping.MapDocument(sys.argv[1])
df = arcpy.mapping.ListDataFrames(mxd)[0]

filename = '%s_layer-sources.txt' % (os.path.basename(mxd.filePath)[:-4])

file = open(filename,'w')

for lyr in arcpy.mapping.ListLayers(mxd, '', df):
    if not lyr.isGroupLayer:
        print >>file, lyr.dataSource

print 'Create layer-sources-list in %s' % (os.path.abspath(filename))

file.close()

del mxd
