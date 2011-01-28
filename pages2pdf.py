"""

* adjusts page to max scale of 1:30k
* exports Data Driven Pages to single PDF documents (300dpi by default)

Usage: python pages2pdf.py mxd-file output-directory

Project: Bikemapbook
Author: Christian Spanring

"""

import arcpy, os, string, sys

# usage help
if sys.argv[1] in ("-h", "--help"):
    print "Usage: python pages2pdf.py mxd-file output-directory"
    sys.exit()

# get map document
mxd = arcpy.mapping.MapDocument(sys.argv[1])

# check for page-name field 'page'
try:
    pageName = str(mxd.dataDrivenPages.pageRow.pagename)
except:
    print "No 'pagename'-field found, using default pagename."

# loop through all mapbook pages
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
    
    # set mapbook page
    mxd.dataDrivenPages.currentPageID = pageNum
    
    # get DataFrame
    df = arcpy.mapping.ListDataFrames(mxd)[0]

    # set a minimun scale of 1:30000
    # TODO: add argument for max scale
    if df.scale < 30000 :
        df.scale = 30000

    # output while exporting
    try:
        pageName = str(mxd.dataDrivenPages.pageRow.pagename).replace(" ", "_")
        arcpy.AddMessage("Exporting " + pageName + " " + str(pageNum) + " of " + str(mxd.dataDrivenPages.pageCount) + " at 1:" + str(df.scale))
    except:
        pageName = "Page-" + str(pageNum)
        arcpy.AddMessage("Exporting " + pageName + " of " + str(mxd.dataDrivenPages.pageCount) + " at 1:" + str(df.scale))
    
    # set pdf
    pdf = sys.argv[2] + pageName + ".pdf"
    
    # export map to pdf with some basic options
    # ExportToPDF (map_document, out_pdf, {data_frame}, {df_export_width}, {df_export_height}, {resolution}, {image_quality}, {colorspace}, {compress_vectors}, {image_compression}, {picture_symbol}, {convert_markers}, {embed_fonts}, {layers_attributes}, {georef_info}, {jpeg_compression_quality})
    arcpy.mapping.ExportToPDF(mxd, pdf, resolution=300)
    
# delete objects     
del mxd, df, pdf