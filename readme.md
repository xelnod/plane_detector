# Description
Lists all airplanes within 450 km from Paris as a list. 

Includes ICAO 24-bit aircraft identification code, flight code (if given), coordinates and distance to Paris.  

# Requirements
- Python 3.5+

# Installation
- As an archive:
1. Download plane-detector-0.1.tar.gz
2. Unzip: `$ tar -xf plane-detector-0.1.tar.gz` <br>
(if you're reading this, you probably already have done that)
3. `$ cd plane_detector-0.1`
4. `$ pip install .`
- From repository:
1. `$ git clone git@github.com:xelnod/plane_detector.git`
2. `$ pip install .` 

# Usage:
`$ plane-detector`

# Testing:
1. `$ cd plane_detector-0.1`
2. `$ py.test plane_detector/tests.py`
