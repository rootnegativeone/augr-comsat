from skyfield.api import load
from skyfield.constants import C  # Ensure this constant is as expected
import sys  # Import sys to handle command line arguments

def light_travel_time(object1, object2):
    # Load data
    planets = load('de421.bsp')

    body1 = planets[object1]
    body2 = planets[object2]

    # Get today's date and time
    ts = load.timescale()
    t = ts.now()

    # Compute the positions
    position1 = body1.at(t)
    position2 = body2.at(t)

    # Calculate the distance between the two objects in astronomical units (AU)
    distance_au = (position1 - position2).distance().au

    # Calculate light travel time
    light_time_days = distance_au / 173.1446326742406  # Use explicit value for C
    light_time_minutes = light_time_days * 1440  # convert days to minutes

    print(f"Distance between {object1} and {object2} (AU): {distance_au}")
    print(f"Light travel time in minutes: {light_time_minutes}")

    return light_time_minutes

if __name__ == "__main__":
    # Check if two command line arguments are given
    if len(sys.argv) != 3:
        print("Usage: python script.py object1 object2")
        sys.exit(1)
    
    # Get celestial bodies from command line arguments
    object1 = sys.argv[1]
    object2 = sys.argv[2]

    # Calculate travel time
    travel_time = light_travel_time(object1, object2)
    print(f"The light travel time from {object1.capitalize()} to {object2.capitalize()} is approximately {travel_time:.2f} minutes.")

'''
Command Line Arguments: The script now takes two command line arguments representing the celestial bodies for which the light travel time is calculated. This is managed by the sys.argv list, where sys.argv[0] is the script name, and sys.argv[1] and sys.argv[2] are the first and second arguments, respectively.
Error Handling: The script checks if exactly two arguments are provided. If not, it prints a usage message and exits. This ensures the script is used correctly.
Integration Friendly: When imported into another script, the function light_travel_time(object1, object2) can be directly called with two string arguments representing the celestial bodies.

Usage:

python3 ./travelTime.py earth mars

from your_script_name import light_travel_time
travel_time = light_travel_time('earth', 'mars')
print(travel_time)


'''
