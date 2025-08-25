import arcpy_metadata

# Define input and output layers
line_layer = "lines_data.shp"  # Replace with your line shapefile
polygon_layer = "WATER_Catchments_AllIsland.shp"  # Replace with your polygon shapefile
output_layer = "lines_with_polygon_ids.shp"

# Perform spatial join
arcpy_metadata.analysis.SpatialJoin(
    target_features=line_layer,
    join_features=polygon_layer,
    out_feature_class=output_layer,
    join_type="KEEP_COMMON",  # Keep only matching features
    match_option="INTERSECT"  # Use Intersect as the spatial relationship
)

print(f"Spatial join completed. Output saved to {output_layer}")