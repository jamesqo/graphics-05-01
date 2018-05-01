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
    P = light[COLOR]
    normal = normalize(normal)
    light[LOCATION] = normalize(light[LOCATION])
    view = normalize(view)
    
    cos_theta = dot_product(normal, light[LOCATION])
    diffuse = [x * y * cos_theta for x, y in zip(P, dreflect)]

    cos_alpha = 

def calculate_ambient(alight, areflect):
    return dot_product(alight, areflect)

def calculate_diffuse(light, dreflect, normal):
    normal = normalize(normal)
    light[LOCATION] = normalize(light[LOCATION])
    
    cos_theta = max(0, dot_product(normal, light[LOCATION]))
    return [x * y * cos_theta for x, y in zip(light[COLOR], dreflect)]

def calculate_specular(light, sreflect, view, normal):
    normal = normalize(normal)
    view = normalize(view)

    T = dot_product(normal, light[LOCATION]) * normal
    R = 2 * T - light[LOCATION] 

    x = 16
    cos_alpha = max(0, dot_product(R, view))
    cos_alpha_x = cos_alpha ** x

def limit_color(color):
    pass

#vector functions
def normalize(vector):
    norm = math.sqrt(sum([v**2 for v in vector]))
    return [v / norm for v in vector]

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
