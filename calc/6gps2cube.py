from __future__ import print_function
import math

RADIUS = 6378137
FLATTENING_DENOM = 298.257223563

def FLATTENING():
    return 1 / FLATTENING_DENOM

def POLAR_RADIUS():
    return RADIUS * (1 - FLATTENING())

def RADIUS_SQRT():
    return RADIUS * RADIUS

def POLAR_RADIUS_SQRT():
    return POLAR_RADIUS() * POLAR_RADIUS()

def ECCENTRICITY2():
    return (2 - FLATTENING()) * FLATTENING()

def ECCENTRICITY():
    return math.sqrt((RADIUS_SQRT() - POLAR_RADIUS_SQRT()) / RADIUS_SQRT())

def ECCENTRICITY_PRIME():
    return math.sqrt((RADIUS_SQRT() - POLAR_RADIUS_SQRT()) / POLAR_RADIUS_SQRT())

print(RADIUS)
print(FLATTENING_DENOM)
print(FLATTENING())
print(POLAR_RADIUS())

def LLAToECEF(lat, lon, alt=0):
    print(lat, lon, alt)
    rlat = lat / 180 * math.pi
    rlon = lon / 180 * math.pi

    slat = math.sin(rlat)
    clat = math.cos(rlat)

    N = RADIUS / math.sqrt(1 - ECCENTRICITY2() * slat * slat)

    x = (N + alt) * clat * math.cos(rlon)
    y = (N + alt) * clat * math.sin(rlon)
    z = (N * (1 - ECCENTRICITY2()) + alt) * slat

    return [x, y, z]

def getN(latitude):
    sinlatitude = math.sin(latitude)
    denom = math.sqrt(1 - ECCENTRICITY() * ECCENTRICITY() * sinlatitude * sinlatitude)
    N = RADIUS / denom
    return N

def degrees(angle):
    return angle * (180 / math.pi)

[X, Y, Z] = LLAToECEF(10, 12, 20)
print([X, Y, Z])

def coord_round(x):
    return int(x) if x >= 0 else int(x) - 1

(x, y, z) = (coord_round(coord) for coord in (X, Y, Z))
print('x, y, z =', x, y, z)

square_number = max(y + 1, z + 1, -y, -z)
print('square_number =', square_number)

left_top = (2 * (square_number - 1)) ** 2 + 1
right_top = left_top + 2 * square_number - 1
right_bottom = right_top + 2 * square_number - 1
left_bottom = right_bottom + 2 * square_number - 1

print('corners =', left_top, right_top, right_bottom, left_bottom)

if square_number == - y: # left side
    if square_number == z + 1: # top-left corner
        cube_p = left_top
    else:
        cube_p = z + left_bottom + square_number
elif square_number == y + 1: # right side
    cube_p = right_top + square_number - 1 - z
elif square_number == z + 1: # top side
    cube_p = right_top - square_number - y
else: # square_number == - z, bottom side
    cube_p = right_bottom + square_number - y

print('cube_p =', cube_p)

if x >= 0:
    slice_number = x * 2
else:
    slice_number = -x * 2 - 1

code = slice_number * 441000000000000 + cube_p

print('code =', code)