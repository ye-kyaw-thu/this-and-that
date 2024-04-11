# Try to Predict Next Eclipse Date

## 1st Version

[eclipse_forecaster.py](https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/eclipse_forecaster.py)    

```python
"""
Try to forecast next eclipse date.
Written by Ye Kyaw Thu, LST Lab., Myanmar
Last updated: 11 April 2024

Reference:
https://pypi.org/project/ephem/

Usage:
python ./eclipse_forecaster.py --help
python ./eclipse_forecaster.py Mandalay Myanmar
python ./eclipse_forecaster.py Bagan Myanmar
python ./eclipse_forecaster.py Kyoto Japan
python ./eclipse_forecaster.py "Phnom Penh" Cambodia
python ./eclipse_forecaster.py "New York" American
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

def find_next_solar_eclipse(city, country):
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

    # Iterate through time to find the next solar eclipse visible from the specified location
    while True:
        # Compute the position of the Sun and Moon at the current time
        observer.date = current_time
        sun = ephem.Sun(observer)
        moon = ephem.Moon(observer)

        # Compute the angular separation between the Sun and Moon
        separation = ephem.separation(sun, moon)

        # Check if the angular separation is small enough to indicate a solar eclipse
        if separation < ephem.degrees('0:30:00'):  # Threshold for a solar eclipse (0.5 degrees)
            return current_time

        # Increment time by one day and continue checking
        current_time += timedelta(days=1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the next solar eclipse visible from a specified city and country.")
    parser.add_argument("city", type=str, help="Name of the city")
    parser.add_argument("country", type=str, help="Name of the country")
    args = parser.parse_args()

    try:
        next_eclipse_time = find_next_solar_eclipse(args.city, args.country)
        if next_eclipse_time:
            print("Next solar eclipse visible from {}, {}: {}".format(args.city, args.country, next_eclipse_time.strftime("%Y-%m-%d %H:%M:%S.%f")))
    except Exception as e:
        print("An error occurred:", e)

```

## Example Usage or Running Results with the Code (1st version)

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py "Phnom Penh" Cambodia
Next solar eclipse visible from Phnom Penh, Cambodia: 2031-05-21 10:05:35.789874
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py Mandalay Myanmar
Next solar eclipse visible from Mandalay, Myanmar: 2053-09-12 10:05:45.561972
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py Kyoto Japan
Next solar eclipse visible from Kyoto, Japan: 2059-11-05 10:05:58.648681
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py "New York" American
Next solar eclipse visible from New York, American: 2025-03-29 10:06:10.459513
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py Bagan Myanmar
Next solar eclipse visible from Bagan, Myanmar: 2053-09-12 10:06:19.684058
```

## Note

သတိထားစေချင်တာက ဒီ တွက်ထားတဲ့ ပရိုဂရမ်က ကျွန်တော်စိတ်ဝင်စားလို့ Python library သုံးခုကို သုံးပြီးစမ်းထားတာပါ။ အချိန်တို့ ရက်တို့က အမှန်တကယ် eclipse ဖြစ်တာနဲ့လွဲသွားနိုင်တာတွေ ရှိနိုင်ပါတယ်။ တကယ်ကတော့ eclipse ရက်ကို တွက်တဲ့ နည်းလမ်းတွေက တစ်မျိုးထက်မကရှိပါတယ်။ ပြီးတော့ sea level ကို ထည့်တာနဲ့ မထည့်တာနဲ့မှာ ရလဒ်က ကွဲသွားနိုင်တယ်။ ဥပမာ ဒီအောက်က ရလဒ်တွေက sea level ကို ထည့်မစဉ်းစားပဲ ရေးထားတဲ့ code ကို run ကြည့်တုန်းက ရတဲ့ ရလဒ်တွေပါ။ ဗဟုသုတရအောင်လို့ ယှဉ်ကြည့်နိုင်အောင်လို့ ...  

### Results without Sea level Information

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py "Phnom Penh" Cambodia
Next solar eclipse visible from Phnom Penh, Cambodia: 2031-05-21 09:57:32.352972
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py Mandalay Myanmar
Next solar eclipse visible from Mandalay, Myanmar: 2059-11-05 09:57:44.626437
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py Kyoto Japan
Next solar eclipse visible from Kyoto, Japan: 2059-11-05 09:57:56.366491
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py "New York" American
Next solar eclipse visible from New York, American: 2025-03-29 09:58:13.720870
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py Bagan Myanmar
Next solar eclipse visible from Bagan, Myanmar: 2059-11-05 09:58:24.353944
```

## Updated Version  

ဒီဗားရှင်းမှာတော့ eclipse of the moon or sun ဆိုတဲ့ အချက်အလက်တွေပါအောင် ကြိုးစားကြည့်ထားတာပါ။  

```python
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
```

## Results with the Updated Version

shell script preparation ...  

```bash
#!/bin/bash

set -x;
python ./eclipse_forecaster2.py Mandalay Myanmar
python ./eclipse_forecaster2.py Bagan Myanmar
python ./eclipse_forecaster2.py Kyoto Japan
python ./eclipse_forecaster2.py "Phnom Penh" Cambodia
python ./eclipse_forecaster2.py "New York" American
set +x;
```

Running results ...  

```
(base) yekyaw.thu@gpu:~/tmp$ ./run-eclipse_forecaster2.sh
+ python ./eclipse_forecaster2.py Mandalay Myanmar
Next solar eclipse visible from Mandalay, Myanmar: 2059-11-05 11:08:58.903177
Next lunar eclipse visible from Mandalay, Myanmar: 2059-11-19 11:08:58.903177
+ python ./eclipse_forecaster2.py Bagan Myanmar
Next solar eclipse visible from Bagan, Myanmar: 2059-11-05 11:09:00.458928
Next lunar eclipse visible from Bagan, Myanmar: 2059-11-19 11:09:00.458928
+ python ./eclipse_forecaster2.py Kyoto Japan
Next solar eclipse visible from Kyoto, Japan: 2034-03-20 11:09:02.087025
Next lunar eclipse visible from Kyoto, Japan: 2044-09-07 11:09:02.087025
+ python ./eclipse_forecaster2.py 'Phnom Penh' Cambodia
Next solar eclipse visible from Phnom Penh, Cambodia: 2059-11-05 11:09:03.349331
Next lunar eclipse visible from Phnom Penh, Cambodia: 2059-11-19 11:09:03.349331
+ python ./eclipse_forecaster2.py 'New York' American
Next solar eclipse visible from New York, American: 2048-06-11 11:09:04.870118
Next lunar eclipse visible from New York, American: 2054-08-18 11:09:04.870118
+ set +x
```

## To Do

တွက်ပြီးထွက်လာတဲ့ ရက်တွေကို အောက်ပါ site တွေနဲ့ confirmation လုပ်ကြည့်ရန် ...  

- [https://eclipse.gsfc.nasa.gov/eclipse.html](https://eclipse.gsfc.nasa.gov/eclipse.html)  
- [https://www.timeanddate.com/eclipse/list.html](https://www.timeanddate.com/eclipse/list.html)    
