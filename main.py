import pgzrun
import numpy

m1=100
m2=100
m3=100
v1 = numpy.array([0, 47])
v2 = numpy.array([-10, -30])
v3 = numpy.array([20, -25])
p1 = numpy.array([500,280])
p2 = numpy.array([110,330])
p3 = numpy.array([340,150])
G = 100000
MIN_R = 40.0

def draw():
    screen.fill((255 ,255 ,255))
    screen.draw.filled_circle(p2, 25.0, (120, 50, 255))
    screen.draw.filled_circle(p1, 25.0, (150, 200, 100))
    screen.draw.filled_circle(p3, 25.0, (150, 100, 50))

def update(dt):
    global p1,v1,p2,v2,p3,v3
    p1 = p1 + dt * v1
    p2 = p2 + dt * v2
    p3 = p3 + dt * v3
    r12 = max(MIN_R, numpy.linalg.norm(p2 - p1))
    r13 = max(MIN_R, numpy.linalg.norm(p3 - p1))
    r23 = max(MIN_R, numpy.linalg.norm(p2 - p3))
    f12 = G * m1 * m2 * (p2 - p1) / pow(r12, 3)
    f13 = G * m1 * m3 * (p3 - p1) / pow(r13, 3)
    f23 = G * m2 * m3 * (p3 - p2) / pow(r23, 3)
    v1 = v1 + dt * (f12 + f13) / m1
    v2 = v2 + dt * (-f12 + f23) / m2
    v3 = v3 + dt * (-f23 + -f13) / m3

pgzrun.go()
