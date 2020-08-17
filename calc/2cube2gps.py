from __future__ import print_function
import math

cube = 3141592653589793238462
a = 441000000000000 
cube_projection = (cube % a) 
half_of_1 = (1/2.0)
n_squareference = (((cube_projection - 1) ** half_of_1) / 2) + 1 
n_squareference = int(n_squareference)

right_top = (2 * (n_squareference - 1)) ** 2 + 2 * n_squareference
right_bottom = right_top + 2 * n_squareference - 1
left_bottom = right_bottom + 2 * n_squareference - 1

if cube_projection >= right_top and cube_projection <= right_bottom:
    Y_meters = n_squareference
elif cube_projection >= left_bottom:
    Y_meters = -n_squareference + 1
elif cube_projection < right_top:
    Y_meters = cube_projection - right_top + n_squareference
else: 
    Y_meters = right_bottom - cube_projection + n_squareference
Y_meters -= 0.5
    
if cube_projection <= right_top:
    Z_meters = n_squareference - 1
elif cube_projection >= right_bottom and cube_projection <= left_bottom:
    Z_meters = -n_squareference
elif cube_projection < right_bottom:
    Z_meters = right_top - cube_projection + n_squareference - 1
else: 
    Z_meters = cube_projection - left_bottom - n_squareference
Z_meters += 0.5

n_layer = cube / a
n_layer = int(n_layer)
n_layer += 1

if ((n_layer % 2) != 0 ): 
    X_meters = n_layer / float(2) 

if ((n_layer % 2) == 0 ):     
    X_meters =  - (n_layer - 1) / float(2) 
    
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