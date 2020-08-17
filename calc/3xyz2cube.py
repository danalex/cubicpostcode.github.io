from sys import argv

def coord_round(x):
    return int(x) if x >= 0 else int(x) - 1

if len(argv) == 4:
    X = float(argv[1])
    Y = float(argv[2])
    Z = float(argv[3])
else:
    X = 3561896.5
    Y = -8402969.5
    Z = -9767161.5

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