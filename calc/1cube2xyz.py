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
    
print('X_meters: ' , X_meters) 
print('Y_meters: ' , Y_meters)
print('Z_meters: ' , Z_meters)