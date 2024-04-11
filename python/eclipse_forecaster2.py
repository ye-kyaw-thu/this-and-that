"""
Try to forecast next eclipse date.
Written by Ye Kyaw Thu, LST Lab., Myanmar
Last updated: 11 April 2024

Reference:
https://pypi.org/project/ephem/

Usage:
python ./eclipse_forecaster2.py --help
python ./eclipse_forecaster2.py Mandalay Myanmar
python ./eclipse_forecaster2.py Bagan Myanmar
python ./eclipse_forecaster2.py Kyoto Japan
python ./eclipse_forecaster2.py "Phnom Penh" Cambodia
python ./eclipse_forecaster2.py "New York" American
"""


import argparse
import ephem
import sys
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim
from urllib.request import urlretrieve

def download_country_info():
    url = "http://download.geonames.org/export/dump/countryInfo.txt"
    filename = "countryInfo.txt"
    print("Downloading countryInfo.txt...")
    urlretrieve(url, filename)
    print("Download completed.")

def get_coordinates(city, country):
    geolocator = Nominatim(user_agent="city-extractor")
    location = geolocator.geocode(city + ", " + country)
    if location:
        return location.latitude, location.longitude, location.altitude  # Return altitude as sea level elevation
    else:
        return None, None, None

def find_next_eclipse(city, country):
    latitude, longitude, elevation = get_coordinates(city, country)
    if latitude is None or longitude is None:
        print("Unknown city or country:", city + ", " + country)
        return None

    # Create a PyEphem observer object for the specified city and country
    observer = ephem.Observer()
    observer.lat = str(latitude)
    observer.lon = str(longitude)
    observer.elevation = elevation  # Use altitude as sea level elevation

    # Start from the current date and time
    current_time = datetime.utcnow()

    # Variables to store eclipse information
    next_solar_eclipse = None
    next_lunar_eclipse = None

    # Iterate through time to find the next solar or lunar eclipse visible from the specified location
    while not (next_solar_eclipse and next_lunar_eclipse):
        # Compute the position of the Sun and Moon at the current time
        observer.date = current_time
        sun = ephem.Sun(observer)
        moon = ephem.Moon(observer)

        # Compute the angular separation between the Sun and Moon
        separation = ephem.separation(sun, moon)

        # Check if the angular separation is small enough to indicate a solar eclipse
        if separation < ephem.degrees('0:30:00'):  # Threshold for a solar eclipse (0.5 degrees)
            next_solar_eclipse = current_time

        # Check if the angular separation is small enough to indicate a lunar eclipse
        if separation > ephem.pi - ephem.degrees('0:30:00'):  # Threshold for a lunar eclipse (opposite sides of Earth)
            next_lunar_eclipse = current_time

        # Increment time by one day and continue checking
        current_time += timedelta(days=1)

    return next_solar_eclipse, next_lunar_eclipse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the next solar or lunar eclipse visible from a specified city and country.")
    parser.add_argument("city", type=str, help="Name of the city")
    parser.add_argument("country", type=str, help="Name of the country")
    args = parser.parse_args()

    try:
        next_solar_eclipse, next_lunar_eclipse = find_next_eclipse(args.city, args.country)

        if next_solar_eclipse:
            print("Next solar eclipse visible from {}, {}: {}".format(args.city, args.country, next_solar_eclipse.strftime("%Y-%m-%d %H:%M:%S.%f")))
        else:
            print("No solar eclipses visible from {}, {} in the near future.".format(args.city, args.country))

        if next_lunar_eclipse:
            print("Next lunar eclipse visible from {}, {}: {}".format(args.city, args.country, next_lunar_eclipse.strftime("%Y-%m-%d %H:%M:%S.%f")))
        else:
            print("No lunar eclipses visible from {}, {} in the near future.".format(args.city, args.country))

    except Exception as e:
        print("An error occurred:", e)
