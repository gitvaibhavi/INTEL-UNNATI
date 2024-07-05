# INTEL-UNNATI

# GPS Toll Based System

This project simulates a GPS toll-based system that calculates the toll for a vehicle based on its path through predefined toll zones.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Toll Zones](#toll-zones)
- [Toll Rates](#toll-rates)
- [Functions](#functions)
  - [is_in_toll_zone](#is_in_toll_zone)
  - [calculate_toll](#calculate_toll)
  - [plot_toll_system](#plot_toll_system)


## Introduction

The GPS Toll Based System calculates the toll for a vehicle's path based on predefined toll zones and their respective toll rates. The system also visualizes the vehicle's path and the toll zones on a map.

## Installation

To run the script, you'll need to have Python installed on your system along with the following libraries:

- `geopy`
- `matplotlib`

You can install these libraries using pip:

```bash
pip install geopy matplotlib
```

## Usage

1. Define the toll zones and their respective rates.
2. Simulate the vehicle's path as a sequence of GPS coordinates.
3. Use the `calculate_toll` function to calculate the total toll for the vehicle's path.
4. Use the `plot_toll_system` function to visualize the toll zones and the vehicle's path.

Run the script using:

```bash
python gps1.py
```

## Toll Zones

The toll zones are defined as a set of coordinates (latitude, longitude) for each zone:

```python
toll_zone = {
    "zone_1": [(37.7749, -122.4194), (37.7849, -122.4094)],
    "zone_2": [(34.0522, -118.2437), (34.0622, -118.2337)],
    "zone_3": [(20.593684, 78.96288), (20.593684, 78.96288)],
    "zone_4": [(18.987807, 72.836447), (18.987807, 72.836447)],
    "zone_5": [(28.651952, 77.231495), (28.651952, 77.231495)],
    "zone_6": [(22.562627, 88.363044), (22.562627, 88.363044)],
    "zone_7": [(13.084622, 80.248357), (13.084622, 80.248357)],
    "zone_8": [(12.977063, 77.587106), (12.977063, 77.587106)]
}
```

## Toll Rates

The toll rates for each zone are defined as follows:

```python
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
```

## Functions

### `is_in_toll_zone`

This function checks if a vehicle is within a toll zone based on its coordinates.

```python
def is_in_toll_zone(vehicle_location, zone_coordinates):
    (lat1, lon1), (lat2, lon2) = zone_coordinates
    return (lat1 <= vehicle_location[0] <= lat2) and (lon1 <= vehicle_location[1] <= lon2)
```

### `calculate_toll`

This function calculates the total toll for a vehicle's path.

```python
def calculate_toll(vehicle_path):
    total_toll = 0
    for location in vehicle_path:
        for zone, coordinates in toll_zone.items():
            if is_in_toll_zone(location, coordinates):
                total_toll += toll_rates[zone]
                break
    return total_toll
```

### `plot_toll_system`

This function visualizes the toll zones and the vehicle's path on a map.

```python
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
    ax.set_title("GPS Toll Based System Simulation")
    ax.legend()
    plt.show()
```

This README provides a comprehensive overview of the script, including installation instructions, usage guidelines, and descriptions of the main components.
