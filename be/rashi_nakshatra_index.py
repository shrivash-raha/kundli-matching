import swisseph as swe
import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
import certifi
import ssl
from geopy.geocoders import Nominatim

# Constants
NAKSHATRA_SEGMENT = 13.333333  # 360° / 27 nakshatras
RASHI_SEGMENT = 30             # 360° / 12 rashis

# Get location coordinates and timezone
def get_location_data(place):
    ctx = ssl.create_default_context(cafile=certifi.where())
    geolocator = Nominatim(user_agent="kundli-matching", ssl_context=ctx)
    location = geolocator.geocode(place)
    if not location:
        raise ValueError("Place not found")
    
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone = pytz.timezone(timezone_str)

    if timezone_str is None:
        raise ValueError("Could not determine timezone for the given location")

    
    # return 28.667, 77.217, timezone
    return location.latitude, location.longitude, timezone

# Convert local time to Julian Day
def get_julian_day(date_str, time_str, timezone):
    dt = datetime.datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    dt_local = timezone.localize(dt)
    dt_utc = dt_local.astimezone(pytz.utc)
    julian_day = swe.julday(dt_utc.year, dt_utc.month, dt_utc.day, 
                            dt_utc.hour + dt_utc.minute/60.0)
    return julian_day

# Get Moon longitude and derive Nakshatra and Rashi
def get_moon_position(julian_day, latitude, longitude):
    swe.set_topo(longitude, latitude, 0)
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    moon_pos = swe.calc_ut(julian_day, swe.MOON)[0]  # returns tuple (longitude, speed, etc.)

    moon_long = moon_pos[0]
    nakshatra_index = int(moon_long // NAKSHATRA_SEGMENT)
    rashi_index = int(moon_long // RASHI_SEGMENT)
    
    return {
        "moon_longitude": moon_long,
        "nakshatra_index": nakshatra_index + 1,  # 1 to 27
        "rashi_index": rashi_index + 1           # 1 to 12
    }

# Main function for one person
def analyze_person_kundli(dob, tob, place):
    lat, lon, timezone = get_location_data(place)
    jd = get_julian_day(dob, tob, timezone)
    moon_data = get_moon_position(jd, lat, lon)
    return moon_data
