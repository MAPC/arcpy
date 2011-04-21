"""

* delete all features in given feature class
* append features in given feature class

Note: ArcMap editing on ArcSDE is notoriously slow. Workaround is
to download the complete the entire feature class to a local file (FGDB) 
(versioned checkout was causing problems too), edit locally and update 
(dump and restore) entire database on SDE once local updates are finished.

Project: bike facility mapping
Author: Christian Spanring

"""

# Import arcpy module
import arcpy

# Local variables:
fc_sde = 'Database Connections/mysdeconnection.sde/mysdefeatureclass'
fc_local = 'C:/myfgdb.gdb/mylocalfeatureclass'

# Process: Delete Features
print 'deleting features in', fc_sde
arcpy.DeleteFeatures_management(fc_sde)

# Process: Append
print 'appending', fc_local, 'to', fc_sde
arcpy.Append_management(fc_local, fc_sde, 'NO_TEST', '', '')

