import pandas as pd
import folium
import geopandas as gpd
from shapely.geometry import LineString

# Load the data
file_path = "Coordinates.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path, sheet_name="Cleaned Data", header=None)
df = df.dropna()
print(df)
def parse_coordinates(row):
    coords = []
    for i in range(0, len(row), 2):
        try:
            # Convert values to float
            lat = float(row[i])
            lon = float(row[i + 1])
            coords.append((lat, lon))
        except (ValueError, TypeError):
            # Skip invalid pairs
            continue
    return coords if len(coords) > 1 else None  # Return None if there are not enough valid points

# Parse all rows into lines
lines = df.apply(parse_coordinates, axis=1)
 # Remove rows with None
print(lines)
# Convert parsed lines to GeoDataFrame
geometries = [LineString(line) for line in lines if line and len(line) > 1]  # Create LineString objects
gdf = gpd.GeoDataFrame({"geometry": geometries}, crs="EPSG:4326")  # Use WGS 84 CRS

# Reproject to a metric CRS for accurate buffering (e.g., UTM or Irish Grid TM65)
gdf_metric = gdf.to_crs("EPSG:29902")  # Reproject to Irish TM65 CRS
buffer_gdf_metric = gdf_metric.copy()
buffer_gdf_metric["geometry"] = buffer_gdf_metric.geometry.buffer(100)  # 100 meters in metric units

# Save the buffered areas as a shapefile
output_shp = "lines_buffer_100m_tm65.shp"
buffer_gdf_metric.to_file(output_shp)

print(f"Buffered shapefile saved as {output_shp}")
# Save the GeoDataFrame as a shapefile
output_shp = "lines_data.shp"  # Output shapefile path
gdf.to_file(output_shp)
print(f"Shapefile saved as {output_shp}")

#print(f"Shapefile saved as {output_shp} in Irish Grid (TM65) CRS.")