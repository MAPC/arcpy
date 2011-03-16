"""

Problem: many seperate Shapefiles belong to one layer. Shapefile-filenames indicate featurenames.
Solution: add Shapefile-filename as attribute to attribute-table and parse feature-name there.

* loops through the directory "shapefiles", adds the field "filename" to each Shapefile and writes the Shapefile-filename into the field

Project: Bikemapping
Author: Christian Spanring

"""

import os, arcpy

# we're only looking for shapefiles
extension = "shp"

count = 0

# loop through files directory
for feature_class in (f for f in os.listdir("shapefiles") if f.endswith(extension) ):
	
	# Process: Add Field
	arcpy.AddField_management("shapefiles/" + feature_class, "filename", "TEXT", "", "", "", "", "NON_NULLABLE", "NON_REQUIRED", "")

	# Process: Calculate Field
	arcpy.CalculateField_management("shapefiles/" + feature_class, "filename", "feature_class[:-4]" , "PYTHON", "")
	
	count += 1
	
	print(feature_class[:-4]), "processed"

print count, "files processed."