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