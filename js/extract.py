import pandas as pd
import re

df = pd.read_csv('bali_tourism.csv')

latitudes = []
longitudes = []



# Regular expression pattern to match latitude and longitude
pattern = r"([-+]?\d+\.\d+)°?\s*([NS])?,?\s*([-+]?\d+\.\d+)°?\s*([EW])?"

# Function to extract latitude and longitude from a given coordinate string
def extract_lat_lon(coord_str):
    match = re.search(pattern, coord_str)
    if match:
        lat_deg = float(match.group(1))
        lat_dir = match.group(2)
        lon_deg = float(match.group(3))
        lon_dir = match.group(4)
        
        # Convert latitude and longitude to decimal format
        if lat_dir == 'S':
            lat_deg = -lat_deg
        if lon_dir == 'W':
            lon_deg = -lon_deg
        
        return lat_deg, lon_deg
    else:
        return None
# Extract latitude and longitude from each coordinate
for coord in df['Coordinate']:
    result = extract_lat_lon(coord)
    if result:
        lat, lon = result
        latitudes.append(lat)
        longitudes.append(lon)
    else:
         latitudes.append(None)
         longitudes.append(None)

df['Latitude'] = latitudes
df['Longitude'] = longitudes

df.to_csv('updated_file.csv', index=False)

