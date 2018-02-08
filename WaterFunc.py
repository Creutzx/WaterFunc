"""uses a basemap, adds a layer file with the environmental characteristics that are sought
Basemap is watershed boundary, NHD streamlines, scale bar, and north arrow.
A layer (.lyr) file is added to show the desired environmental attribute."""

def waterfunc(lyr_name):
    import arcpy
    import os

    str_dir_main = r"\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps"
    str_mxd_blank = r"Upper_Yaquina_TMDL_Blank_ME.mxd"
    str_df_cur = r"Layers"
    str_mxd_save_pre = r"Upper_Yaquina_TMDL_UY_"
    str_mxd_save_post = r".mxd"
    lyr_save_pre = r"UY_"
    lyr_save_post = r".lyr"

    mxd = arcpy.mapping.MapDocument(str_dir_main + "\\" + str_mxd_blank)
    df = arcpy.mapping.ListDataFrames(mxd, str_df_cur)[0]
    str_layerfile = os.path.join(str_dir_main, lyr_save_pre + lyr_name + lyr_save_post)
    addlayer = arcpy.mapping.Layer(str_layerfile)
    arcpy.mapping.AddLayer(df, addlayer, "BOTTOM")
    arcpy.RefreshTOC()
    arcpy.RefreshActiveView()
    mxd.saveACopy(str_dir_main + "\\" + str_mxd_save_pre + lyr_name + str_mxd_save_post)

    del addlayer, df, mxd

"""Function calls for the following abbreviated names of environmental attributes:
Abbreviation            Attribute
Geo                     Geology
Elev                    Elevation
Precip                  Precipitation"""

waterfunc(lyr_name = "Geo")
waterfunc(lyr_name = "Elev")
waterfunc(lyr_name = "Precip")
