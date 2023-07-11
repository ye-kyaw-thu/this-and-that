# -*- coding: utf-8 -*-
"""
Last updated: 11 July 2023
@author: Ye Kyaw Thu, LU Lab., Myanmar
How to run:
python tz_converter.py -h

python tz_converter.py "10:57 PM EST"
python tz_converter.py "8:00 pm pst"
python tz_converter.py "8:00, AM, UTC"

python tz_converter.py -l
"""

import sys
import argparse
from datetime import datetime
import pytz
import pycountry

# Define the timezones
zones = {
    "PST": pytz.timezone('America/Los_Angeles'),
    "EST": pytz.timezone('America/New_York'),
    "UTC": pytz.timezone('UTC'),
    "IST": pytz.timezone('Asia/Kolkata'),
    "GMT": pytz.timezone('Etc/GMT'),
}

# Define the countries for each timezone
zone_countries = {
    "PST": ["US", "CA", "MX"],
    "EST": ["US", "CA", "MX", "PA", "EC", "PE", "CO"],
    "UTC": ["GH", "IS", "CI", "BF", "GM", "SN", "ML", "GN", "GW", "SL", "LR"],
    "IST": ["IN"],
    "GMT": ["GB", "IE", "PT", "IS", "GH", "CI", "BF", "GM", "SN", "ML", "GN", "GW", "SL", "LR"]
}

def list_countries():
    for zone, country_codes in zone_countries.items():
        countries = [pycountry.countries.get(alpha_2=cc).name for cc in country_codes]
        print(f"{zone}: {', '.join(countries)}")

def convert_time(input_time, input_zone, output_zone):
    # Parse the input time and attach the input timezone
    naive_datetime = datetime.strptime(input_time, "%I:%M %p")
    aware_datetime = zones[input_zone].localize(naive_datetime)
    
    # Convert to the output timezone
    output_datetime = aware_datetime.astimezone(zones[output_zone])
    
    return output_datetime.strftime("%I:%M %p")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Convert time between timezones.")

    # Add the arguments
    parser.add_argument('Time', metavar='Time', type=str, help='the time to be converted in the format "HH:MM AM/PM TZ" or "HH:MM, AM/PM, TZ"', nargs='?')
    parser.add_argument('-l', '--list', action='store_true', help='List countries associated with each timezone')

    # Parse the arguments
    args = parser.parse_args()

    if args.list:
        list_countries()
        return

    if not args.Time:
        parser.error('Time is required unless --list is provided')

    # Remove commas and split the input
    input_parts = args.Time.replace(",", "").split(" ")
    input_time = " ".join(input_parts[:2]).upper()
    input_zone = input_parts[2].upper()

    # Validate the input timezone
    if input_zone not in zones.keys():
        print("Invalid timezone! Please enter a valid timezone: PST, EST, UTC, IST, or GMT.")
        return

    # Convert and print for each output timezone
    for output_zone in zones.keys():
        if output_zone == input_zone:
            continue
        output_time = convert_time(input_time, input_zone, output_zone)
        print(f"{output_time} {output_zone}")

if __name__ == "__main__":
    main()
