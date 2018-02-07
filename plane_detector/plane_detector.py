#!/usr/bin/env python

import requests
import geopy.distance

from tabulate import tabulate
from plane_detector.config import OPENSKY_API_ENDPOINT, CITY_COORDS, MAX_DISTANCE_FROM_CITY_KM


def calculate_distance(to_lat, to_long, lat, long):
    """
    Calculates distances between two points on map
    :return: distance, km: float
    """
    return geopy.distance.vincenty((to_lat, to_long), (lat, long)).km


class PlaneDetector:
    def detect(self, max_distance=MAX_DISTANCE_FROM_CITY_KM):
        """
        Detects planes withing constant distance in km from Paris (default 450 unless changed in config).
        :return: list of dicts: {'flight_code': str if found,
                                 'lat': float,
                                 'long': float,
                                 'distance': float}
        """
        paris_lat, paris_long = CITY_COORDS
        r = requests.get(OPENSKY_API_ENDPOINT)
        if not r.ok:
            return None
        r_json = r.json()['states']

        result = []

        for i in r_json:
            lat, long = i[6], i[5]
            if lat and long:
                # won't use (*CITY_COORDS, lat, long) since it would make the code incompatible with Python < 3.5
                distance = calculate_distance(paris_lat, paris_long, lat, long)
                if distance <= max_distance:
                    result.append({'icao24': i[0],
                                   'flight_code': i[1],
                                   'lat': lat,
                                   'long': long,
                                   'distance': distance})

        return result

    def detect_smart(self, max_distance=MAX_DISTANCE_FROM_CITY_KM):
        """
        Alternative implementation, made for the sake of demonstration an example of bad coding. One line though.
        Doesn't work with Python < 3.5
        """
        return [{'icao24': i[0], 'flight_code': i[1], 'lat': i[6], 'long': i[5], 'distance': calculate_distance(*CITY_COORDS, i[6], i[5])} for i in filter(lambda i: i[6] and i[5] and calculate_distance(*CITY_COORDS, i[6], i[5]) < max_distance, requests.get(OPENSKY_API_ENDPOINT).json()['states'])]


def execute():
    detector = PlaneDetector()
    planes = detector.detect()
    if planes:
        print("Here's a list of planes within %s km from Paris" % int(MAX_DISTANCE_FROM_CITY_KM))
        headers = ('ICAO24', 'Flight Code', 'Lat', 'Long', 'Distance')
        print(tabulate([
            [plane['icao24'], plane['flight_code'], plane['lat'], plane['long'], plane['distance']] for plane in planes
        ], headers=headers))
