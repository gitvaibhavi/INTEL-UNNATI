import geopy.distance
import matplotlib.pyplot as plt #used to draw lines, diagrams and charts

# Define toll zone as a set of coordinates (latitude, longitude)
toll_zone = {
    "zone_1": [(37.7749, -122.4194), (37.7849, -122.4094)],  # San Francisco example coordinates
    "zone_2": [(34.0522, -118.2437), (34.0622, -118.2337)],   # Los Angeles example coordinates
    "zone_3": [(20.593684, 78.96288), (20.593684, 78.96288)], # India example coordinates
    "zone_4": [(18.987807, 72.836447), (18.987807, 72.836447)], # Mumbai example coordinates
    "zone_5": [(28.651952, 77.231495), (28.651952, 77.231495)], # Delhi example coordinates
    "zone_6": [(22.562627, 88.363044), (22.562627, 88.363044)], # Kolkata example coordinates
    "zone_7": [(13.084622, 80.248357), (13.084622, 80.248357)], # Chennai example coordinates
    "zone_8": [(12.977063, 77.587106), (12.977063, 77.587106)] # Bengalūru example coordinates
}

# Define toll rates for each zone
toll_rates = {
    "zone_1": 2.5,
    "zone_2": 3.5,
    "zone_3": 4.5,
    "zone_4": 5.5,
    "zone_5": 6.5,
    "zone_6": 7.5,
    "zone_7": 8.5,
    "zone_8": 9.5
}

# Function to check if a vehicle is within a toll zone
def is_in_toll_zone(vehicle_location, zone_coordinates):
    (lat1, lon1), (lat2, lon2) = zone_coordinates
    return (lat1 <= vehicle_location[0] <= lat2) and (lon1 <= vehicle_location[1] <= lon2)

# Function to calculate toll for a vehicle's path
def calculate_toll(vehicle_path):
    total_toll = 0
    for location in vehicle_path:
        for zone, coordinates in toll_zone.items():
            if is_in_toll_zone(location, coordinates):
                total_toll += toll_rates[zone]
                break  # Assume each point can only be in one zone at a time
    return total_toll

# Simulate vehicle path (sequence of GPS coordinates)
vehicle_path = [
    (22.562627, 88.363044),
    (12.977063, 77.587106),
    (34.0523, -118.2438),
    (34.0623, -118.2338)
]

# Calculate toll for the simulated path
total_toll = calculate_toll(vehicle_path)
print(f"Total toll for the vehicle's path: ${total_toll:.2f}")
# Function to plot toll zones and vehicle path
def plot_toll_system(vehicle_path):
    fig, ax = plt.subplots()
    
    # Plot toll zones
    for zone, coordinates in toll_zone.items():
        (lat1, lon1), (lat2, lon2) = coordinates
        ax.plot([lon1, lon2], [lat1, lat2], 'ro-', label=f"{zone} Toll Zone")
    
    # Plot vehicle path
    lons, lats = zip(*vehicle_path)
    ax.plot(lons, lats, 'bo-', label="Vehicle Path")
    
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title("GPS TOLL BASED SYSTEM SIMULATION")
    ax.legend()
    plt.show()

# Visualize the path
plot_toll_system(vehicle_path)
