from plane_detector.plane_detector import PlaneDetector
import requests
from plane_detector.config import OPENSKY_API_ENDPOINT


def test_connect():
    assert requests.get(OPENSKY_API_ENDPOINT).ok


def test_detectors_return_similar_results():
    pd = PlaneDetector()
    assert pd.detect() == pd.detect_smart()


def test_output_format():
    pd = PlaneDetector()
    field_names = ('lat', 'long', 'distance', 'flight_code', 'icao24')
    for i in pd.detect():
        for field_name in field_names:
            assert field_name in i
