import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

# lighting functions
# areflect, dreflect, sreflect hold constants of ambient/diffuse/specular reflection?
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    normal = normalize(normal)
    light[LOCATION] = normalize(light[LOCATION])
    view = normalize(view)
    
    amb = calculate_ambient(alight=ambient, areflect=areflect)
    diffuse = calculate_diffuse(light, dreflect, normal)
    specular = calculate_specular(light, sreflect, view, normal)

    return limit_color([a + d + s for a, d, s in zip(amb, diffuse, specular)])

def calculate_ambient(alight, areflect):
    return limit_color([x * y for x, y in zip(alight, areflect)])

def calculate_diffuse(light, dreflect, normal):
    normal = normalize(normal)
    light[LOCATION] = normalize(light[LOCATION])
    
    cos_theta = max(0, dot_product(normal, light[LOCATION]))
    return limit_color([x * y * cos_theta for x, y in zip(light[COLOR], dreflect)])

def calculate_specular(light, sreflect, view, normal):
    normal = normalize(normal)
    view = normalize(view)

    norm_T = dot_product(normal, light[LOCATION])
    T = [norm_T * t for t in normal]
    R = [2 * t - loc for t, loc in zip(T, light[LOCATION])]

    x = 16
    cos_alpha = max(0, dot_product(R, view))
    cos_alpha_x = cos_alpha ** x
    return limit_color([x * y * cos_alpha_x for x, y in zip(light[COLOR], sreflect)])

def limit_color(color):
    # NB: The int() is needed to keep it from spazzing out bigtime
    return [int(max(0, min(255, val))) for val in color]

#vector functions
def normalize(vector):
    norm = math.sqrt(sum([v**2 for v in vector]))
    return [float(v) / norm for v in vector]

def dot_product(a, b):
    assert len(a) == len(b)
    return sum([aa * bb for aa, bb in zip(a, b)])

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
