import csv
from gmplot import gmplot

# Create a Google Map plotter
gmap = gmplot.GoogleMapPlotter(28.689169, 77.321648, 17)  # Set the center coordinates and zoom level

# Set the path to your Google Maps API key if required
# gmap.apikey = 'your_google_maps_api_key_here'

# Load and process the CSV data
with open('route.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header if it exists

    for row in reader:
        lat, long = float(row[0]), float(row[1])

        # Plot markers with different colors
        if reader.line_num == 2:  # First coordinate
            gmap.marker(lat, long, color='yellow')
        else:
            gmap.marker(lat, long, color='blue')

        last_coordinates = (lat, long)

    # Mark the last coordinate as red
    gmap.marker(last_coordinates[0], last_coordinates[1], color='red')

# Draw the map and save it to an HTML file
gmap.draw('route_map.html')

print("Map plotted successfully. Check 'route_map.html' for the route visualization.")