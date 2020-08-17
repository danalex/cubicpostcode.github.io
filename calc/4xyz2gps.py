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

def ECEFToLLA(X, Y, Z):
    p = math.sqrt(X * X + Y * Y)
    theta = math.atan((Z * RADIUS) / (p * POLAR_RADIUS()))

    sinTheta = math.sin(theta)
    cosTheta = math.cos(theta)

    num = Z + ECCENTRICITY_PRIME() * ECCENTRICITY_PRIME() * POLAR_RADIUS() * sinTheta * sinTheta * sinTheta
    denom = p - ECCENTRICITY() * ECCENTRICITY() * RADIUS * cosTheta * cosTheta * cosTheta

    latitude = math.atan(num / denom)
    longitude = math.atan(Y / X)
    N = getN(latitude)
    altitude = (p / math.cos(latitude)) - N

    if X < 0 and Y < 0:
        longitude = longitude - math.pi

    if X < 0 and Y > 0:
        longitude = longitude + math.pi

    return [degrees(latitude), degrees(longitude), altitude]

def getN(latitude):
    sinlatitude = math.sin(latitude)
    denom = math.sqrt(1 - ECCENTRICITY() * ECCENTRICITY() * sinlatitude * sinlatitude)
    N = RADIUS / denom
    return N

def degrees(angle):
    return angle * (180 / math.pi)

#[X, Y, Z] = LLAToECEF(10, 12, 20)
#print([X, Y, Z])
print(ECEFToLLA(X, Y, Z))