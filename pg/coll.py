from math import sqrt

def collide(ball1, ball2):
    v1new = calc_speed(ball1, ball2)
    v2new = calc_speed(ball2, ball1)
    return [v1new, v2new]

def calc_speed(ball1, ball2):
    m1 = m2 = 1
    v1 = ball1[3]
    v2 = ball2[3]
    x1 = ball1[0]
    x2 = ball2[0]
    xd = vdiff(x1, x2)
    vd = vdiff(v1, v2)
    if norm(xd) == 0:
       print(ball1, ball2)
    coeff = 2*m2 / (m1 + m2) * dot_prod(vd, xd) / (norm(xd) * norm(xd))
    xds = vmult(xd, coeff)
    return vdiff(v1, xds)

def dot_prod(v1, v2):
   return sum([a[0] * a[1] for a in zip(v1, v2)])

def norm(v):
   return sqrt(sum([a*a for a in v]))

def vdiff(v1, v2):
   return [a[0] - a[1] for a in zip(v1, v2)]

def vmult(v, s):
   return [a*s for a in v]
